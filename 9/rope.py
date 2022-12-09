class Rope:

    def __init__(self):
        self.head_position = 0, 0
        self.tail_position = 0, 0



    def step(self, direction):
        if direction == 'U':
            self.head_position = self.head_position[0] - 1, self.head_position[1]
        elif direction == 'L':
            self.head_position = self.head_position[0], self.head_position[1] - 1
        elif direction == 'D':
            self.head_position = self.head_position[0] + 1, self.head_position[1]
        elif direction == 'R':
            self.head_position = self.head_position[0], self.head_position[1] + 1
        self.__update_tail()

    def __update_tail(self):
        allignements = [(0, 0, 1)]
        if self.head_position[0] - self.tail_position[0] > 1:
            self.tail_position = self.tail_position[0] + 1, self.tail_position[1]
            self.__straighten_tail('x')
        elif self.tail_position[0] - self.head_position[0] > 1:
            self.tail_position = self.tail_position[0] - 1, self.tail_position[1]
            self.__straighten_tail('x')
        elif self.head_position[1] - self.tail_position[1] > 1:
            self.tail_position = self.tail_position[0], self.tail_position[1] + 1
            self.__straighten_tail('y')
        elif self.tail_position[1] - self.head_position[1] > 1:
            self.__straighten_tail('y')
            self.tail_position = self.tail_position[0], self.tail_position[1] - 1

    def __straighten_tail(self, axis):
        if axis == 'x':
            if self.tail_position[1] != self.head_position[1]:
                self.tail_position = self.tail_position[0], self.head_position[1]
        elif axis == 'y':
            if self.tail_position[0] != self.head_position[0]:
                self.tail_position = self.head_position[0], self.tail_position[1]
