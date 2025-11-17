from google import genai
from flask import Flask, render_template, request

app = Flask(__name__)

# Your NEW API key
API_KEY = "AIzaSyDzJa9W5oBPCL3P5iDl-S25zS-_xR4ZlsM"

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.0-flash-exp"   # Latest model (2025)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=user_input
            )

            return render_template(
                "index.html",
                user_input=user_input,
                response=response.text
            )
        except Exception as e:
            return render_template(
                "index.html",
                error="Error: " + str(e)
            )

    return render_template("index.html", response=None)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
