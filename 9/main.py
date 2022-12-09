from node import Node

with open('input2.txt', 'r') as file:
    steps = []
    for line in file.readlines():
        line = line.strip()
        step = line.split()
        step = step[0], int(step[1])
        steps.append(step)
    length = 1
    rope = Node(length)
    visited = []
    for direction, times in steps:
        for _i in range(times):
            rope.step(direction)
            visited.append(rope.__tail)
            print(rope.pos())
