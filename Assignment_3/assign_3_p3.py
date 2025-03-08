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
