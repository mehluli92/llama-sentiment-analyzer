**Local Sentiment + Reasoning Analyzer**

A fully offline web application that analyzes the sentiment of any statement and explains its reasoning using Llama 3.1 8B running locally via Ollama on Apple Silicon.

**Features**
- 100% local – no data leaves your machine
- Runs completely offline after initial model download
- Real-time sentiment detection with detailed evidence and confidence scoring
- Powered by Llama 3.1 8B on Metal (Apple M2/M3)
- Simple Flask web interface

**Requirements**
- macOS with Apple Silicon (M1/M2/M3/M4)
- Ollama installed and running
- Python 3.9+

**Quick Start**
1. Clone this repository
2. Create and activate virtual environment:
   python3 -m venv venv && source venv/bin/activate
3. Install dependencies:
   pip install flask langchain-ollama
4. Start Ollama (open the Ollama app or run `ollama serve`)
5. Run the web app:
   python app/main.py
6. Open http://127.0.0.1:5000 in your browser

**Model**
Uses llama3.1:8b (downloaded automatically by Ollama on first use)

**Project Structure**
- app/main.py – Flask application
- app/templates/index.html – Web interface
- notebooks/ – Optional Jupyter notebooks for experimentation
