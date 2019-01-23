# Import installed packages
from flask import Flask, jsonify

# Import app code
app = Flask(__name__)

# Setup app
from .core import app_setup


@app.route("/api/")
def root():
    return jsonify({"message": "Wassup World"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
