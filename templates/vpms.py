from pymongo import MongoClient
from flask import Flask, render_template, request

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")
db=client["admin"]

@app.route('/',methods = ['GET','POST'])
@app.route('/register')
def home():
    if( request.method=='POST'):
        name=request.form['name']
        return render_template('result.html',name =name)
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0')
