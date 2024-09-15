
from flask import Flask, jsonify
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/api/v1/fake-data")
def fake_data():
    return {
        "name": "John Doe",
        "age": 30,
        "location": "New York"
    }

@app.route("/api/v1/test-mysql")
def test_mysql():
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    mysql_database = os.getenv("MYSQL_DATABASE")

    # ENV vars check
    if not mysql_host or not mysql_user or not mysql_password or not mysql_database:
        return jsonify({"error": "Missing environment variables"}), 500

    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM test_table")
            records = cursor.fetchall()
            cursor.close()
            connection.close()
            return jsonify({"data": records}), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
