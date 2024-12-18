from flask import Flask, send_file 
import json
app = Flask(__name__)

dicty = {
    "status": 'ok',
    "response": {
        "configuration":{
            "isActive":True
        },
        "url":"/otaFile.bin"
    }
}

@app.route('/',methods=['GET'])
def home():
    return "hello"

@app.route('/api/v1/configuration/sync', methods=['POST'])
def verify(resp):
    obj = json.dump(resp)
    if(obj["command"] == "UPDCHK"):
        return json.dumps(dicty)
    else:
        return 404

@app.route('/otaFile.bin',methods=['GET'])
def downlaod():
    return send_file("firmware.bin")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6666)