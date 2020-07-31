import re

regex = r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$"
n = int(input())
for i in range(n):
    data = input()
    match = re.fullmatch(regex, data)

    if match:
        sad = match[2] + match[3] + match[4] + match[5]
        print(f"Password: {sad}")
    else:
        print("Try another password!")
# Try Input	
# 3
# ##>00|no|NO|!!!?<###
# ##>123|yes|YES|!!!<##
# $$<111|noo|NOPE|<<>$$	Try another password!
# Password: 123yesYES!!!
# Try another password!