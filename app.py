from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyC50LcX6xZPO1k__ZRwAOr0CSrGPwDrfnM"
genai.configure(api_key=GEMINI_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")

        model = genai.GenerativeModel("gemini-2.0-flash")

        response = model.generate_content(user_message)
        #ai_response = response.text  

        clean_response = response.text.replace('**', '') 
        clean_response = clean_response.replace('*', '') 
        clean_response = clean_response.replace('`', '') 

        return jsonify({"response": clean_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
