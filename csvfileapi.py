from flask import Flask, app, jsonify, request
import csv
app = Flask(__name__)

@app.route('/',methods=['GET'])
def get():
    return jsonify("Welcome")
@app.route('/details',methods=['GET'])
def read():
    f = open("det.csv",'r',newline='\r\n')
    s_reader = csv.DictReader(f)
    for i in s_reader:
        return (i)
    f.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')
