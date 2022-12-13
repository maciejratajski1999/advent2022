class Node:

    def __init__(self, length=0):
        self.__pos = 0, 0
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

    def step(self, y, x, jump_flag=0):
        prev = self.__pos
        self.__pos = self.__pos[0] + y, self.__pos[1] + x
        if self.tail:
            self.__update_tail(y, x, prev, jump_flag)

    def __update_tail(self, y, x, prev, jump_flag=0):
        distance_y, distance_x = self.__distance()
        if distance_y + distance_x > 2:
            self.tail.step(y, x, 1)
            new_y, new_x = prev[0] - self.tail.__pos[0], prev[1] - self.tail.__pos[1]
            self.tail.step(new_y, new_x)
        elif distance_y == 2 or distance_x == 2:
            self.tail.step(y, x)
        elif distance_y == distance_x == 1 and jump_flag:
            self.tail.step(y, x, 1)
        else:
            pass


    def __distance(self):
        distance_y = abs(self.__pos[0] - self.tail[0])
        distance_x = abs(self.__pos[1] - self.tail[1])
        return distance_y, distance_x

    def __straighten_tail(self, axis):
        pass


    def get_snake(self):
        pos = [self.__pos]
        tail = self.tail
        while tail:
            pos.append(tail)
            tail = tail.tail
        return pos