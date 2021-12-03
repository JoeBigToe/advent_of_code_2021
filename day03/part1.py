


with open('.\day03\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

gama = ''
for i in range(len(data[0])):
    count = 0
    for line in range(len(data)):
        if data[line][i] == '1':
            count += 1
    gama += '1' if (count > len(data)/2) else '0'

gama_int = int(gama, 2)
epsilon_int = gama_int ^ pow(2, len(data[0])) -1

print(gama_int * epsilon_int)