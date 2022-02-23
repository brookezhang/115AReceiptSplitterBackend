from flask import Flask, request
from AzureReceiptRec import AzureReceipt
app = Flask(__name__)

@app.route('/get_items')
def get_items():
    reciept = request.json
    imgStr = reciept["base64"]
    r = AzureReceipt()
    return r.get(imgStr) 

app.run(host='127.0.0.1', port=5000) # if on PC, use '0.0.0.0' instead
