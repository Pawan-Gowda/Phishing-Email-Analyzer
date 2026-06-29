def analyze_domain(email_address):
    """Analyzes sender domain for suspicious keywords."""
    suspicious_keywords = [
        "secure", "verify", "account", "update", 
        "login", "bank", "support", "confirm",
        "urgent", "alert", "suspended", "unusual"
    ]
    
    if not email_address:
        return {"domain": None, "flagged": False, "keywords": []}
    
    domain = email_address.split("@")[-1].lower()
    flagged_keywords = [kw for kw in suspicious_keywords if kw in domain]
    
    return {
        "domain": domain,
        "flagged": len(flagged_keywords) > 0,
        "keywords": flagged_keywords
    }