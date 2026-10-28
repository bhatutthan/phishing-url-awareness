"""EWB Phishing URL Awareness Checker. It only reads URL text."""
import re
from urllib.parse import urlparse

INFO_MESSAGES = ("No URL entered", "Could not identify", "No listed warning")


def inspect_url(raw_url):
    """Return a list of findings for one URL string, without opening it."""
    url = raw_url.strip()
    if url == "":
        return ["No URL entered."]

    if "://" in url:
        candidate = url
    else:
        candidate = "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()
    if host == "":
        return ["Could not identify a hostname."]

    findings = []

    # Everything before the @ is only login info, so it can pretend to be a trusted site.
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if len(findings) == 0:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    first = findings[0]
    if first.startswith(INFO_MESSAGES):
        return False
    # The malformed-input message is information too, not a warning sign.
    if first.startswith("This text is not"):
        return False
    return True


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        text = input("\nEnter a sample URL (or type q to quit):")

        if text.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(text)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()