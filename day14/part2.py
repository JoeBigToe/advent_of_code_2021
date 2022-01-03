from collections import Counter

def read(file):
    with open(file) as fp:
        pattern, instructions = fp.read().split('\n\n')
        mapping = { el[:2]: el[6] for el in instructions.split('\n') }
        pairs = Counter( el for el in zip(pattern, pattern[1:]) )
        chars = Counter(pattern)
    
    return pairs, mapping, chars

def solve(pairs, mapping, chars, steps):

    for _ in range(steps):
        new_pairs = Counter()
        for (a,b), count in pairs.items():
            match = mapping[a+b]
            new_pairs[a+match] += count
            new_pairs[match+b] += count
            chars[match] += count
        pairs = new_pairs
    return (max(chars.values()) - min(chars.values()))

print(solve(*read('.\day14\puzzle.txt'), 40))
