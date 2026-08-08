# Phishing URL Detector 🛡️

A simple Python tool that checks if a URL looks safe or suspicious.

> ⚠️ For learning only. Not a replacement for real security tools.

---

## What's Inside

```
phishing-url-detector/
│
├── phishing_detector.py
├── test_urls.txt
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## How It Works

It checks the URL for suspicious signs and gives a score.

| Check | What it looks for |
|-------|------------------|
| IP address | `http://192.168.1.1/login` |
| Suspicious words | `login`, `verify`, `bank` |
| Bad domain endings | `.tk`, `.ru`, `.xyz` |
| Fake brand names | `paypa1`, `g00gle` |
| URL shorteners | `bit.ly`, `tinyurl` |
| @ symbol | `user@evil.com/fake` |
| Too many subdomains | `a.b.c.evil.com` |

**Score result:**
```
Score 5+  → 🚨 Likely phishing
Score 3-4 → ⚠️  Suspicious
Score 0-2 → ✅ Likely safe
```

---

## Setup

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python phishing_detector.py
```

```
Enter URL: https://paypa1.com/verify/account
🚨 Likely phishing — Fake brand name, Suspicious keywords found

Enter URL: https://www.google.com
✅ Likely safe
```

---

## Test URLs

Sample URLs are in `test_urls.txt` to try out.

---

## Requirements

- Python 3.6+
- `tldextract`

---

## License

MIT — see [LICENSE](LICENSE)
