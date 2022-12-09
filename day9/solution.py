class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, direction):
        if direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "U":
            self.y += 1

class Tail:
    def __init__(self, head):
        self.x = 0
        self.y = 0
        self.visited = {(0, 0)}
        self.head = head
    def move(self):
        if self.head.x - self.x > 1:
            self.x += 1
            if self.head.y - self.y > 0:
                self.y += 1
            elif self.head.y - self.y < 0:
                self.y -= 1
        elif self.head.x - self.x < -1:
            self.x -= 1
            if self.head.y - self.y > 0:
                self.y += 1
            elif self.head.y - self.y < 0:
                self.y -= 1
        elif self.head.y - self.y > 1:
            self.y += 1
            if self.head.x - self.x > 0:
                self.x += 1
            elif self.head.x - self.x < 0:
                self.x -= 1
        elif self.head.y - self.y < -1:
            self.y -= 1
            if self.head.x - self.x > 0:
                self.x += 1
            elif self.head.x - self.x < 0:
                self.x -= 1
        self.visited.add((self.x, self.y))

def part1(filename):
    head = Head()
    tail = Tail(head)
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        direction, magnitude = line.split()
        for _ in range(int(magnitude)):
            head.move(direction)
            tail.move()
    return len(tail.visited)

def part2(filename):
    knots = []
    knots.append(Head())
    for i in range(9):
        knots.append(Tail(head=knots[i]))
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        direction, magnitude = line.split()
        for _ in range(int(magnitude)):
            knots[0].move(direction)
            for knot in knots[1:]:
                knot.move()
    return len(knots[9].visited)

print("Part 1:", part1("day9/data.txt"))
print("Part 2:", part2("day9/data.txt"))