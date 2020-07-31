string = input()

while True:
    command = input()
    if command == "For Azeroth":

        break
    tokens = command.split()

    comanda = tokens[0]

    if comanda == "GladiatorStance":
        string = string.upper()
        print(string)
    elif comanda == 'DefensiveStance':
        string = string.lower()
        print(string)
    elif comanda == "Dispel":
        index = int(tokens[1])
        letter = tokens[2]
        if 0 <= index < len(string):
            string = string[:index] + letter + string[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    elif comanda == "Target":
        if tokens[1] == "Change":
            substring = tokens[2]
            second_substring = tokens[3]
            string = string.replace(substring, second_substring)
            print(string)

        elif tokens[1] == "Remove":
            substring = tokens[2]
            string = string.replace(substring, "")
            print(string)

        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")