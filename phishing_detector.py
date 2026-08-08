# Phishing URL Detector
# Checks if a URL looks suspicious or safe

import re
import tldextract
from urllib.parse import urlparse

def detect_phishing(url):
    # Add https if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Validate URL
    try:
        parsed = urlparse(url)
        if not parsed.netloc:
            return "❌ Invalid URL"
    except:
        return "❌ Invalid URL"

    extracted = tldextract.extract(url)
    domain    = f"{extracted.domain}.{extracted.suffix}"
    subdomain = extracted.subdomain
    score     = 0
    reasons   = []

    # 1. IP address used instead of domain
    if re.match(r'^https?://(\d{1,3}\.){3}\d{1,3}', url):
        score += 2
        reasons.append("IP address used instead of domain")

    # 2. Too many subdomains
    if subdomain and subdomain.count('.') >= 2:
        score += 1
        reasons.append("Too many subdomains")

    # 3. Suspicious words in URL
    bad_words = ['login', 'verify', 'update', 'secure', 'account', 'confirm', 'bank', 'signin']
    if any(word in url.lower() for word in bad_words):
        score += 2
        reasons.append("Suspicious keywords found")

    # 4. Suspicious domain endings
    bad_tlds = ['.tk', '.ga', '.ml', '.cf', '.gq', '.ru', '.xyz', '.top']
    if any(url.lower().endswith(tld) or f".{extracted.suffix}" == tld for tld in bad_tlds):
        score += 2
        reasons.append(f"Suspicious domain ending: .{extracted.suffix}")

    # 5. Fake brand names (typosquatting)
    fake_brands = [r'paypa[1l]', r'faceb[0o]0k', r'g[0o][0o]gle', r'micros[0o]ft', r'amaz[0o]n']
    if any(re.search(pattern, url.lower()) for pattern in fake_brands):
        score += 2
        reasons.append("Fake brand name detected")

    # 6. URL shortener
    shorteners = ['bit.ly', 'tinyurl', 't.co', 'ow.ly']
    if any(s in domain for s in shorteners):
        score += 1
        reasons.append("URL shortener detected")

    # 7. @ symbol in URL
    if '@' in parsed.netloc:
        score += 2
        reasons.append("@ symbol found in URL")

    # Result
    if score >= 5:
        return f"🚨 Likely phishing — {', '.join(reasons)}"
    elif score >= 3:
        return f"⚠️  Suspicious — {', '.join(reasons)}"
    else:
        return "✅ Likely safe"


# --- Try it out ---
if __name__ == "__main__":
    print("Phishing URL Detector")
    print("Type 'quit' to exit\n")

    while True:
        url = input("Enter URL: ").strip()
        if url.lower() in ['quit', 'exit', 'q']:
            print("Stay safe online!")
            break
        if url:
            print(detect_phishing(url), "\n")
