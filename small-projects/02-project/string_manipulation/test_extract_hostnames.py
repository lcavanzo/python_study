import pytest
from extract_hostnames import extract_hostname


@pytest.mark.parametrize(
    "url, expected_url",
    [
        ("https://www.example.com", "example.com"),
        ("http://sub.domain.org", "sub.domain.org"),
        ("another-site.net", "another-site.net"),
        ("http://google.com?test1", "google.com"),
        ("http://google.com/test1", "google.com"),
        ("https://www.example.com/path/to/resource", "example.com"),
        ("www.anothersite.org", "anothersite.org"),
        ("http://api.service.net/data?id=123&type=json", "api.service.net"),
        ("This is not a url string", None),
        ("ftp://invalid..domain/file.txt", None),
        ("local-host", None),
    ],
)
def test_extract_hostnames(url, expected_url):
    assert extract_hostname(url) == expected_url
