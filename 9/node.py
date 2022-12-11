class Node:

    def __init__(self, length=0):
        self.__pos = 0, 0
        if length > 0:
            self.tail = Node(length-1)
        else:
            self.tail = None

    def pos(self):
        return self.__pos

    def __getitem__(self, item):
        return self.pos()[item]

    def step(self, direction):
        if direction == 'U':
            self.__pos = self.__pos[0] - 1, self.__pos[1]
        elif direction == 'L':
            self.__pos = self.__pos[0], self.__pos[1] - 1
        elif direction == 'D':
            self.__pos = self.__pos[0] + 1, self.__pos[1]
        elif direction == 'R':
            self.__pos = self.__pos[0], self.__pos[1] + 1
        if self.tail:
            self.__update_tail()

    def __update_tail(self):
        if self.__pos[0] - self.tail[0] > 1:
            self.tail.step('D')
            self.__straighten_tail('x')
        elif self.tail[0] - self.__pos[0] > 1:
            self.tail.step('U')
            self.__straighten_tail('x')
        elif self.__pos[1] - self.tail[1] > 1:
            self.tail.step('R')
            self.__straighten_tail('y')
        elif self.tail[1] - self.__pos[1] > 1:
            self.tail.step('L')
            self.__straighten_tail('y')

#TODO: here is the error
    # def __straighten_tail(self, axis):
    #     if axis == 'x':
    #         if self.tail[1] != self.__pos[1]:
    #             self.tail.__pos = self.tail[0], self.__pos[1]
    #     elif axis == 'y':
    #         if self.tail[0] != self.__pos[0]:
    #             self.tail.__pos = self.__pos[0], self.tail[1]

    def __straighten_tail(self, axis):
        if axis == 'x':
            if self.tail[1] > self.__pos[1]:
                self.tail.step('L')
            elif self.tail[1] < self.__pos[1]:
                self.tail.step('R')
        elif axis == 'y':
            if self.tail[0] > self.__pos[0]:
                self.tail.step('U')
            if self.tail[0] < self.__pos[0]:
                self.tail.step('D')

    def get_snake(self):
        pos = [self.__pos]
        tail = self.tail
        while tail:
            pos.append(tail)
            tail = tail.tail
        return pos