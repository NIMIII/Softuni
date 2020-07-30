string = input()

data = input()

while data != "Finish":
    token = data.split()

    command = token[0]

    if command == "Replace":
        current_ch = token[1]
        new_ch = token[2]
        string = string.replace(current_ch, new_ch)
        print(string)
    elif command == "Cut":
        start_index = int(token[1])
        end_index = int(token[2])
        if 0 <= start_index and end_index < len(string):
            del_string = string[start_index:end_index + 1]
            string = string.replace(del_string, "")
            print(string)
        else:
            print("Invalid indexes!")

    elif command == "Make":
        upper_or_lower = token[1]
        if upper_or_lower == "Upper":
            string = string.upper()
            print(string)
        elif upper_or_lower == "Lower":
            string = string.lower()
            print(string)
    elif command == "Check":
        substring = token[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif command == "Sum":
        start_index = int(token[1])
        end_index = int(token[2])
        if 0 <= start_index and end_index < len(string):
            new_string = string[start_index:end_index + 1]
            sum = 0
            for ch in new_string:
                sum += ord(ch)
            print(sum)
        else:
            print("Invalid indexes!")
    data = input()