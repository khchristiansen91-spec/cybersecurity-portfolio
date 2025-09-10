# Security Headers Scanner

This project contains a simple command-line tool that scans web servers for common HTTP security headers and reports their presence or absence. The goal is to teach how to automate security header checks and highlight insecure configurations.

## Features

- Accepts a single URL or a list of URLs from a text file.
- Sends HTTP GET requests and captures response headers using Python's `requests` library.
- Checks for important security headers such as:
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection
  - Referrer-Policy and Permissions-Policy
- Produces a simple report listing which headers are present, missing, or misconfigured.
- Outputs results to the console; future versions could generate a CSV or HTML report.

## Usage

1. Install dependencies from `requirements.txt` (e.g., `pip install -r requirements.txt`).
2. Run `python scanner.py --url https://example.com` to scan a single site.
3. Or run `python scanner.py --file urls.txt` to scan multiple sites listed in `urls.txt`.
4. Review the console output to see which security headers each site has or lacks.

## Disclaimer

This scanner is for educational and testing purposes. Always obtain permission before scanning or assessing systems you do not own. The script is intentionally lightweight and does not account for all possible security headers or complex configurations.
