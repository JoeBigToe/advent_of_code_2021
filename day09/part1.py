with open('.\day09\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [ [ int(num) for num in list(el.strip()) ] for el in lines ]

def is_smallest_neighboor(y,x):
    up = data[y-1][x] if y > 0 else 10
    down = data[y+1][x] if y < len(data)-1 else 10
    left = data[y][x-1] if x > 0 else 10
    right = data[y][x+1] if x < len(data[0])-1 else 10

    if data[y][x] < up and \
       data[y][x] < left and \
       data[y][x] < down and \
       data[y][x] < right:
        return True
    else:
        return False
    pass

total = 0 
for row in range(len(data)):
    for collumn in range(len(data[0])):
        if is_smallest_neighboor(row,collumn):
            total += data[row][collumn] +1

print(total)