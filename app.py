from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>RENDER WORKS</h1><p>Hello from Render!</p>"
