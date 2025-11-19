from flask import Flask, request, render_template
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
    return chain.invoke({"text": text})   # ← fixed here

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form["text"]
        result = analyze(user_input)
    return render_template("index.html", result=result, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)