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