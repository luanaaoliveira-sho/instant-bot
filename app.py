from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bot-callback", methods=["POST"])
def callback():
    data = request.json

    if data.get("event_type") == "event_verification":
        return jsonify({
            "seatalk_challenge": data["event"]["seatalk_challenge"]
        })

    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)