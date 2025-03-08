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