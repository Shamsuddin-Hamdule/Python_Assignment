'''
4. Validate a URL
Problem Statement: Write a function to validate if a given URL is in the format http:// or https:// followed by a valid domain name and an optional path.
Hint:
•	A URL pattern can be described as https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?.
Input Example:
url = "https://www.example.com/path/to/page"
Output Example:
True
Input Example:
url = "ftp://example.com"
Output Example:
False
'''
import re

url1 = "https://www.example.com/path/to/page"
url2 = "ftp://example.com"


logic = r"https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?."
match1 = bool(re.match(logic,url1))
match2 = bool(re.match(logic,url2))
print(match1,match2)