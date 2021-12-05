global x_points

def add_line(map, pts):
    
    x_diff = (pts[2] - pts[0])
    y_diff = (pts[3] - pts[1])
    size = max([abs(x_diff), abs(y_diff)])
    
    x_dir = int(x_diff / abs(x_diff) if x_diff else 0)
    y_dir = int(y_diff / abs(y_diff) if y_diff else 0)
    
    for inc in range(size+1):
        x = pts[0] + inc*x_dir
        y = pts[1] + inc*y_dir
        map[y][x] += 1
        if map[y][x] >= 2:
            x_points.update({ "{0}-{1}".format(x,y) : map[y][x]})

with open('.\day05\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

inst = []
for line in data:
    p1, p2 = line.split(' -> ')
    inst += [ int(el) for el in p1.split(',')]
    inst += [ int(el) for el in p2.split(',')]

map_size = max(inst)
map = [ [0 for i in range(map_size+1)] for j in range(map_size+1)]

x_points = {}

for i in range(0, len(inst), 4):
    if inst[i] == inst[i+2] or \
       inst[i+1] == inst[i+3]:
        add_line(map, inst[i:i+4])
    

print(len(x_points.keys()))