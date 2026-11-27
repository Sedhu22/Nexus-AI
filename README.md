# NEXUS AI — Offline Intelligent Desktop Assistant

NEXUS AI is a Python-based desktop assistant powered by local Large Language Models (LLMs). It provides AI chat, document summarization, desktop automation, and system monitoring through a simple graphical interface.

## Features

- **Offline AI Chat:** Interact with a locally running Phi-3 Mini model using Ollama.
- **Document Analysis:** Extract and summarize content from PDF and TXT files.
- **Desktop Automation:** Take screenshots and open the web browser.
- **System Monitoring:** View CPU and RAM usage.
- **Modern Interface:** Dark-themed desktop dashboard built with CustomTkinter.

## Tech Stack

- Python
- Ollama
- Phi-3 Mini
- CustomTkinter
- PyMuPDF
- PyAutoGUI
- Psutil
- BeautifulSoup

## Project Structure

```text
Nexus-AI/
├── core/
│   ├── ai.py
│   ├── automation.py
│   └── documents.py
├── ui/
│   └── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sedhu22/Nexus-AI.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Nexus-AI
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Install Ollama and download the model:

   ```bash
   ollama pull phi3:mini
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Requirements

- Python 3.10 or later
- Ollama
- Phi-3 Mini model
- Windows, macOS, or Linux (some automation features may vary by operating system)

## Contributors

Developed collaboratively by **Sedhu Madhavan** and **Santina V**.

## Project Status

Core features implemented and tested locally. Further improvements and enhancements are ongoing.
