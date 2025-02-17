websites = (
    "http://google.com",
    "yahoo.com",
    "bing.com",
    "duckduckgo.com",
    "https://facebook.com",
    "twitter.com",
    "instagram.com",
    "reddit.com"
)

# for website in websites:
#     if (website.startswith("https://") == False):
#         print(website + " " + str(website.startswith("https://")))
#         website = "https://" + website

for website in websites:
    if not website.startswith("https://"):
        # website = "https://" + website
        website = f"https://{website}"
    print(website)
