# arr1 = current_pos, arr2 = diff
def add_arrays(arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] += arr2[i]

def mult_array(arr1, factor):
    for i in range(len(arr1)):
        arr1[i] *= factor 

def update_depth(arr1, factor):
    arr1[1] = arr1[0]*factor

with open('.\day02\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

# horizontal, depth, aim
pos = [0,0,0]

ins = {
    'forward': [1,0,0],
    'down': [0,0,1],
    'up': [0,0,-1]
}

for inst in data:
    move, x = inst.split()
    diff = ins[move].copy()
    mult_array(diff, int(x))
    if move == 'forward':
        update_depth(diff, pos[-1])
    
    add_arrays(pos, diff)

print(pos[0]*pos[1])