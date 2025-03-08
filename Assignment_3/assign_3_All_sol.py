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

'''
2. Check if a String is a Valid Phone Number
Problem Statement: Write a function to check whether a given string is a valid phone number in the format (XXX) XXX-XXXX.
Hint:
Input Example:
phone = "(123) 456-7890"
Output Example:
True
Input Example:
phone = "123-456-7890"
Output Example:
False
'''

import re 

phone1 = "(123) 456-7890"
phone2 = "123-456-7890"
logic = r"\(\d{3}\) \d{3}-\d{4}"
match1 = bool(re.match(logic,phone1))
match2 = bool(re.match(logic,phone1))
print(match1,match2)


'''
3. Count the Number of Words in a String
Problem Statement: Write a function that counts the number of words in a given string. Words are defined as sequences of alphanumeric characters separated by spaces or punctuation.
Hint:
Input Example:
text = "Hello, my name is John Doe."
Output Example:
5
'''

import re 

text = "Hello, my name is John Doe."

logic = r"[\w+]+.[\s]"

match = re.findall(logic,text)
print(len(match))


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

'''5. Extract Dates from a String
Problem Statement: Write a function to extract all dates in the format MM-DD-YYYY from a given string.
Hint:
Input Example:
text = "My birthday is on 12-10-1995 and my friend's birthday is 01-20-1990."
Output Example:
['12-10-1995', '01-20-1990']
'''

import re

text = "My birthday is on 12-10-1995 and my friend's birthday is 01-20-1990."
logic = r"\b\d{2}-\d{2}-\d{4}\b"
match = re.findall(logic,text)
print(match)

'''
6. Replace All Whitespace with a Single Space
Problem Statement: Write a function that replaces all consecutive whitespace characters (spaces, tabs, newlines) in a string with a single space.
Hint:
•	Use  to match one or more whitespace characters and replace them with a single space.
Input Example:
text = "This    is    a   test  string.     "
Output Example:
"This is a test string."
'''
import re 

text = "This    is    a   test  string.     "
logic = r"\s+"
replace = re.sub(logic,' ',text)
print(replace)

'''
7. Extract All Hashtags from a Text
Problem Statement: Write a function to extract all hashtags (words starting with #) from a given string.
Hint:
•	Use the regular expression  to match hashtags.
Input Example:
text = "Loving the weather today! #sunny #goodvibes #relax"
Output Example:
['#sunny', '#goodvibes', '#relax']
'''

import re
text = "Loving the weather today! #sunny #goodvibes #relax"

logic = r"#\w+"
match  = re.findall(logic,text)
print(match)

'''8. Validate a Strong Password
Problem Statement: Write a function to validate a password. A strong password must meet the following criteria:
•	Be at least 8 characters long.
•	Contain both uppercase and lowercase letters.
•	Contain at least one digit.
•	Contain at least one special character (e.g., @, #, $).
Hint:

Input Example:
password = "Strong@123"
Output Example:
True
Input Example:
python
Copy
password = "weakpass"
Output Example:
False
'''
import re 

password1 = "Strong@123"
password2 = "weakpass"
logic = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"
match1 = bool(re.match(logic,password1))
match2 = bool(re.match(logic,password2))
print(match1,match2)

'''9. Find All IP Addresses in a String
Problem Statement: Write a function to extract all valid IPv4 addresses from a given string. An IPv4 address has the form X.X.X.X, where X is a number between 0 and 255.
Hint:
•	Use the pattern  to match IP addresses and validate that each part is between 0 and 255.

Input Example:
text = "The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."
Output Example:
['192.168.0.1', '10.0.0.255']
'''
import re
text = "The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."

#logic = r"(?:\d{1,3}<256\.){3}\d{1,3}"
logic = r"\b(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\b"

match = re.findall(logic,text)
print(match)

'''
10. Validate a Date in DD-MM-YYYY Format
Problem Statement: Write a function to validate if a given string represents a valid date in the format DD-MM-YYYY.
Hint:
•	Use the regular expression to match the format, then use Python’s datetime module to validate the actual date.
Input Example:
date = "15-04-2023"
Output Example:
True
Input Example:
date = "31-02-2023"
Output Example:
False

'''

import re 
logic = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
date1 = "15-04-2023"
date2 = "31-02-2023"
match1 = bool(re.match(logic,date1))
match2 = bool(re.match(logic,date2))
print(match1,match2)