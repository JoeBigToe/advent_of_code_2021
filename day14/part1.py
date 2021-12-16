from collections import Counter

with open('.\day14\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [ el.rstrip() for el in lines ]

start = list(data[0])

patterns = {}
for i in range(2,len(data)):
    key, value = data[i].split(' -> ')
    patterns.update({
        key: value
    })

steps = 10
for step in range(steps):
    i = 1
    while i < len(start):
        key = "".join(start[i-1:i+1])
        start.insert(i, patterns[key])
        i += 2
count = Counter(start)
ordered = count.most_common()
high = ordered[0][1]
low = ordered[-1][1]
print(high - low)



