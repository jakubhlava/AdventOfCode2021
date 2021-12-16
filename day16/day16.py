from math import prod
with open("input.txt", "r") as f:
    packet_data = f.read().strip()

part1 = 0

def parse_packet(packet):
    global part1
    if packet[-4:-1] == "0000":
        packet = packet[:-4]
    parsed = {
        "version": int(packet[:3], 2),
        "type": int(packet[3:6], 2)
    }
    part1 += parsed["version"]
    if parsed["type"] == 4:
        #print("Detected packet literal type")
        start = 6
        data = []
        while True:
            group = packet[start:start+5]
            data.append(group[1:])
            start += 5
            if group[0] == "0":
                parsed["value"] = int("".join(data), 2)
                break
       # print("Parsed packet:", parsed, "len:", start)
        return parsed, start
    else:
      #  print("Detected operator packet")
        parsed["len_type_id"] = packet[6]
        if parsed["len_type_id"] == "0":
           # print("Detected length mode")
            mode = 0
            #print("Len",packet[7:22])
            length = int(packet[7:22], 2)
        else:
           # print("Detected count mode")
            mode = 1
          #  print("Len", packet[7:18])
            length = int(packet[7:18], 2)
        parsed["subpackets"] = []
        start = 22 if mode == 0 else 18
        while length > 0:
         #   print("Remaining length of operator data:", length)
            pak, end = parse_packet(packet[start:])
            start += end
            if mode == 0:
                length -= end
            else:
                length -= 1
            parsed["subpackets"].append(pak)
        #print("Parsed operator packet", parsed, "len:", start)
        return parsed, start

def get_packet_value(packet):
    match packet["type"]:
        case 4:
            return packet["value"]
        case 0:
            return sum([get_packet_value(p) for p in packet["subpackets"]])
        case 1:
            return prod([get_packet_value(p) for p in packet["subpackets"]])
        case 2:
            return min([get_packet_value(p) for p in packet["subpackets"]])
        case 3:
            return max([get_packet_value(p) for p in packet["subpackets"]])
        case 5:
            return 1 if get_packet_value(packet["subpackets"][0]) > get_packet_value(packet["subpackets"][1]) else 0
        case 6:
            return 1 if get_packet_value(packet["subpackets"][0]) < get_packet_value(packet["subpackets"][1]) else 0
        case 7:
            return 1 if get_packet_value(packet["subpackets"][0]) == get_packet_value(packet["subpackets"][1]) else 0

binpacket = ''.join([format(int(p, 16), "04b") for p in packet_data]).replace("0b", "")
pkt, end = parse_packet(binpacket)
print(pkt)
print("Part 1:", part1)
print("Part 2:", get_packet_value(pkt))

