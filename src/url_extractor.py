import re

def extract_urls(email_text):
    """Extracts all URLs from email text using regex."""
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(pattern, email_text)
    return urls

def extract_sender(email_text):
    """Extracts sender email address from email text."""
    pattern = r'From:.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    match = re.search(pattern, email_text)
    return match.group(1) if match else None