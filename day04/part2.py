import re 

def get_winners(matrices):
    winners = []
    for key in matrices.keys():
        if len(matrices[key]) == 0:
            winners.append(key.split('-')[1])
    return list(dict.fromkeys(winners))


with open('.\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

numbers = [int(el) for el in data[0].split(',')]

matrix = 0
matrices = {}
matrix_size = len(data[2].split())

# Construct the matrices data structure
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

# Run the bingo game
for i in range(len(numbers)):
    for key in matrices.keys():
        if numbers[i] in matrices[key]:
            matrices[key].remove(numbers[i])

    winner_boards = get_winners(matrices)

    # Process winners
    if winner_boards:
        for winner in winner_boards:
            total = 0 
            for key in range(5):
                total += sum(matrices["l{0}-{1}".format(key, winner)])
            score = total * numbers[i]
            for key in range(5):
                del matrices["l{0}-{1}".format(key, winner)]
                del matrices["c{0}-{1}".format(key, winner)]


# Print the result
print(score)

