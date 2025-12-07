from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="mydb"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM entries")
    data = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return render_template("index.html", entries=data)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (name) VALUES (%s)", (username,))
    conn.commit()
    cursor.close()
    conn.close()

    return ("<h1>Saved! Go back to <a href='/'>Home</a></h1>")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
