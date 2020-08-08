string = input()
command = input()
while command != "Reveal":
    token = command.split(":|:")

    args = token[0]

    if args == "InsertSpace":
        index = int(token[1])
        string = string[:index] + " " + string[index:]
        print(string)
    elif args == "Reverse":
        substring = token[1]
        if substring in string:
            string = string.replace(substring, "", 1)
            new_sub = substring[::-1]
            string += new_sub
            print(string)
        else:
            print("error")
    elif args == "ChangeAll":
        substring = token[1]
        replacement = token[2]

        string = string.replace(substring, replacement)

        print(string)


    command = input()

print(f"You have a new text message: {string}")

# Input
# HiwaHiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal

# Output
# Howare?uoy
# Howareyou?
# error
# How areyou?
# How are you?
# You have a new text message: How are you?
