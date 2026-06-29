from datetime import datetime

def generate_report(url, vt_result, domain_result):
    """Generates a threat verdict for a single URL."""
    report = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "domain_analysis": domain_result,
        "vt_analysis": None,
        "verdict": "UNKNOWN"
    }

    if vt_result:
        stats = vt_result.get("data", {}).get("attributes", {}).get("stats", {})
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        harmless = stats.get("harmless", 0)

        report["vt_analysis"] = {
            "malicious": malicious,
            "suspicious": suspicious,
            "harmless": harmless
        }

        if malicious > 0:
            report["verdict"] = "MALICIOUS"
        elif suspicious > 0 or domain_result.get("flagged"):
            report["verdict"] = "SUSPICIOUS"
        else:
            report["verdict"] = "SAFE"

    return report

def save_report(reports, filename=None):
    """Saves all reports to a text file."""
    if not filename:
        filename = f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("       PHISHING EMAIL ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")

        for report in reports:
            f.write(f"URL: {report['url']}\n")
            f.write(f"Time: {report['timestamp']}\n")
            f.write(f"Verdict: {report['verdict']}\n")

            if report["domain_analysis"]["flagged"]:
                f.write(f"Suspicious domain keywords: {report['domain_analysis']['keywords']}\n")

            if report["vt_analysis"]:
                f.write(f"Malicious engines: {report['vt_analysis']['malicious']}\n")
                f.write(f"Suspicious engines: {report['vt_analysis']['suspicious']}\n")
                f.write(f"Harmless engines: {report['vt_analysis']['harmless']}\n")

            f.write("-" * 40 + "\n")

    return filename