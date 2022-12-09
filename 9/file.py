from rope import Rope

with open('input.txt', 'r') as file:
    steps = []
    for line in file.readlines():
        line = line.strip()
        step = line.split()
        step = step[0], int(step[1])
        steps.append(step)
    rope = Rope()
    visited_by_tail = [(rope.tail_position)]
    for step in steps:
        direction, times = step
        for _i in range(times):
            rope.step(direction)
            print(rope.head_position, rope.tail_position)
            visited_by_tail.append(rope.tail_position)
    print(visited_by_tail)
    print(len(set(visited_by_tail)))