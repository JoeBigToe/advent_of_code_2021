

with open('.\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [int(line.rstrip()) for line in lines]

increases = 0
for i in range(len(data)-1):
    if (sum(data[i+1:i+4]) > sum(data[i:i+3])):
        increases += 1

print(increases)
