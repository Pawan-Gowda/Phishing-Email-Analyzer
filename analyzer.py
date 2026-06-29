import requests
import re

<<<<<<< HEAD
# Your VirusTotal API key
API_KEY = "e13c6ddf38a48f5dee14b8d745d7a7aebba461c470893d511e898d833fb39fdf"

# Function to extract URLs from email text
=======
API_KEY = "API key"

>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
def extract_urls(email_text):
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(pattern, email_text)
    return urls

<<<<<<< HEAD
# Function to check a URL against VirusTotal
=======
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
def check_url(url):
    api_url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(api_url, headers=headers, data=f"url={url}")
    response_json = response.json()
    if "data" not in response_json:
        print(f"API Error: {response_json}")
        return None
    scan_id = response_json["data"]["id"]
    result_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
    result = requests.get(result_url, headers=headers)
    return result.json()

<<<<<<< HEAD
# Function to generate a threat report
=======
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
def generate_report(url, result):
    if result is None:
        print("Could not get results for this URL.")
        return
    stats = result["data"]["attributes"]["stats"]
    malicious = stats["malicious"]
    suspicious = stats["suspicious"]
    harmless = stats["harmless"]
    print("\n" + "="*50)
    print(f"URL: {url}")
    print(f"Malicious engines: {malicious}")
    print(f"Suspicious engines: {suspicious}")
    print(f"Harmless engines:  {harmless}")
    if malicious > 0:
        print("VERDICT: ⚠️  MALICIOUS - Do not click this URL!")
    elif suspicious > 0:
        print("VERDICT: ⚠️  SUSPICIOUS - Treat with caution!")
    else:
        print("VERDICT: ✅ SAFE")
    print("="*50)

<<<<<<< HEAD
# Function to analyze sender email address
=======
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
def analyze_sender(email_address):
    print("\n" + "="*50)
    print(f"SENDER ANALYSIS: {email_address}")
    
<<<<<<< HEAD
    # Extract domain from email
    domain = email_address.split("@")[-1]
    
    # List of suspicious patterns
=======
    domain = email_address.split("@")[-1]

>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
    suspicious_patterns = ["secure", "verify", "account", "update", "login", "bank", "support"]
    
    flagged = [word for word in suspicious_patterns if word in domain.lower()]
    
    if flagged:
        print(f"⚠️  SUSPICIOUS DOMAIN - Contains keywords: {flagged}")
    else:
        print(f"✅ Domain looks normal: {domain}")
    print("="*50)

<<<<<<< HEAD
# Main function
=======
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
def main():
    print("="*50)
    print("   PHISHING EMAIL ANALYZER")
    print("="*50)
    
<<<<<<< HEAD
    # Analyze the sender
=======
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
    analyze_sender("support@secure-bank-verify.com")
    
    email_text = """
    Dear user, your account has been compromised.
    Please verify your identity here: http://suspicious-link.com
    Or visit our support page: http://google.com
    """
    print("\nExtracting URLs from email...")
    urls = extract_urls(email_text)
    if not urls:
        print("No URLs found in email.")
        return
    print(f"Found {len(urls)} URL(s). Checking with VirusTotal...")
    for url in urls:
        result = check_url(url)
        generate_report(url, result)

<<<<<<< HEAD
main()
=======
main()
>>>>>>> f24a5b271f7516ff1cb8e55d07747608bf6d469e
