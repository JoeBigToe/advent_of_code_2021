with open('.\day09\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [ [ int(num) for num in list(el.strip()) ] for el in lines ]

def count_basin(y,x):
    count = 1
    data[y][x] = 9
    if y > 0 and data[y-1][x] != 9:
        count += count_basin(y-1,x)
    if  y < len(data)-1 and data[y+1][x] != 9:
        count += count_basin(y+1,x)
    if  x > 0 and data[y][x-1] != 9:
        count += count_basin(y,x-1)
    if  x < len(data[0])-1 and data[y][x+1] != 9:
        count += count_basin(y,x+1)
    return count

def is_smallest_neighboor(y,x):
    up = data[y-1][x] if y > 0 else 10
    down = data[y+1][x] if y < len(data)-1 else 10
    left = data[y][x-1] if x > 0 else 10
    right = data[y][x+1] if x < len(data[0])-1 else 10

    if data[y][x] < up and \
       data[y][x] < left and \
       data[y][x] < down and \
       data[y][x] < right:
        return count_basin(y,x)
    else:
        return False

total = 0 
for row in range(len(data)):
    for collumn in range(len(data[0])):
        if is_smallest_neighboor(row,collumn):
            total += data[row][collumn] +1

print(total)