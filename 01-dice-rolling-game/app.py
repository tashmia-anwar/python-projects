from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# Takes user request to roll the number of dice, otherwise rolls two dice
@app.route("/roll")
def game():
    try:
        num = int(request.args.get("dice", 2))
        rolls = []
        for _ in range(num):
            die = random.randint(1,6)
            rolls.append(die)
        # return str(rolls)
        return jsonify({"rolls": rolls})
    except ValueError:
        return jsonify({"error": "dice must be a number"})

if __name__ == "__main__":
    app.run(debug=True)