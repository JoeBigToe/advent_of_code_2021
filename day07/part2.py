from statistics import median

def summatory(num):
    return num * (num+1) / 2
    
def calculate_cost(data, point):
    return sum([ summatory(abs(el-point)) for el in data ]) 

def find_point(data, point, direction):
    point += direction
    cost = calculate_cost(data, point)
    new_cost = cost

    while True:
        point += direction
        new_cost = calculate_cost(data, point)
        if new_cost < cost:
            cost = new_cost
        else:
            break

    print(cost)

with open('.\day07\puzzle.txt') as fp:
    line = fp.readlines()
    data = [ int(el) for el in line[0].split(',') ]


point = round(median(data))
cost = calculate_cost(data, point)

if calculate_cost(data, point + 1) < cost:
    find_point(data, point, 1)
elif calculate_cost(data, point - 1) < cost:
    find_point(data, point, -1)
else:
    print(cost)
    

