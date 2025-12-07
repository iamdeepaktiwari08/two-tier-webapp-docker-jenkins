from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Auto Deploy Test 1 — Webhook Working!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
