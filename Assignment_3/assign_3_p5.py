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