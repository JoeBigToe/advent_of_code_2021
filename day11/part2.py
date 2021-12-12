with open('.\day11\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [ [ int(num) for num in list(el.strip()) ] for el in lines ]

x_max = len(data[0])
y_max = len(data)

def remove_out_of_index(el):
    
    x, y = [ int(a) for a in el.split(":")]
    if x < 0 or x >= x_max or y < 0 or y >= y_max:
        return False
    else: 
        return True

def add_energy_to_neighboors(dumbos, neighboors):
    flashes = 0
    for neighboor in neighboors:
        if not dumbos[neighboor]['flashed']:
            dumbos[neighboor]['value'] += 1
            if dumbos[neighboor]['value'] > 9:
                dumbos[neighboor]['flashed'] = True
                dumbos[neighboor]['value'] = 0
                flashes += add_energy_to_neighboors(dumbos, dumbos[neighboor]['neighboors']) + 1
    return flashes
    
def get_neighboors(x,y):
    output = [
        "{0}:{1}".format(x-1,y-1),
        "{0}:{1}".format(x,y-1),
        "{0}:{1}".format(x+1,y-1),
        "{0}:{1}".format(x-1,y),
        "{0}:{1}".format(x+1,y),
        "{0}:{1}".format(x-1,y+1),
        "{0}:{1}".format(x,y+1),
        "{0}:{1}".format(x+1,y+1)
    ]

    filtered_output =  list(filter(remove_out_of_index, output))
    return filtered_output

flashes = 0
dumbos = {}
steps = 1000

for y in range(len(data)):
    for x in range(len(data[0])):
        dumbos.update({
            "{0}:{1}".format(x,y) : {
                "value": data[y][x],
                "flashed": False,
                "neighboors": get_neighboors(x,y)  
            }
        })
flashes = 0
for step in range(steps):
    for key in dumbos.keys():
        dumbos[key]['flashed'] = False
    flashes += add_energy_to_neighboors(dumbos, dumbos.keys())
    
    if all([dumbos[key]['flashed'] for key in dumbos.keys()]):
        print(step+1)
        break
