email = input()

data = input()

while data != "Complete":
    token = data.split()

    command = token[0]

    if command == "Make":
        upper_or_lower = token[1]
        if upper_or_lower == "Upper":
            email = email.upper()
            print(email)
        elif upper_or_lower == "Lower":
            email = email.lower()
            print(email)
    elif command == "GetDomain":
        count = int(token[1])
        last_ch = email[-count:]
        print(last_ch)
    elif command == "GetUsername":
        if "@" in email:
            ch = email.index("@")
            substring = email[:ch]
            print(substring)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")


    elif command == "Replace":
        char = token[1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        sord = []
        for ch in email:
            sord.append(str(ord(ch)))
        print(" ".join(sord))
    data = input()
