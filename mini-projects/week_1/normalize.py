
#https://Google.com/search/
url = str(input("Please input a URL: "))
url = url.lower()
url = url.strip()

if url.startswith("https://"):
    new = url[8:]
elif url.startswith("http://"):
    new = url[7:]

if new.endswith("/"):
    final = new[:-1]
print(final)

