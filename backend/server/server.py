from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        payload = request.json
        print(f"received payload --> {payload}")
        return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
