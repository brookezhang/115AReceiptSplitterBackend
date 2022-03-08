import json
import os, sys
sys.path.insert(1, os.getcwd()) 
from ocr import ReceiptOcr

if __name__ == '__main__':
    img_data = json.load(open('./testing/receipt.json'))
    ocrObj = ReceiptOcr()
    foundItems = ocrObj.get_ocr(img_data['img_string'])
    print(foundItems)
 