from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Drink more coffer RIGHT NOW!!"

app.run(host="0.0.0.0", port=80)