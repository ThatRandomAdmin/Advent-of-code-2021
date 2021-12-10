f = open("Day_2\input.txt", "r")
lines = f.readlines()

x_axis = 0
y_axis = 0
aim = 0

for i in lines:
    command, amount = i.split()
    amount = int(amount)

    if command == "up":
        aim -= amount
    elif command == "down":
        aim += amount
    else:
        x_axis += amount
        y_axis += aim * amount

print(x_axis * y_axis)