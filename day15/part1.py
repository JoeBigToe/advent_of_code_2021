# import heartrate
# heartrate.trace(browser=True)
import heapq
from math import floor

def read(path, repetitions):
    out = {}
    infinite_number = 9999999
    with open(path) as fp:
        data = fp.read().split('\n')
    
    max_x, max_y = len(data[0]), len(data)
    for y in range(  repetitions *len(data)):
        for x in range( repetitions *len(data[0])):
            value = (floor(x/max_x) + floor(y/max_y) + int(data[y % max_x][x % max_y])) % 9
            value = value if value else 9
            out.update({f'{x}-{y}' : {'cost': value, 'from': '', 'total_cost': infinite_number},})

    return (out, repetitions * max_x, repetitions * max_y)

def get_neighbours(data, node):
    x,y = [int(el) for el in node.split('-')]
    nodes = filter(lambda x: x in data.keys(), [f'{x-1}-{y}', f'{x+1}-{y}', f'{x}-{y-1}', f'{x}-{y+1}'])
    return list(nodes)

def solve(data, max_x, max_y):
    end_node = f'{max_x}-{max_y}'
    current_key = '0-0'
    current_node = data[current_key]
    current_node['total_cost'] = 0
    prio_q = []
    
    while True:
        neighbour_nodes_keys = get_neighbours(data, current_key)
        for node_key in neighbour_nodes_keys:
            current_cost = data[node_key]['cost'] + current_node['total_cost']
            if current_cost < data[node_key]['total_cost']:
                data[node_key]['total_cost'] = current_cost    
                heapq.heappush(prio_q, (data[node_key]['total_cost'], node_key))
            if node_key == end_node:
                return data[node_key]['total_cost']
        _ = data.pop(current_key)
        _, current_key = heapq.heappop(prio_q)
        current_node = data[current_key]

for index, repetition in enumerate([1, 5]):
    data, max_x, max_y = read('./day15/puzzle.txt', repetition)
    print(f'Part {index + 1}: {solve(data, max_x-1, max_y-1)}')
    