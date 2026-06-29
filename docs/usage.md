# Phishing Email Analyzer — Usage Guide

## Installation

1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Copy config.example.py to config.py and add your VirusTotal API key: cp config.example.py config.py

## Usage

Run the analyzer: python main.py

## How It Works

1. Paste suspicious email text into the email_text variable in main.py
2. The tool extracts all URLs automatically
3. Each URL is checked against 50+ antivirus engines via VirusTotal API
4. Sender domain is analyzed for suspicious keywords
5. A report is generated with SAFE/SUSPICIOUS/MALICIOUS verdicts

## Project Structure

phishing-analyzer/

├── src/

│ ├── url_extractor.py — URL and sender extraction

│ ├── vt_checker.py — VirusTotal API integration

│ ├── domain_analyzer.py — Domain suspicious keyword analysis

│ └── report_generator.py — Report generation and saving

├── tests/ — Unit tests

├── docs/ — Documentation

├── main.py — Entry point

├── requirements.txt — Dependencies

├── config.example.py — API key template

└── .gitignore — Git ignore rules

## Requirements

- Python 3.x
- VirusTotal API key (free at virustotal.com)
