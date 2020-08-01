spellbook = {}


while True:
    data = input().split()

    if data[0] == "End":
        break
    command = data[0]
    hero_name = data[1]

    if command == "Enroll":
        if hero_name in spellbook:
            print(f"{hero_name} is already enrolled.")

        spellbook[hero_name] = []
    elif command == "Learn":
        spell = data[2]


        if hero_name not in spellbook:
            print(f"{hero_name} doesn't exist.")
            continue

        if spell in spellbook[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
            continue
        spellbook[hero_name].append(spell)

    elif command == "Unlearn":
        spell = data[2]

        if hero_name not in spellbook:
            print(f"{hero_name} doesn't exist.")
            continue

        if spell not in spellbook[hero_name]:
            print(f"{hero_name} doesn't know {spell}.")
            continue

        spellbook[hero_name].remove(spell)
spellbook = dict(sorted(spellbook.items(), key=lambda u: (-len(u[1]), u[0])))

print("Heroes:")
for name, spells in spellbook.items():
    print(f"== {name}: {', '.join(spells)}")
# Input
#
# Enroll Stefan
# Enroll Pesho
# Enroll Stefan
# Learn Stefan ItShouldWork
# Learn Stamat ItShouldNotWork
# Unlearn Gosho Dispel
# Unlearn Stefan ItShouldWork


# Output

# Stefan is already enrolled.
# Stamat doesn't exist.
# Gosho doesn't exist.
# Heroes:
# == Pesho: 
# == Stefan:

