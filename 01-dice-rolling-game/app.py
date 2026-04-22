from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# Takes user request to roll the number of dice, otherwise rolls two dice
@app.route("/roll")
def game():
    num = int(request.args.get("dice", 2))
    rolls = []
    for _ in range(num):
        die = random.randint(1,6)
        rolls.append(die)
    # return str(rolls)
    return jsonify({"rolls": rolls})

if __name__ == "__main__":
    app.run(debug=True)