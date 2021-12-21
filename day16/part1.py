def read(path):
    with open(path) as fp:
        num = fp.read().strip()
        instruction = format(int(num, 16), f'0{4*len(num)}b')

    return instruction

def read_literal(packet):
    
    group_size = 5
    literal = ''
    
    blocks = [ packet[i:i + group_size] for i in range(0, len(packet), group_size) ]
    
    for block in blocks:
        literal += block[1:]
        if block[0] == '0':
            break
    
    return literal

def read_packet(instruction):
    packet_version = int(instruction[:3], 2)
    packet_type = int(instruction[3:6], 2)

    if packet_type == 4:
        packet = instruction[6:]
        # return read_literal(packet)
        return packet_version
    else:
        if instruction[6] == '0':
            length = int(instruction[7:22],2)
            tmp = instruction[22:22+length]
            packets = []
            for i in range(0, len(tmp), 11):
                if i + 21 < len(tmp):
                    packets.append(tmp[i:i + 11])
                else:
                    packets.append(tmp[i:])
                    break

        else:
            length = int(instruction[7:18],2)
            tmp = instruction[18:18+11*length]
            packets = [ tmp[i:i + 11] for i in range(0, len(tmp), 11) ]
        
        for packet in packets:
            packet_version += read_packet(packet)
        
        return packet_version


print(read_packet(read("./day16/puzzle.txt")))