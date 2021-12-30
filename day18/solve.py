from io import RawIOBase
from math import floor, ceil
from itertools import permutations

class Node:
    def __init__(self, left = None, right = None, parent = None, value = None, level = None):
        self.left = left
        self.right = right
        self.level = level
        self.value = value
        self.parent = parent

class Tree:
    def __init__(self, data):
        inp = eval(data)
        self.root = Node()
        self.populate(inp, self.root, 0)
        self.search_result = None
        self.search_completed = False
        self.literals = []

    def print(self, node=None):
        if not node:
            node = self.root
        if type(node.value) is int:
            return str(node.value)
        else:
            return "[{0},{1}]".format(self.print(node.left), self.print(node.right))
        
    def __add__(self, other):
        t = Tree("[{0}, {1}]".format(self.print(), other.print()))
        t.reduce()
        return t

    def magnitude(self, node=None):
        if not node:
            node = self.root
        if type(node.value) is int:
            return node.value
        else:
            return 3 * self.magnitude(node.left) + 2 * self.magnitude(node.right)

    def populate(self, inp, node, level):
        left, right = inp
        
        node.left = Node(parent = node, level = level)
        node.right = Node(parent = node, level = level)

        node.left.value = left if isinstance(left, int) else None
        node.right.value = right if isinstance(right, int) else None

        if not isinstance(left, int):
            self.populate(left, node.left, level + 1)

        if not isinstance(right, int):
            self.populate(right, node.right, level + 1)

    def traverse(self):
        node = self.root
        stack = [node]
        literals_stack = []
        while len(stack):
            if node.value != None:
                if node not in literals_stack:
                    literals_stack.append(node)
            if node.left:
                stack.append(node.left)
                node = node.left
            else:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                    node = node.right
        self.literals = literals_stack

    def get_nodes_to_explode(self):
        out = []
        for literal in self.literals:
            if literal.level == 4 and literal.parent not in out:
                out.append(literal.parent)
        return out

    def get_nodes_to_split(self):
        for literal in self.literals:
            if literal.value >= 10:
                return literal

    def reduce(self):
        self.traverse()
        while True:
            nodes_to_explode = self.get_nodes_to_explode()
            for node in nodes_to_explode:
                self.explode_node(node)
            node_to_split = self.get_nodes_to_split()
            if node_to_split:
                self.split_node(node_to_split)
            else:
                break
        

    def explode_node(self, node):
        result = self.find_first_left(node.left)
        if result != None:
            result.value += node.left.value
        
        result = self.find_first_right(node.right)
        if result != None:
            result.value += node.right.value

        index = self.literals.index(node.left)
        self.literals.insert(index, node)
        self.literals.remove(node.left)
        self.literals.remove(node.right)
        node.value, node.left, node.right = 0, None, None

    def split_node(self, node):
        node.left = Node(parent = node, value = floor(node.value/2), level = node.level +1)
        node.right = Node(parent = node, value = ceil(node.value/2), level = node.level +1)
        index = self.literals.index(node)
        self.literals.insert(index, node.right)
        self.literals.insert(index, node.left)
        self.literals.remove(node)
        node.value = None

    def find_first_left(self, node):
        index = self.literals.index(node)
        return self.literals[index -1] if index else None
    
    def find_first_right(self, node):
        index = self.literals.index(node)
        return self.literals[index +1] if index < len(self.literals) -1 else None

def read(path):
    with open(path) as fp:
        data = fp.read().split()
    return [ Tree(el) for el in data]

fish_numbers = read('./day18/puzzle.txt')

# Part 1
current = fish_numbers[0]
for number in fish_numbers[1:]:
    current += number
print(current.magnitude())

# Part  2
current = fish_numbers[0]
max_magnitude = 0
combinations = list(permutations(fish_numbers,2))
for number in combinations:
    current = number[0] + number[1]
    current_mag = current.magnitude()
    if current_mag > max_magnitude:
        max_magnitude = current_mag
print(max_magnitude)