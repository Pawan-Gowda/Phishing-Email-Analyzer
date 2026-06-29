# Phishing Email Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VirusTotal](https://img.shields.io/badge/VirusTotal-394EFF?style=for-the-badge&logo=virustotal&logoColor=white)

## Overview

A Python-based modular tool that analyzes suspicious emails to detect phishing attempts by extracting URLs and checking them against VirusTotal's threat intelligence database.

## Project Structure

phishing-analyzer/

├── src/

│ ├── url_extractor.py — URL and sender extraction

│ ├── vt_checker.py — VirusTotal API integration

│ ├── domain_analyzer.py — Domain analysis

│ └── report_generator.py — Report generation

├── tests/ — Unit tests

├── docs/usage.md — Usage guide

├── main.py — Entry point

├── requirements.txt — Dependencies

└── config.example.py — API key template

## Features

- Extracts all URLs from email text automatically
- Checks each URL against 50+ antivirus engines via VirusTotal API
- Analyzes sender domain for suspicious keywords
- Generates SAFE/SUSPICIOUS/MALICIOUS verdicts
- Saves detailed scan reports as text files

## Setup

1. Install dependencies: pip install -r requirements.txt
2. Copy config.example.py to config.py and add your VirusTotal API key
3. Run: python main.py

## Skills Demonstrated

- Python scripting and modular architecture
- API integration (VirusTotal)
- Threat intelligence and phishing detection
- Email and domain analysis
- Security tool development

## Example Output
![Tool Output](docs/output.png)

## Legal Disclaimer

This tool is for educational purposes only. Use responsibly.


