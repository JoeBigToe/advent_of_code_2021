from math import floor

with open('.\day10\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

points = [3, 57, 1197, 25137]

score = []
for line in data:
    i = 0
    stack = []
    ignore = False
    while i < len(line):
        if line[i] in opening_chars:
            stack.append(line[i])
        else:
            index = opening_chars.index(stack.pop())
            if line[i] != closing_chars[index]:
                ignore = True
                break
        i += 1
    
    if not ignore:
        this_score = 0
        while len(stack):
            this_score *= 5
            this_score += opening_chars.index(stack.pop()) + 1
        score.append(this_score)

print(sorted(score)[floor(len(score)/2)])