n = int(input())

HP = {}
MP = {}


for i in range(n):
    data = input().split()
    username = data[0]
    hit_points = int(data[1])
    mana = int(data[2])

    HP[username] = hit_points
    MP[username] = mana

while True:
    token = input().split(" - ")
    if token[0] == "End":
        break

    command = token[0]
    username = token[1]

    if command == "CastSpell":
        mp_needed = int(token[2])
        spell_name = token[3]
        if mp_needed <= MP[username]:
            MP[username] -= mp_needed
            print(f"{username} has successfully cast {spell_name} and now has {MP[username]} MP!")
        else:
            print(f"{username} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(token[2])
        attacker = token[3]
        if damage < HP[username]:
            HP[username] -= damage
            print(f"{username} was hit for {damage} HP by {attacker} and now has {HP[username]} HP left!")
        else:
            print(f"{username} has been killed by {attacker}!")
            HP.pop(username)
            MP.pop(username)
    elif command == "Recharge":
        amount = int(token[2])
        left = 200 - MP[username]
        MP[username] = amount + MP[username]
        if MP[username] > 200:
            MP[username] = 200
            print(f"{username} recharged for {left} MP!")
        else:
            print(f"{username} recharged for {amount} MP!")
    elif command == "Heal":
        amount = int(token[2])
        left = 100 - HP[username]
        HP[username] = amount + HP[username]

        if HP[username] > 100:
            HP[username] = 100
            print(f"{username} healed for {left} HP!")
        else:
            print(f"{username} healed for {amount} HP!")

HP = dict(sorted(HP.items(), key=lambda hp: (-hp[1], hp[0])))

for username, hp in HP.items():
    print(username)
    print(f"  HP: {hp}")
    print(f"  MP: {MP[username]}")

# Input
# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End

# Output
# Solmyr healed for 10 HP!
# Solmyr recharged for 50 MP!
# Kyrre was hit for 66 HP by Orc and now has 33 HP left!
# Kyrre has successfully cast ViewEarth and now has 35 MP!
# Solmyr
#   HP: 95
#   MP: 170
# Kyrre
#   HP: 33
#   MP: 35


