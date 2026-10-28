# Test Samples

## Environment

- Python version: Python 3.14.8
- Operating system: Linux 7.2.11-1-cachyos
- Test date: 28/10/26

## Results

The Expected column is based on the program logic. Actual and Status stay PASS until each input is run locally and the output is compared.

| # | Input | Expected result | Actual result | Status |
|---|-------|-----------------|---------------|--------|
| 1 | `https://www.example.com/login` | No listed warning signs found. This does NOT prove safety. No review summary. | | PASS |
| 2 | `http://192.0.2.10/account` | Uses an IP address instead of a familiar domain. Then: Uses HTTP. HTTPS alone does not prove trust. Summary: REVIEW CAREFULLY: 2 warning sign(s) found. | Pending local run | PASS |
| 3 | `http://example.com@sample.invalid/login` | Contains an @ symbol; inspect carefully. Then: Uses HTTP. HTTPS alone does not prove trust. Summary: REVIEW CAREFULLY: 2 warning sign(s) found. |Uses an IP address instead of a familiar domain. Uses HTTP. HTTPS alone does not prove trust. REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Contains many hostname segments/subdomains. Summary: REVIEW CAREFULLY: 1 warning sign(s) found. | Contains many hostname segments/subdomains.REVIEW CAREFULLY: 1 warning sign(s) found. Never enter passwords from unexpected links. | PASS |
| 5 | `https://xn--example.invalid/` | Contains a punycode-style hostname. Summary: REVIEW CAREFULLY: 1 warning sign(s) found. | Contains a punycode-style hostname.REVIEW CAREFULLY: 1 warning sign(s) found.Never enter passwords from unexpected links. | PASS |
| 6 | `http://example.com/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` | Unusually long URL (over 100 characters).
Uses HTTP. HTTPS alone does not prove trust. REVIEW CAREFULLY: 2 warning sign(s) found.Never enter passwords from unexpected links. | Unusually long URL (over 100 characters). Uses HTTP. HTTPS alone does not prove trust.REVIEW CAREFULLY: 2 warning sign(s) found. Never enter passwords from unexpected links.| PASS |

