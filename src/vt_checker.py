import requests

def check_url(url, api_key):
    """Sends URL to VirusTotal and returns analysis results."""
    api_url = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(api_url, headers=headers, data=f"url={url}")
    response_json = response.json()
    if "data" not in response_json:
        return None
    scan_id = response_json["data"]["id"]
    result_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
    result = requests.get(result_url, headers=headers)
    return result.json()