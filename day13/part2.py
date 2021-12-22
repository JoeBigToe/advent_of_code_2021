with open('.\day13\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [ el.rstrip() for el in lines ]

def fold(direction, middle, dots):
    
    x_factor = 1 if direction == "fold along x" else 0
    y_factor = 1 if direction == "fold along y" else 0

    iterable_dots = list(dots)
    for dot in iterable_dots:
        x,y = [ int(el) for el in dot.split(",")]
        if x*x_factor > middle or y*y_factor > middle:
            dots.remove(f'{x},{y}')
            dots.add("{0},{1}".format( abs(x_factor * 2 * middle - x), abs(y_factor * 2 * middle - y)))
        
dots = set()
folding_instructions = []

read_dots = True
for line in data:
    if not line:
        read_dots = False
        continue 
    if read_dots:
        dots.add(line)
    else:
        folding_instructions.append(line.split("="))         

for instruction in folding_instructions:
    fold(instruction[0], int(instruction[1]), dots)

# Print dots
max_size = 30
matrix = [[" " for x in range(max_size)] for y in range(max_size)] 
for x in range(max_size):
    for y in range(max_size):
        if f'{x},{y}' in dots:
            matrix[y][x] = "#"

for y in range(max_size):
    print("".join(matrix[y]))
