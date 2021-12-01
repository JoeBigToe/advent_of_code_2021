

with open('.\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [int(line.rstrip()) for line in lines]

increases = 0
for i in range(len(data)-1):
    if (data[i+1] > data[i]):
        increases += 1

print(increases)
