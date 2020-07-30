n = int(input())
cars = {}
for i in range(n):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])


    cars[car] = {}
    cars[car]["mileage"] = mileage
    cars[car]["fuel"] = fuel


input_command = input()
while input_command != "Stop":
    tokens = input_command.split(" : ")
    command = tokens[0]
    car = tokens[1]
    if command == "Drive":
        fuel = int(tokens[3])
        distance = int(tokens[2])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] > 100_000:
                print(f"Time to sell the {car}!")
                del (cars[car])
    elif command == "Refuel":
        fuel = int(tokens[2])
        fuel_to_fill = 0
        current_fuel = cars[car]["fuel"]

        if current_fuel + fuel <= 75:

            cars[car]["fuel"] += fuel
            fuel_to_fill = fuel
        else:
            fuel_to_fill = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
        print(f"{car} refueled with {fuel_to_fill} liters")

    elif command == "Revert":
        distance = int(tokens[2])
        if cars[car]["mileage"] - distance < 10_000:
            cars[car]["mileage"] = 10_000
        else:
            cars[car]["mileage"] -= distance
            print(f"{car} mileage decreased by {distance} kilometers")





    input_command = input()
sorted_cars = sorted(cars.keys(), key= lambda c:(-cars[c]["mileage"], c))

for x in sorted_cars:

    print(f"{x} -> Mileage: {cars[x]['mileage']} kms, Fuel in the tank: {cars[x]['fuel']} lt.")