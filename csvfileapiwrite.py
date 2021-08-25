from flask import Flask,jsonify,request
import csv

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def get():
    return ("Welcome")
@app.route('/details',methods=['GET'])
def read():
    f = open("det.csv",'r',newline='\r\n')
    s_reader = csv.DictReader(f)
    for i in s_reader:
        return (i)
    f.close()
@app.route('/details',methods = ['POST'])
def write():
    f = open ("det.csv","w",newline='')
    s_writer = csv.writer(f)
    s_writer.writerow(['id','Name','E-mail'])
    studentdetails = []
    r = request.json['id']
    n= request.json['name']
    m= request.json['email']
    lst=[r,n,m]
    studentdetails.append(lst)
    s_writer.writerows(studentdetails)
    f.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='2000')
    