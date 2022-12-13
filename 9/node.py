class Node:

    def __init__(self, length=0):
        self.__pos = 0, 0
        self.__length = length
        if length > 0:
            self.tail = Node(length-1)
        else:
            self.tail = None

    def pos(self):
        return self.__pos

    # def __directions(self, direction):
    #
    #     return directions[direction]

    def __getitem__(self, item):
        return self.pos()[item]

    def step(self, y, x):
        self.__pos = self.__pos[0] + y, self.__pos[1] + x
        if self.tail:
            self.__update_tail()

    def __update_tail(self):
        distance_y, distance_x = self.__distance()
        if distance_y == 1 and distance_x == 1:
            pass
        elif distance_y + distance_x >= 2:
            breakflag=0
            for y in [-1, 0, 1]:
                if breakflag:
                    break
                for x in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    current_y, current_x = self.tail.__pos
                    new_y, new_x = current_y + y, current_x + x
                    if abs(self.__pos[0] - new_y) + abs(self.__pos[1] - new_x) == 1:
                        self.tail.step(y, x)
                        breakflag = 1
                        break
            else:
                for direction in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                    y, x = direction
                    current_y, current_x = self.tail.__pos
                    new_y, new_x = current_y + y, current_x + x
                    if abs(self.__pos[0] - new_y) == abs(self.__pos[1] - new_x) == 1:
                        self.tail.step(y, x)
                        break

    def __distance(self):
        distance_y = abs(self.__pos[0] - self.tail[0])
        distance_x = abs(self.__pos[1] - self.tail[1])
        return distance_y, distance_x

    def get_snake(self):
        pos = [self.__pos]
        tail = self.tail
        while tail:
            pos.append(tail)
            tail = tail.tail
        return pos