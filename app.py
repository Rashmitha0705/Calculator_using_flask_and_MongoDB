from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["calculator_db"]
history_collection = db["history"]

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        equation = request.json['equation']
        result = request.json['result']
        save_history(equation, result)

    return render_template("calculator.html", history=get_history())

def save_history(equation, result):
    history = {
        "equation": equation,
        "result": result,
        "created_on": datetime.now()
    }
    history_collection.insert_one(history)

def get_history():
    history = list(history_collection.find({}, {"_id": 0}))
    return history

if __name__ == "__main__":
    app.run(debug=True)
