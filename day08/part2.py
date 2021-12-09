from itertools import permutations

with open('.\day08\puzzle.txt') as fp:
    lines = fp.readlines()

digits_list = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9' 
}

segments = 'abcdefg'
combinations = list(permutations(segments, len(segments)))

total = 0
for line in lines:
    for combination in combinations:
        cloned_line = list(line.strip())
        found = True
        
        for i in range(len(cloned_line)):
            if cloned_line[i] not in ['|', ' '] :
                combination_index = ord(cloned_line[i]) - 97
                cloned_line[i] = combination[combination_index] 
        
        
        digits, output = "".join(cloned_line).split(' | ')
        for digit in digits.split():
            if "".join(sorted(digit)) not in digits_list.keys():
                found = False
                break
        
        if found:
            # No more combinations test
            result = ''
            for digit in output.split():
                result += digits_list["".join(sorted(digit))]
            total += int(result)
            break


print(total)