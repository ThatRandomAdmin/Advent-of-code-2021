f = open("Day_1\input.txt", "r")
lines = f.readlines()

count = 0
prev = 0
data = []

for i in lines:
    data.append(int(i))

for i in range(0, len(data) - 2):
    x = sum(data[i:i+3])
    count += 1 * (x > prev)
    prev = x
        
  
print (count - 1)