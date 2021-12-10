f = open("Day_2\input.txt", "r")
lines = f.readlines()

x_axis = 0
y_axis = 0

for i in lines:
    command, amount = i.split()
    amount = int(amount)

    if command == "up":
        y_axis -= amount
    elif command == "down":
        y_axis += amount
    else:
        x_axis += amount

print(x_axis * y_axis)