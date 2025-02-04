from flask import Flask, request
from ocr import ReceiptOcr
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps("TabDrop Backend!")

@app.route('/items', methods=['GET','POST'])
def items():
    reciept = request.json
    imgStr = reciept["base64"]
    ocrObj = ReceiptOcr()
    foundItems = ocrObj.do_ocr(imgStr)
    code = 200
    if foundItems == "Error":
        code = 400
    return foundItems, code
