import re

regex = r'(U\$)(?P<username>[A-Z][a-z]{2,})\1(P@\$)(?P<password>[a-z]{5,}[0-9]+)\3'


n = int(input())
count = 0
for i in range(n):
    data = input()

    match = re.fullmatch(regex, data)
    if match:
        count += 1
        print("Registration was successful")
        print(f"Username: {match['username']}, Password: {match['password']}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {count}")
# Input

# 3
# U$MichaelU$P@$asdqwe123P@$
# U$NameU$P@$PasswordP@$
# U$UserU$P@$ad2P@$

# Output
# 3
# U$MichaelU$P@$asdqwe123P@$
# U$NameU$P@$PasswordP@$
# U$UserU$P@$ad2P@$	Registration was successful
# Username: Michael, Password: asdqwe123
# Invalid username or password
# Invalid username or password
# Successful registrations: 1

