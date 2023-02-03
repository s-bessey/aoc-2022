import json

def receive_signal(filename):
    lines = []
    for l in open(filename):
        if l != '\n':
            lines.append(json.loads(l))
        # else:
        #     lines.append("")
    return lines

def compare_numbers(left, right):
    print(left, right)
    if left == right:
        return -1
    if left > right:
        return 0
    if left < right:
        return 1    

def compare_packets(left, right):
    if not left and not right:
        return 0
    elif not left:
        return 1
    elif not right:
        return 0
    if not isinstance(left, list):
        left = [left]
    elif type(right) != list:
        right = [right]
    if isinstance(left[0], int) and isinstance(right[0], int):
        for i in range(len(left)):
            correct = compare_numbers(left, right)
            if correct != -1:
                print(correct)
                return correct
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], list) or isinstance(right[i], list):
            compare_packets(left[i], right[i])
        else:
            correct = compare_numbers(left[i], right[i])
            if correct != -1:
                return correct



# print(receive_signal("day13\example.txt"))
print(compare_packets([9], [[8,7,6]]))