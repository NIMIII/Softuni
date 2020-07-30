username = input()

data = input()

while data != "Sign up":
    token = data.split()

    command = token[0]

    if command == "Case":
        l_and_u = token[1]
        if l_and_u == "lower":
            username = username.lower()
            print(username)
        elif l_and_u == "upper":
            username = username.upper()
            print(username)
    elif command == "Reverse":
        start_index = int(token[1])
        end_index = int(token[2])
        if 0 <= start_index and end_index < len(username):
            substring = username[end_index:start_index - 1:-1]
            print(substring)
        else:
            continue
    elif command == "Cut":
        substring = token[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = token[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        char = token[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    data = input()