class Directory:
    def __init__(self, name, size,  parent=None, is_file=False):
        self.name = name
        self.files = []
        self.dirs = {}
        self.parent = parent
        self.size = size
        self.is_file = is_file

root = Directory("/", 0, None)

def create_tree(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    current = None
    for line in lines:
        l = line.split()
        # Changing directories
        if l[1] == "cd":
            curr_dir = line.split()[-1]
            # go up a level
            if curr_dir == "..":
                current = current.parent
            # is root
            elif curr_dir == "/":
                current = root
            # otherwise, cd into this directory
            else:
                current = current.dirs[l[2]]
        # look at dirs
        elif l[0] == "dir":
            current.dirs[l[1]] = Directory(l[1], 0, parent = current)
        elif l[1] != "ls":
            current.dirs[l[1]] = Directory(l[1], int(l[0]), parent=current, is_file=True)
    return root


def traverse(root, dirs):
    for node in root.dirs.values():
        traverse(node, dirs)
        node.parent.size += node.size
        if not node.is_file:
            dirs.append(node.size)
    


def part1():
    tree = create_tree("day7/data.txt")
    dirs = []
    traverse(tree, dirs)
    vals = [item for item in dirs if item <= 100000]
    print(sum(vals))

def part2():
    tree = create_tree("day7/data.txt")
    dirs = []
    traverse(tree, dirs)
    used = root.size
    needed = used - 70000000 + 30000000
    dirs.sort()
    for i in dirs:
        if i > needed:
            print(i)
            break

# part1()
part2()
# def part1(data):
