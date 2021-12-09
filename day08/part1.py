with open('.\day08\puzzle.txt') as fp:
    lines = fp.readlines()

total = 0
for line in lines:
    trials, output = line.split(' | ')
    digits = output.split()
    total += len(list(filter(lambda x: len(x) in [2,3,4,7], digits)))

print(total)