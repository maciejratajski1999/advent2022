from node import Node

directions = {'U': (-1, 0),
              'D': (1, 0),
              'L': (0, -1),
              'R': (0, 1)}

with open('input2.txt', 'r') as file:
    steps = []
    for line in file.readlines():
        line = line.strip()
        step = line.split()
        step = step[0], int(step[1])
        steps.append(step)
    length = 9
    rope = Node(length)
    visited = []
    for direction, times in steps:
        print(direction, times)
        for _i in range(times):
            y, x = directions[direction]
            rope.step(y, x)
            tail = rope.tail
            for j in range(length-1):
                tail = tail.tail
            visited.append((tail[0], tail[1]))
            snake = rope.get_snake()
            x_min, x_max = -0,5
            x_range = x_max - x_min + 1
            y_min, y_max = -5,0
            y_range = y_max - y_min + 1
            grid = [[str('.') for _j in range(x_range)] for _i in range(y_range)]
            # print(grid)
            # print(y_min, x_min)
            for place in visited:
            #     # print(place)
                grid[place[0] - y_min][place[1] - x_min] = "#"
            for i in range(len(snake)):
                pos = snake[len(snake) - i - 1]
                grid[pos[0] - y_min][pos[1] - x_min] = str(len(snake) - i - 1)
            for row in grid:
                print(''.join(row))

print(len(set(visited)))
visited = set(visited)
# xs, ys = [grid[1] for grid in visited], [grid[0] for grid in visited]
# x_min, x_max = min(xs), max(xs)
# x_range = x_max - x_min + 1
# y_min, y_max = min(ys), max(ys)
# y_range = y_max - y_min + 1
# grid = [[str('.') for _j in range(x_range)] for _i in range(y_range)]
# # print(grid)
# # print(y_min, x_min)
# for place in visited:
#     # print(place)
#     grid[place[0] - y_min][place[1] - x_min] = "#"
# for row in grid:
#     print(''.join(row))