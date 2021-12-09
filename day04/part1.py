import re 

with open('.\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

numbers = [int(el) for el in data[0].split(',')]

matrix = 0
matrices = {}
matrix_size = len(data[2].split())

for line in range(1, len(data)):
    if data[line] == "" :
        matrix += 1
        for i in range(matrix_size):
            matrices.update({
                "c{0}-m{1}".format(i, matrix): []
            })
        continue

    matrices.update({
        "l{0}-m{1}".format((line) % matrix_size, matrix): [int(el) for el in data[line].split()]
    })

    for i in range(matrix_size):
        matrices["c{0}-m{1}".format(i, matrix)].append(int(data[line].split()[i]))

winning_matrix = False
i = 0
while not(winning_matrix):
    for key in matrices.keys():
        if numbers[i] in matrices[key]:
            matrices[key].remove(numbers[i])
            if len(matrices[key]) == 0:
                winning_matrix = key.split('-')[1]
                break
    if not winning_matrix:
        i += 1

total = 0 
for key in range(5):
    total += sum(matrices["l{0}-{1}".format(key, winning_matrix)])

print(total * numbers[i])

