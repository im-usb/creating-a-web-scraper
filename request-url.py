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


# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = requests.get(website)
#     # print(response.status_code)
#     if response.status_code >= 500:
#         status[website] = "Server error responses"
#     elif response.status_code >= 400:
#         status[website] = "Client error responses"
#     elif response.status_code >= 300:
#         status[website] = "Redirection responses"
#     elif response.status_code >= 200:
#         status[website] = "Successful responses"
#     elif response.status_code >= 100:
#         status[website] = "Informational responses"

# print(status)
