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

