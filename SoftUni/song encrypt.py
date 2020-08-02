import re

regex = r"\b(?P<artist>[A-Z][a-z\s\']+):(?P<song>[A-Z\s]+)\b"

while True:
    command = input()

    if command == "end":
        break

    match = re.fullmatch(regex, command)
    if match:
        artist = match["artist"]
        key = len(artist)
        sad = match[0]

        gay = ""
        for ch in sad:
            new_ord = ord(ch) + key
            if ch.isupper():
                if new_ord > 90:
                    new_key = key - (90 - ord(ch))
                    new_ord = 64 + new_key
                    gay += chr(new_ord)
                else:
                    gay += chr(new_ord)
            if ch.islower():
                if new_ord > 122:
                    new_key = key - (122 - ord(ch))
                    new_ord = 96 + new_key
                    gay += chr(new_ord)
                else:
                    gay += chr(new_ord)

            if ch == " " or ch == "'" or ch == ":":
                gay += ch
        if ":" in gay:
            gay = gay.replace(":", "@")
        print(f"Successful encryption: {gay}")
    else:
        print("Invalid input!")


# Input

# Eminem:VENOM
# Linkin park:NUMB
# Drake:NONSTOP
# Adele:HELLO
# end


# Output

# Michael Jackson:ANOTHER PART OF ME
# Adele:ONE AND ONLY
# Guns n'roses:NOVEMBER RAIN
# Christina Aguilera: HuRt
# end
#
