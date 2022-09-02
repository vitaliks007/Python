import struct


def create_c_structures(data, address):
    result = []
    for c_address in struct.unpack('>2H', data[address:address + 4]):
        c1 = list(struct.unpack('>2f', data[c_address:c_address + 8]))
        c2 = struct.unpack('>h', data[c_address + 8:c_address + 10])[0]
        c3 = struct.unpack('>q', data[c_address + 10:c_address + 18])[0]

        result.append({
            'C1': c1,
            'C2': c2,
            'C3': c3
        })
    return result


def create_e_structure(data, address):
    result = {}
    e_size = struct.unpack('>I', data[address:address + 4])[0]
    e_address = struct.unpack('>I', data[address + 4:address + 8])[0]
    result['E1'] = list(struct.unpack('>' + str(e_size) + 'h',
                                      data[e_address:e_address + e_size * 2]))

    e_size = struct.unpack('>H', data[address + 8:address + 10])[0]
    e_address = struct.unpack('>I', data[address + 10:address + 14])[0]
    result['E2'] = list(struct.unpack('>' + str(e_size) + 'B',
                                      data[e_address:e_address + e_size]))

    return result


def main(data):
    a1 = struct.unpack('>I', data[3:7])[0]
    a2 = struct.unpack('>I', data[7:11])[0]

    b1 = struct.unpack('>h', data[a1:a1 + 2])[0]
    b2 = create_c_structures(data, a1 + 2)
    b3 = struct.unpack('>q', data[a1 + 6:a1 + 14])[0]
    b4 = struct.unpack('>d', data[a1 + 14:a1 + 22])[0]

    d1 = struct.unpack('>H', data[a2:a2 + 2])[0]
    d2 = struct.unpack('>b', data[a2 + 2:a2 + 3])[0]
    d3 = create_e_structure(data, a2 + 3)
    d4 = struct.unpack('>b', data[a2 + 17:a2 + 18])[0]

    out_dict = {
        'A1': {
            'B1': b1,
            'B2': b2,
            'B3': b3,
            'B4': b4
        },
        'A2': {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4
        }
    }
    return out_dict


print(main(b'YQQ\x00\x00\x00/\x00\x00\x00P>@\xd6o\xbe\x96T\xda\x116x\x1b+\x94\xbd\xdc\x83'
           b'\xe1\xbe\xb0\x17\xd5<\xb2\xb3\t\xe1\x821\\\x9c\xde\xd8\xe4\x0bI\xce'
           b'3\x00\x0b\x00\x1dd\x81f\x1fwq\xd8\x06?\xee\xf1\xca\x8aC\xae\xb2ay<'
           b'H\xbc\xf4\xf6\x8a\xe5a\xac\xa0\x7f{\x00\x00\x00\x03\x00\x00\x00E\x00'
           b'\x05\x00\x00\x00K\xcd'))
