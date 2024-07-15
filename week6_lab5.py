import re

# Input IP address
ip_address = input("Enter an IPv4 address: ")

pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

match = re.search(pattern, ip_address)

if match:
    print(ip_address," is a valid IP address.")
else:
    print(ip_address,"is not a valid IP address.")
