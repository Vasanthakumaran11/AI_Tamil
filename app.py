from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai   # If using Gemini

app = Flask(__name__)
CORS(app)

# ✅ Replace with your key or environment variable
GEMINI_API_KEY = "YOUR_GEMINI_KEY"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    if not msg:
        return jsonify({"reply": "No message received."})
    try:
        resp = model.generate_content(msg)
        reply = resp.text.strip() if resp.text else "No reply."
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)