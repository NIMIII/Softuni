inbox = {}


while True:
    token = input().split("->")
    if token[0] == "Statistics":
        break

    command = token[0]
    username = token[1]

    if command == "Add":
        if username in inbox:
            print(f"{username} is already registered")
            continue
        inbox[username] = []
    elif command == "Send":
        email = token[2]
        inbox[username].append(email)
    elif command == "Delete":
        if username not in inbox:
            print(f'{username} not found!')
            continue
        inbox.pop(username)


inbox = dict(sorted(inbox.items(), key=lambda u: (-len(u[1]), u[0])))

print(f"Users count: {len(inbox)}")

for key, value in inbox.items():
    print(key)
    for emails in value:
        print(f"- {emails}")


# Input
# Add->Mike
# Add->George
# Send->George->Hello World
# Send->George->Some random test mail
# Send->Mike->Hello, do you want to meet up tomorrow?
# Send->George->It would be a pleasure
# Send->Mike->Another random test mail
# Statistics

# Output
# Users count: 2
# George
#  - Hello World
#  - Some random test mail
#  - It would be a pleasure
# Mike
#  - Hello, do you want to meet up tomorrow?
#  - Another random test mail

