with open('.\day10\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

points = [3, 57, 1197, 25137]

total = 0
for line in data:
    i = 0
    stack = []  
    while i < len(line):
        if line[i] in opening_chars:
            stack.append(line[i])
        else:
            index = opening_chars.index(stack.pop())
            if line[i] != closing_chars[index]:
                total += points[closing_chars.index(line[i])]
                break
        i += 1

print(total)