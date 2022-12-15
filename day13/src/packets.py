import json

from functools import cmp_to_key


def parse_packet(line):
    return json.loads(line)


def right_order(p1, p2):
    if isinstance(p1, int):
        if isinstance(p2, int):
            if p1 == p2:
                return None
            return p1 < p2
        return right_order([p1], p2)

    # p1 list and p2 int
    if isinstance(p2, int):
        return right_order(p1, [p2])

    # both lists
    i = 0
    right = None
    while right is None:
        if i >= len(p1) and i >= len(p2):
            return None
        if i >= len(p2):
            return False
        if i >= len(p1):
            return True
        right = right_order(p1[i], p2[i])
        i += 1
    return right


def right_order_indices(input_lines):
    right_order_sum = 0
    for i in range(0, len(input_lines), 3):
        p1 = parse_packet(input_lines[i])
        p2 = parse_packet(input_lines[i + 1])
        if right_order(p1, p2):
            right_order_sum += i // 3 + 1
    return right_order_sum


def compare(p1, p2):
    result = right_order(p1, p2)
    if result:
        return -1
    if result == None:
        return 0
    return 1


def sorted_packets(input_lines):
    packets = [parse_packet("[[2]]"), parse_packet("[[6]]")]
    for i in range(0, len(input_lines), 3):
        packets.append(parse_packet(input_lines[i]))
        packets.append(parse_packet(input_lines[i + 1]))

    packets.sort(key=cmp_to_key(compare))
    return packets


def decoder_key(input_lines):
    packets = sorted_packets(input_lines)
    for i in range(len(packets)):
        if json.dumps(packets[i]) == "[[2]]":
            p1 = i + 1
        if json.dumps(packets[i]) == "[[6]]":
            p2 = i + 1
    return p1 * p2
