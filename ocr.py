import json
import base64
import os
from dotenv import load_dotenv
from flask import Flask, request
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

class ReceiptOcr:
    # sets up credentials for Azure api
    # input: NONE 
    # output: azure api object 
    def get_credentials(self):
        load_dotenv()
        API_KEY = os.getenv('API_KEY')
        ENDPOINT = os.getenv('ENDPOINT')
        return FormRecognizerClient(ENDPOINT, AzureKeyCredential(API_KEY))

    # get_receipt(): Converts base64 string to receipt_pic.jpeg file 
    # input: none 
    # output: receipt image file
    def get_receipt(self, img_str):
        with open("./receipt_pic.jpeg","wb") as fh:
            fh.write(base64.b64decode(img_str))

        # open and read image for azure api object
        with open("./receipt_pic.jpeg", "rb") as fd:
            receipt = fd.read()
            return receipt

    def create_item(self, name, value):
        entry = {}
        entry['item_name'] = name
        entry['price'] = value
        return entry

    # parse_receipt(receipt, form_recognizer_client): runs azure recognizer on receipt image 
    # input: read receipt image file object, form recognizer client object
    # output: list of receipt items in the form of [{item_name : str}, {price : int}, ...]
    # Used code from this website:
    # https://docs.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.formrecognizerclient?view=azure-python#azure-ai-formrecognizer-formrecognizerclient-begin-recognize-receipts
    def parse_receipt(self, receipt, form_recognizer_client):
        # scans picture using premade-receipt recoginizer
        poller = form_recognizer_client.begin_recognize_receipts(receipt, locale='en-US')
        if not poller:
            return 'Error'
        receipts = poller.result()
        if not receipts:
            return 'Error'
        item_list = [] # dictionary to hold receipt items and their values

        for idx, receipt in enumerate(receipts):
            if not receipt.fields: 
                return 'Error'
            if receipt.fields.get('Items'):
                for idx, item in enumerate(receipt.fields.get('Items').value):         
                    item_name = item.value.get('Name')
                    item_entry = {}
                    if item_name:
                        item_entry['item_name'] = item_name.value 
                    item_total_price = item.value.get('TotalPrice')
                    if item_total_price:
                        item_entry['price'] = item_total_price.value
                    if 'price' in item_entry:
                        item_list.append(item_entry)
            subtotal = receipt.fields.get('Subtotal')
            if subtotal:
                if subtotal.value:
                    item_list.append(self.create_item('subtotal', subtotal.value))
                else:
                    return 'Error'
        return item_list

    # gets receipt image data and parses it 
    def get_ocr(self, img_str):
        form_recognizer_client = self.get_credentials()
        receipt = self.get_receipt(img_str) # make b64 string into img file
        items_l = self.parse_receipt(receipt, form_recognizer_client) # run azure api over receipt and return item list
        if items_l == [] or items_l == 'Error':
            return 'Error'
        else:
            return json.dumps(items_l)

