from urllib.request import urlopen

with urlopen("http://example.com") as response:
    print(response.read().decode("utf-8"))

