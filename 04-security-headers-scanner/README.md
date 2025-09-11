# Security Headers Scanner

This command-line tool scans one or more websites to check for the presence of critical HTTP security headers. It's a straightforward way to highlight misconfigured or missing headers and to practice automating security assessments.

## Features

- **Multiple targets:** Accept a single URL or a list of URLs via command-line arguments.
- **Concurrent scanning:** Use a thread pool to scan multiple sites in parallel for faster results.
- **Checks essential headers:** Content-Security-Policy (CSP), Strict-Transport-Security (HSTS), X-Content-Type-Options, X-Frame-Options, Referrer-Policy and Permissions-Policy.
- **Clear output:** Prints each target's HTTP status and the value of each header (or `MISSING` if not set).

## Usage

1. Install dependencies (Python 3):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the scanner against one or more HTTPS sites:

   ```bash
   python scanner.py https://example.com https://another-site.org
   ```

   Use the `-t` flag to adjust the number of concurrent threads (default 5):

   ```bash
   python scanner.py -t 10 https://example.com https://another-site.org
   ```

3. Example output:

   ```
   GET https://example.com -> 200
   Content-Security-Policy: default-src 'self'
   Strict-Transport-Security: max-age=63072000; includeSubDomains
   X-Content-Type-Options: nosniff
   X-Frame-Options: SAMEORIGIN
   Referrer-Policy: no-referrer
   Permissions-Policy: MISSING
   ```

## Extending the tool

This scanner is deliberately simple. You can extend it by:

- Adding checks for additional headers (e.g. Cache-Control or X-XSS-Protection).
- Saving results to a CSV or JSON file instead of printing them.
- Integrating it into a continuous integration pipeline to catch misconfigurations during development.

---

*This project is for educational and ethical testing purposes. Only scan sites you own or are authorized to test.*
