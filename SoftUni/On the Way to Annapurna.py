diary = {}

while True:
    data = input().split("->")
    if data[0] == "END":
        break


    command = data[0]
    store = data[1]

    if command == "Add":
        items = data[2]

        if store not in diary:
            diary[store] = []
            for item in items.split(","):
                diary[store].append(item)
        elif store in diary:

            for item in items.split(","):
                diary[store].append(item)
    elif command == "Remove":
        if store in diary:
            diary.pop(store)
        else:
            continue

diary = dict(sorted(diary.items(), key=lambda u: (len(u[1]),u[0]), reverse=True))


print("Stores list:")

for store, items in diary.items():
    print(store)
    for item in items:
        print(f"<<{item}>>")

# Input
# Add->PeakSports->Map,Navigation,Compass
# Add->Paragon->Sunscreen
# Add->Groceries->Dried-fruit,Nuts
# Add->Groceries->Nuts
# Add->Paragon->Tent
# Remove->Paragon
# Add->Pharmacy->Pain-killers
# END

# Output
# Stores list:
# PeakSports
# <<Map>>
# <<Navigation>>
# <<Compass>>
# Groceries
# <<Dried-fruit>>
# <<Nuts>>
# <<Nuts>>
# Pharmacy
# <<Pain-killers>>
