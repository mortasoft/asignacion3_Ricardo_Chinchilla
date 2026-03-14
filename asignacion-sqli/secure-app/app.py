from flask import Flask, request, jsonify, render_template
import mysql.connector
import os
import re

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppass"),
        database=os.getenv("DB_NAME", "secureapp")
    )


def is_valid_username(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", value))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/users", methods=["GET"])
def get_user():
    user_id = request.args.get("id", "")

    if not user_id.isdigit():
        return jsonify({"error": "Parámetro id inválido"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # SEGURO: consulta parametrizada
    query = "SELECT id, username, email, role FROM users WHERE id = %s"
    cursor.execute(query, (int(user_id),))

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not is_valid_username(username):
        return jsonify({"error": "Username inválido"}), 400

    if len(password) < 3 or len(password) > 100:
        return jsonify({"error": "Password inválido"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # SEGURO: consulta parametrizada
    query = "SELECT id, username, role FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({"message": "Login exitoso", "user": user})
    return jsonify({"message": "Credenciales inválidas"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
