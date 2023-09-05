# THIS FILE HAS AN ERROR! If there are nested lists, sometimes the case where one
# list is shorter will break!

import json, functools

def compare(val1, val2):
    # if both integers, lower should come first
    if isinstance(val1, int) and isinstance(val2, int):
        if val1 != val2:
            return val1 < val2
    # if both lists, compare each value in each list
    else:
        # make sure both are lists
        val1 = val1 if isinstance(val1, list) else [val1]
        val2 = val2 if isinstance(val2, list) else [val2]

        for i in range(max(len(val1), len(val2))):
            try:
                val1[i]
            except IndexError:
                return True
            try:
                val2[i]
            except IndexError:
                return False
            truth = compare(val1[i], val2[i])

            if truth != None:
                return 1 if truth == True else -1

def solution(filename):
    # with open(filename, 'r') as f:
    #     signals = f.read().splitlines()
    signals = []
    for l in open(filename, 'r'):
        if l != '\n':
            signals.append(json.loads(l))

    part1 = []
    for i in range(0, len(signals), 2):
        if compare(signals[i], signals[i + 1]) == 1:
            part1.append(i // 2 + 1)
    print(sum(part1))

    signals.append([[2]])
    signals.append([[6]])
    sorted_signals = sorted(signals, key=functools.cmp_to_key(compare), reverse=True)
    print((sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))
    with open("day13/answer.txt", 'w') as f:
        for line in sorted_signals: f.write(str(line) + "\n")
solution("day13/data.txt")
