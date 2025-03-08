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
