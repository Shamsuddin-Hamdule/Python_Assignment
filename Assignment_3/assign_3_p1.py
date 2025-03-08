'''1. Extract All Email Addresses from a String
Problem Statement: Write a function that extracts all email addresses from a given string.
Hint:
•	Use regular expressions to identify patterns that start with alphanumeric characters, followed by @, then a domain name with a period, and finally a valid domain extension.
Input Example:
text = "Contact john.doe@example.com, jane_doe123@domain.org for more details."
Output Example:
['john.doe@example.com', 'jane_doe123@domain.org']
'''

import re

text = "Contact john.doe@example.com, jane_doe123@domain.org for more details."

logic = r"[\w]+.[\w]+@[\w]+.[\w][\w][\w]"
match = re.findall(logic,text)
print(match)