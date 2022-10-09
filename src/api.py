from flask import Flask, jsonify

from algorithms.singlePipe import get_pipeline
from db import is_correct_role, get_available_roles
from models import get_digest, get_insights, get_trends

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello! We have urls:</p>" \
           "<p>" \
           "<ul>" \
           "<li>/insights</li>" \
           " <li>/digest/SOME_ROLE , ex. /digest/accountant or /digest/director</li>" \
           "<li>/trends</li>" \
           "</ul>" \
           "</p>"


@app.route("/insights")
def insight():
    return jsonify(get_insights())


@app.route("/trends")
def trends():
    return jsonify(get_trends())


@app.route("/digest/<role>")
def digest(role: str):
    if is_correct_role(role):
        return jsonify(get_digest(role))
    return jsonify({"error": f"No such role: {role}. We have roles likes: {get_available_roles()}"})


if __name__ == '__main__':
    get_pipeline()
    app.run(host="0.0.0.0", port=5000)
