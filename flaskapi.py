from flask import Flask, request
from AzureReceiptRec import AzureReceipt
import json
app = Flask(__name__)

@app.route('/get_items', methods=['POST'])
def get_items():
    reciept = request.json
    imgStr = reciept["base64"]
    r = AzureReceipt()
    t = r.get(imgStr)
    if t == 'Error':
        return json.dumps("Error"), 400
    else:
        return t, 200


app.run(host='127.0.0.1', port=5000) # if on PC, use '0.0.0.0' instead
