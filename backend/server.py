from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from src.rules.obligation_rules import identify_user_obligations
from src.rules.privacy_rules import identify_privacy_related_sections
from src.rules.ip_rules import identify_ip_related_sections
from src.model import SpacyModel
from src.helpers.util import clean_lower, clean_space

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["POST"])
@cross_origin()
def hello():
    content_type = request.headers.get("Content-Type")
    print(request.headers.get("Content-Type"))
    if content_type == "application/json":
        payload = request.json
        text: str = payload["rawText"]
        category: str = payload["category"]
        nlp = SpacyModel.get_small_model()
        text_no_space = clean_space(nlp(text))
        text_lower = clean_lower(nlp(text_no_space))
        doc = nlp(text_lower)
        res = None
        if category == "obligations":
            res = identify_user_obligations(nlp, doc)
        elif category == "privacy":
            res = identify_privacy_related_sections(nlp, doc)
        elif category == "ip":
            res = identify_ip_related_sections(nlp, doc)
        else:
            res = []
        print(f"res is {res}")
        return jsonify({"success": True, "info": res})

    else:
        return jsonify({"success": False})


if __name__ == "__main__":
    app.run(debug=True)
