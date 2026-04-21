from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/roll")
def game():
    rolls = []
    for _ in range(2):
        die = random.randint(1,6)
        rolls.append(die)
    return str(rolls)

if __name__ == "__main__":
    app.run(debug=True)