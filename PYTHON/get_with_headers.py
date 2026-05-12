from urllib.request import Request, urlopen

url = "https://example.com"
req = Request(url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    },
)

with urlopen(req, timeout=20) as response:
    html = response.read().decode("utf-8")
    print(html)

