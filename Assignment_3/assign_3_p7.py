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