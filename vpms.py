from pymongo import MongoClient
from flask import Flask, render_template, request

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")
db=client["vpmsdb"]

@app.route('/')
def home():
    return render_template('index.php')


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0')
