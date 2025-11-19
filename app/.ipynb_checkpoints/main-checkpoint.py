from flask import Flask, request, jsonify, render_template
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)
llm = OllamaLLM(model="llama3.1:8b", temperature=0.0)

def analyze(text):
    template = """You are an expert in sentiment analysis and logical reasoning.

Statement: "{text}"

Step by step:
1. Detect the overall sentiment: Positive, Negative, Neutral, or Mixed.
2. Quote the exact words/phrases that led you to this conclusion.
3. Explain your reasoning clearly in 2–4 sentences.
4. Rate confidence from 1–10.

Respond in this exact format:
Sentiment: [your answer]
Evidence: [quoted phrases]
Reasoning: [your explanation]
Confidence: [1–10]"""

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"text": text})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json(force=True)
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    raw = analyze(data["text"])
    lines = [line.split(": ", 1) for line in raw.split("\n") if ": " in line]
    result = {k.strip().lower(): v.strip() for k, v in lines}
    return jsonify(result)

if __name__ == "__main__":
    # gunicorn finds the 'app' variable automatically
    app.run(host="0.0.0.0", port=5000)
