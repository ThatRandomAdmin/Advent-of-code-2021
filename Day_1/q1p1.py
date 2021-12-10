f = open("Day_1\input.txt", "r")
lines = f.readlines()

count = 0
prev = 0

for i in lines:
    x = int(i)
    count += 1 * (x > prev)
    prev = x
        
print (count - 1)
