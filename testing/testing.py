import json
from ocr import ReceiptOcr

if __name__ == '__main__':
    img_data = json.load(open('./receipt.json'))
    ocrObj = ReceiptOcr()
    foundItems = ocrObj.get_ocr(img_data['img_string'])
    print(foundItems)
 