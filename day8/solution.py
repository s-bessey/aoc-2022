def is_visible(loc, graph, y_max, x_max):
    y = loc[0]
    x = loc[1]
    height = graph[y][x]
    top = bottom = left = right = 1

    i = 0
    while i < y:
        if graph[i][x] >= height:
            top = 0
            break
        i += 1

    i = y + 1
    while i < y_max:
        if graph[i][x] >= height:
            bottom =  0
            break
        i += 1

    i = 0
    while i < x:
        if graph[y][i] >= height:
            left = 0
            break
        i += 1
    i = x + 1
    while i < x_max:
        if graph[y][i] >= height:
            right = 0
            break
        i += 1

    return max([top, bottom, left, right])

def part1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    visible = 0
    x_max = len(lines[0]) - 1
    y_max = len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            if i == y_max - 1 or j == x_max - 1 or i == 0 or j == 0:
                visible += 1
            else:
                visible += is_visible([i, j], lines, y_max, x_max)

    print(visible)

def visibility(loc, graph, y_max, x_max):
    squares = [0, 0, 0, 0]
    y = loc[0]
    x = loc[1]

    if x == 0 or y == 0 or x == x_max or y == y_max:
        return 0
    height = graph[y][x]

    i = y - 1
    while i >= 0:
        squares[0] += 1
        if graph[i][x] >= height:
            break
        i -= 1
    i = y + 1
    while i < y_max:
        squares[1] += 1
        if graph[i][x] >= height:
            break
        i += 1

    i = x - 1
    while i >= 0:
        squares[2] += 1
        if graph[y][i] >= height:
            break
        i -= 1
    i = x + 1
    while i < x_max:
        squares[3] += 1
        if graph[y][i] >= height:
            break
        i += 1

    return squares[0] * squares[1] * squares[2] * squares[3]

def part2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    largest_sight = 0
    x_max = len(lines[0]) - 1
    y_max = len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            v = visibility([i, j], lines, x_max, y_max)
            if v > largest_sight:
                largest_sight = v
    print(largest_sight)

part1("day8/data.txt")
part2("day8/data.txt")
