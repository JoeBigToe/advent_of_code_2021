# arr1 = current_pos, arr2 = diff
def add_arrays(arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] += arr2[i]

def mult_array(arr1, factor):
    out = arr1.copy()
    for i in range(len(out)):
        out[i] *= factor 
    return out

with open('.\day02\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

# horizontal, depth
pos = [0,0]

ins = {
    'forward': [1,0],
    'down': [0,1],
    'up': [0,-1]
}

for inst in data:
    move, x = inst.split()
    add_arrays(pos, mult_array(ins[move], int(x)))

print(pos[0]*pos[1])