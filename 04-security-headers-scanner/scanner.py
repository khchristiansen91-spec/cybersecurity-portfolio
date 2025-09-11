import argparse
import sys
import requests
import concurrent.futures

# List of security headers to check
REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check_headers(url: str) -> str:
    """
    Perform an HTTP GET request to the given URL and check for the presence of
    common security headers. Returns a formatted string summarizing the results.
    """
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        lines = [f"Results for {url} (status {response.status_code})"]
        for header in REQUIRED_HEADERS:
            value = response.headers.get(header)
            lines.append(f"{header}: {value if value else 'MISSING'}")
        return "\n".join(lines)
    except Exception as e:
        return f"{url} -> ERROR: {e}"

def main():
    parser = argparse.ArgumentParser(description="Scan one or more URLs for common HTTP security headers.")
    parser.add_argument("targets", nargs="+", help="One or more URLs (e.g., https://example.com)")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of concurrent threads")
    args = parser.parse_args()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        for result in executor.map(check_headers, args.targets):
            print(result)
            print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python scanner.py <url1> [url2 ...]")
        sys.exit(1)
    main()
