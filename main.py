from src.url_extractor import extract_urls, extract_sender
from src.vt_checker import check_url
from src.domain_analyzer import analyze_domain
from src.report_generator import generate_report, save_report

# Your VirusTotal API key
from config import VIRUSTOTAL_API_KEY

def main():
    print("=" * 60)
    print("       PHISHING EMAIL ANALYZER")
    print("=" * 60)

    email_text = """
    Dear user, your account has been compromised.
    Please verify your identity here: http://suspicious-link.com
    Or visit our support page: http://google.com
    """

    print("\n[*] Extracting URLs...")
    urls = extract_urls(email_text)
    sender = extract_sender(email_text)

    if not urls:
        print("[-] No URLs found.")
        return

    print(f"[+] Found {len(urls)} URL(s)")
    print(f"[*] Checking with VirusTotal...")

    reports = []
    for url in urls:
        vt_result = check_url(url, VIRUSTOTAL_API_KEY)
        domain_result = analyze_domain(sender)
        report = generate_report(url, vt_result, domain_result)
        reports.append(report)
        print(f"[{'!' if report['verdict'] != 'SAFE' else '+'}] {url} — {report['verdict']}")

    filename = save_report(reports)
    print(f"\n[+] Report saved: {filename}")

main()