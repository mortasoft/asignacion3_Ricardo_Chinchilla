from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppass"),
        database=os.getenv("DB_NAME", "secureapp")
    )


@app.route("/")
def home():
    return """
    <h1>Aplicación vulnerable a SQL Injection</h1>
    <p>Endpoints:</p>
    <ul>
      <li>GET /users?id=1</li>
      <li>POST /login  (username, password)</li>
    </ul>
    """


@app.route("/users", methods=["GET"])
def get_user():
    user_id = request.args.get("id", "")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # VULNERABLE: concatenación directa
    query = f"SELECT id, username, email, role FROM users WHERE id = {user_id}"
    print("Executing query:", query)
    cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # VULNERABLE: concatenación directa
    query = (
        f"SELECT id, username, role FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    print("Executing query:", query)
    cursor.execute(query)

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({"message": "Login exitoso", "user": user})
    return jsonify({"message": "Credenciales inválidas"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
