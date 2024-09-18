from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the LLM (you can change the model as per your need)
model = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    response = model(prompt, max_length=50, num_return_sequences=1)
    return {"response": response[0]["generated_text"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
