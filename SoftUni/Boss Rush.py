import re

regex = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"




n = int(input())
for i in range(n):
    data = input()
    match = re.fullmatch(regex, data)
    if match:
        print(f"{match[1]}, The {match[2]}")
        print(f">> Strength: {len(match[1])}")
        print(f">> Armour: {len(match[2])}")
    else:
        print("Access denied!")