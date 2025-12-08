"""
Write a Python function extract_hostname(url) that takes a URL string and uses regular expressions to extract only the hostname.

The hostname should not include http://, https://, www., or any path/query parameters.

Then, write unit tests for your extract_hostname function using assert statements to cover:

    At least 3 valid URL formats (e.g., with/without protocol, with/without www, with/without path).
    At least 2 invalid URL formats (e.g., not a URL, malformed).

Example Valid URL and Expected Hostname:

    https://www.example.com/path?query=1 -> example.com
    http://sub.domain.org -> sub.domain.org
    another-site.net -> another-site.net

Hint: Consider using re.sub() to clean the string before extracting, or a single complex regex. For testing, define a list of (input, expected_output) tuples.
"""

import re


def extract_hostname(url):
    """
    Extracts the hostname from a URL string using regular expressions.
    The hostname should not include http://, https://://, www., or any path/query parameters.
    Returns the hostname string if valid, otherwise None.
    """
    hostname_pattern = re.compile(
        r"^(?:https?://)?"  # Optional protocol (http:// or https://)
        r"(?:www\.)?"  # Optional www.
        r"([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}|"  # Covers sub.domain.com, domain.co.uk (at least two dots for full domain)
        r"[a-zA-Z0-9-]+\.[a-zA-Z]{2,})"  # Covers simple domain.com (single dot for domain.tld)
        r"(?:[:/].*|\?.*)?$"  # Optional port, path, or query string
    )

    match = hostname_pattern.search(url)
    if match:
        return match.group(1)
    return None


if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "http://sub.domain.org",
        "another-site.net",
        "http://google.com?test1",
        "http://google.com/test1",
        "https://www.example.com/path/to/resource",
        "www.anothersite.org",
        "http://api.service.net/data?id=123&type=json",
        "This is not a url string",
        "ftp://invalid..domain/file.txt",
        "local-host",  # -> None (no TLD)
    ]
    for url in urls:
        print(extract_hostname(url))
