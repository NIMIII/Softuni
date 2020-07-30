string = input()
data = input()
while data != "Generate":
    token = data.split(">>>")

    command = token[0]

    if command == "Contains":
        substring = token[1]
        if substring in string:
            print(f"{string} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        indices = token[1]
        start_index = int(token[2])
        end_index = int(token[3])
        if indices == "Upper":
            new_string = string[start_index:end_index]
            upper_string = new_string.upper()

            string = string.replace(new_string, upper_string)
            print(string)
        elif indices == "Lower":
            new_string = string[start_index:end_index]
            lower_string = new_string.lower()

            string = string.replace(new_string, lower_string)
            print(string)
    elif command == "Slice":
        start_index = int(token[1])
        end_index = int(token[2])

        new_string = string[start_index:end_index]
        string = string.replace(new_string, "")
        print(string)

    data = input()

print(f"Your activation key is: {string}")