heights = "abcdefghijklmnopqrstuvwxyz"

def read_graph(filename):
    lines = [line.strip() for line in open(filename)]
    return lines

def find_start(graph, distances):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "S":
                distances[i][j] = 0
                return {(i, j)}, distances

def find_a(graph, distances):
    starts = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "S" or graph[i][j] == "a":
                distances[i][j] = 0
                starts.add((i, j))
    return starts, distances

def find_index(letter):
    if letter == "E":
        letter = "z"
    elif letter == "S":
        letter = "a"
    return heights.index(letter)

def find_distance(graph, next_coords, distances):
    if not next_coords:
        for i in distances:
            print(i)
        return -1
    i, j = next_coords.pop()

    if i > 0 and find_index(graph[i - 1][j]) - find_index(graph[i][j]) <= 1 and distances[i - 1][j] - 1 > distances[i][j]:
        next_coords.add((i - 1, j))
        distances[i - 1][j] = distances[i][j] + 1
    if i < len(graph) - 1 and find_index(graph[i + 1][j]) - find_index(graph[i][j]) <= 1 and distances[i + 1][j] - 1 > distances[i][j]:
        next_coords.add((i + 1, j))
        distances[i + 1][j] = distances[i][j] + 1
    if j > 0 and find_index(graph[i][j - 1]) - find_index(graph[i][j]) <= 1 and distances[i][j - 1] - 1 > distances[i][j]:
        next_coords.add((i, j - 1))
        distances[i][j - 1] = distances[i][j] + 1
    if j < len(graph[0]) - 1 and find_index(graph[i][j + 1]) - find_index(graph[i][j]) <= 1 and distances[i][j + 1] - 1 > distances[i][j]:
        next_coords.add((i, j + 1))
        distances[i][j + 1] = distances[i][j] + 1
    return next_coords, distances, (i, j)

    
def part1(graph):
    distances = [[9999 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    next_coords, distances = find_start(graph, distances)
    while next_coords:
        next_coords, distances, letter = find_distance(graph, next_coords, distances)
        if graph[letter[0]][letter[1]] == "E":
            return distances[letter[0]][letter[1]]

def part2(graph):
    distances = [[9999 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    next_coords, distances = find_a(graph, distances)
    while next_coords:
        next_coords, distances, letter = find_distance(graph, next_coords, distances)
        if graph[letter[0]][letter[1]] == "E":
            return distances[letter[0]][letter[1]]


def main(filename):
    graph = read_graph(filename)
    return part1(graph), part2(graph)

print(main("day12\data.txt"))
