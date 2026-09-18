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

| Check | What it looks for | Points |
|-------|------------------|--------|
| IP address | `http://192.168.1.1/login` | +2 |
| Suspicious words | `login`, `verify`, `bank` | +2 |
| Bad domain endings | `.tk`, `.ru`, `.xyz` | +2 |
| Fake brand names | `paypa1`, `g00gle` (but not the real `google.com`) | +2 |
| URL shorteners | `bit.ly`, `t.co` | +1 |
| @ symbol | `user@evil.com/fake` | +2 |
| Too many subdomains | `a.b.c.evil.com` | +1 |

**Score result:**
```
Score 4+  → 🚨 Likely phishing
Score 3   → ⚠️  Suspicious
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
🚨 Likely phishing — Suspicious keywords found, Fake brand name detected

Enter URL: https://www.google.com
✅ Likely safe
```

---

## Test URLs

Sample URLs with their expected results are in `test_urls.txt` to try out.

---

## Requirements

- Python 3.8+
- `tldextract`

---

## License

MIT — see [LICENSE](LICENSE)
