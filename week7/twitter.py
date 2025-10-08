

import re

url = input("URL: ").strip()


username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)


print (f"Username: {username}")






"""
username = url.removeprefix("https://twitter.com/")

print (f"Username: {username}")
"""
