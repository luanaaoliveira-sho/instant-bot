from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bot-callback", methods=["POST"])
def callback():
    data = request.get_json()

    if data.get("event_type") == "event_verification":
        challenge = data["event"]["seatalk_challenge"]

        return jsonify({
            "seatalk_challenge": challenge
        })

    return "", 200

@app.route("/")
def home():
    return "Bot online", 200
