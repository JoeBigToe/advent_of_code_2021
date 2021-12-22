from collections import deque
from math import prod

def read(path):
    with open(path) as fp:
        num = fp.read().strip()
        instruction = format(int(num, 16), f'0{4*len(num)}b')
    return instruction


class Program:

    def __init__(self, instruction):
        self.instruction = deque(instruction)
        self.version_sum = 0
        self.bits_read = 0

    def read(self, size):
        self.bits_read += size
        return "".join([self.instruction.popleft() for _ in range(size)])

    def read_packet(self):
        self.version_sum += int(self.read(3), 2)
        packet_type = int(self.read(3), 2)

        if packet_type == 4:
            output = ''
            while True:
                stop =  self.read(1) == '0'                
                output += self.read(4)
                if stop:
                    output = int(output, 2)
                    break
        else:
            packets = []
            if self.read(1) == '0':                
                length = int(self.read(15),2)
                tmp = self.bits_read
                while self.bits_read - tmp < length:
                    packets.append(self.read_packet())
            else:
                c = int(self.read(11), 2)
                for _ in range(c):
                    packets.append(self.read_packet())

            output = {
                0: sum(packets),
                1: prod(packets),
                2: min(packets),
                3: max(packets),
                5: 1 if packets[0] > (packets[1] if len(packets) > 1 else 0) else 0 ,
                6: 1 if packets[0] < (packets[1] if len(packets) > 1 else 0) else 0,
                7: 1 if packets[0] == (packets[1] if len(packets) > 1 else 0) else 0 
            }[packet_type]
        
        return output


p = Program(read("./day16/puzzle.txt"))
result = p.read_packet()

print(f'Part 1: {p.version_sum}')
print(f'Part 2: {result}')
