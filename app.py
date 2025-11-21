from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="color: green;">Welcome to My Flask App Home Page</h1>'

@app.route("/info")
def srtechopsinfo():
    return '<h1 style="color: violet;">****Welcome to SUNDARJEE DevOps Journey---Thank You</h1>'

@app.route("/contact")
def srtechopsmobilenumber():
    return '<h1 style="color:red;">FOR TRAINING ENQUIRY: +91 9688023053</h1>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
