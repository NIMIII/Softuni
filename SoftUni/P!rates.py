people = {}
gold = {}
while True:
    token = input().split("||")
    if token[0] == "Sail":
        break
    city = token[0]
    population = int(token[1])
    money = int(token[2])


    if city in people:
        people[city] += population
        gold[city] += money
    else:
        people[city] = population
        gold[city] = money

while True:
    token = input().split("=>")
    if token[0] == "End":
        break

    command = token[0]
    town = token[1]

    if command == "Plunder":
        population = int(token[2])
        money = int(token[3])


        people[town] -= population
        gold[town] -= money
        print(f"{town} plundered! {money} gold stolen, {population} citizens killed.")
        if people[town] <= 0 or gold[town] <= 0:
            print(f"{town} has been wiped off the map!")
            people.pop(town)
            gold.pop(town)
            continue


    elif command == "Prosper":
        money = int(token[2])

        if money < 0:
            print("Gold added cannot be a negative number!")
        else:
            gold[town] += money
            print(f"{money} gold added to the city treasury. {town} now has {gold[town]} gold.")

gold = dict(sorted(gold.items(), key=lambda u : (-u[1], u[0])))

count = len(gold)
if count > 0:
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
for names, gold in gold.items():
    humans = people[names]
    print(f"{names} -> Population: {humans} citizens, Gold: {gold} kg")


# Input

# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End

#Output

# Tortuga plundered! 380 gold stolen, 75000 citizens killed.
# 180 gold added to the city treasury. Santo Domingo now has 810 gold.
# Ahoy, Captain! There are 3 wealthy settlements to go to:
# Havana -> Population: 410000 citizens, Gold: 1100 kg
# Tortuga -> Population: 270000 citizens, Gold: 870 kg
# Santo Domingo -> Population: 240000 citizens, Gold: 810 kg