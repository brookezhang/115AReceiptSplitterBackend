from flask import Flask, request
from AzureReceiptRec import AzureReceipt
import json
application = Flask(__name__)

@application.route('/')
def hello_world():
    return json.dumps("Hello World!")

@application.route('/items', methods=['GET','POST'])
def items():
    reciept = request.json
    imgStr = reciept["base64"]
    r = AzureReceipt()
    t = r.get(imgStr)
    print(t)
    if t == 'Error':
        return json.dumps("Error"), 400
    else:
        return t, 200

