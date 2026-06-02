from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from rag_engine import generate_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    bot_response = generate_response(
        user_message
    )

    return jsonify({
        "response": bot_response
    })

if __name__ == "__main__":
    app.run(debug=True)