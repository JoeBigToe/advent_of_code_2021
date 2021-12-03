def filter_report( data, index, value):
    return list(filter(lambda x: x[index] == value, data))


def loop_report(data, criteria):
    index = 0
    while len(data) > 1:
        count = 0
        for line in range(len(data)):
            if data[line][index] == '1':
                count += 1
        value = int(criteria) if (count >= len(data)/2) else int(not(criteria))
        data = filter_report(data, index, str(value))
        index += 1
    return data
    

with open('.\day03\puzzle.txt') as fp:
    lines = fp.readlines()
    data = [line.rstrip() for line in lines]

oxygen = loop_report(data.copy(), criteria=True)
co2 = loop_report(data.copy(), criteria=False)

print(int(oxygen[0],2) * int(co2[0], 2))