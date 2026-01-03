def normalize_url(url):
    url = url.lower().strip()

    if url.startswith("https://"):
        url = url[8:]
    elif url.startswith("http://"):
        url = url[7:]

    while url.endswith("/"):
        url = url[:-1]

    return url

user_input = input("Please input a URL: ")
print(normalize_url(user_input))
