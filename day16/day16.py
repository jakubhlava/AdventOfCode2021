with open("input-sm.txt", "r") as f:
    packet = f.read()

def parse_literal(packet):
    parsed = {
        "version": int(packet[:3], 2),
        "type": int(packet[3:6], 2)
    }
    print(packet[:3], packet[3:6])
    start = 6
    data = []
    while True:
        group = packet[start:start+5]
        data.append(group[1:])
        print(group)
        if group[0] == "0":
            parsed["value"] = int("".join(data), 2)
            break
        else:
            start += 5
    return parsed

binpacket = ''.join([format(int(p, 16), "04b") for p in packet]).replace("0b", "")
print(binpacket)
print(parse_literal(binpacket))