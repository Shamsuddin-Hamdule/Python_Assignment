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