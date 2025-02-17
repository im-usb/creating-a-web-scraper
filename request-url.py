import requests

websites = (
    "https://google.com",
    "yahoo.com",
    "bing.com",
    "duckduckgo.com",
    "https://facebook.com",
    "twitter.com",
    "instagram.com",
    "reddit.com"
)

status = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = requests.get(website)
    # print(response.status_code)
    if response.status_code == 200:
        status[website] = response.status_code
    else:
        status[website] = response.status_code

print(status)
