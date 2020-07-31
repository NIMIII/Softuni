party = {}
unliked_meal = 0
while True:
    args = input().split("-")
    if args[0] == "Stop":
        break

    command = args[0]
    guest = args[1]
    meal = args[2]

    if command == "Like":

        if guest not in party:
            party[guest] = []

        if meal in party[guest]:
            continue
        party[guest].append(meal)



    elif command == "Unlike":
        if guest not in party:
            print(f"{guest} is not at the party.")
            continue

        if meal not in party[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            continue

        party[guest].remove(meal)
        print(f"{guest} doesn't like the {meal}.")
        unliked_meal += 1

party = dict(sorted(party.items(),key=lambda u: (-len(u[1]),u[0])))

for guest, meals in party.items():
    print(f"{guest}: {', '.join(party[guest])}")

print(f"Unliked meals: {unliked_meal}")

# Input
# Like-Krisi-shrimps
# Like-Krisi-soup
# Like-Misho-salad
# Like-Pena-dessert
# Stop

# Output
# Krisi: shrimps, soup
# Misho: salad
# Pena: dessert
# Unliked meals: 0

# Input
# Like-Krisi-shrimps
# Unlike-Vili-carp
# Unlike-Krisi-salad
# Unlike-Krisi-shrimps
# Stop

# Output
# Vili is not at the party.
# Krisi doesn't have the salad in his/her collection.
# Krisi doesn't like the shrimps.
# Krisi:
# Unliked meals: 1
