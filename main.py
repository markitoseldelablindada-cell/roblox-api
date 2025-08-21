from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Buscar usuario por nombre
@app.route("/user")
def user_info():
    username = request.args.get("username")
    resp = requests.post(
        "https://users.roblox.com/v1/usernames/users",
        json={"usernames": [username], "excludeBannedUsers": True}
    )
    data = resp.json()
    if data["data"]:
        return jsonify(data["data"][0])
    return jsonify({"error": "Usuario no encontrado"}), 404

# Obtener seguidores
@app.route("/followers")
def followers():
    user_id = request.args.get("userId")
    resp = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followers?limit=100")
    return jsonify(resp.json())

# Obtener seguidos
@app.route("/following")
def following():
    user_id = request.args.get("userId")
    resp = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followings?limit=100")
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
