# AI Portfolio Chatbot

An AI-powered portfolio assistant built using Ollama, Gradio, and PyPDF.

## Features

* Chat with an AI version of me
* Uses LinkedIn profile and resume as context
* Runs locally using Ollama
* Interactive Gradio interface
* PDF resume processing

## Tech Stack

* Python
* Ollama
* Llama 3.2
* Gradio
* PyPDF

## Installation

```bash
git clone <repo-url>
cd AI-Portfolio-Chatbot

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
ollama serve
ollama pull llama3.2

python app.py
```

## Architecture

Resume PDF → Context Extraction → System Prompt → Llama 3.2 → Gradio UI
