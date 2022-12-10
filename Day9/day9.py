class rope_end():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def coord_x(self):
        return self.x
    def coord_y(self):
        return self.y
    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1
    def move_up(self):
        self.y += 1
    def move_down(self):
        self.y -= 1
    def distance(self,rope2):
        return ((rope2.coord_x() - self.coord_x())** 2 + (rope2.coord_y() - self.coord_y())** 2)** .5
    def follow_end(self,rope2):
        if ((rope2.coord_y() - self.coord_y()) == 2) and (rope2.coord_x() == self.coord_x()): self.move_up()
        elif ((rope2.coord_y() - self.coord_y()) == -2) and (rope2.coord_x() == self.coord_x()): self.move_down()
        elif ((rope2.coord_x() - self.coord_x()) == 2) and (rope2.coord_y() == self.coord_y()) : self.move_right()
        elif ((rope2.coord_x() - self.coord_x()) == -2) and (rope2.coord_y() == self.coord_y()): self.move_left()
        elif ((rope2.coord_y() - self.coord_y()) == 2) and ((rope2.coord_x() - self.coord_x()) == 1) or \
             ((rope2.coord_y() - self.coord_y()) == 1) and ((rope2.coord_x() - self.coord_x()) == 2): 
                 self.move_up()
                 self.move_right()
        elif ((rope2.coord_y() - self.coord_y()) == 2) and ((rope2.coord_x() - self.coord_x()) == -1) or \
             ((rope2.coord_y() - self.coord_y()) == 1) and ((rope2.coord_x() - self.coord_x()) == -2): 
                 self.move_up()
                 self.move_left()
        elif ((rope2.coord_y() - self.coord_y()) == -2) and ((rope2.coord_x() - self.coord_x()) == 1) or \
             ((rope2.coord_y() - self.coord_y()) == -1) and ((rope2.coord_x() - self.coord_x()) == 2): 
                 self.move_down()
                 self.move_right()
        elif ((rope2.coord_y() - self.coord_y()) == -2) and ((rope2.coord_x() - self.coord_x()) == -1) or \
             ((rope2.coord_y() - self.coord_y()) == -1) and ((rope2.coord_x() - self.coord_x()) == -2): 
                 self.move_down()
                 self.move_left()
    def read_instruction(self,instruction):
        if instruction == 'U': self.move_up()
        elif instruction == 'D': self.move_down()
        elif instruction == 'L': self.move_left()
        elif instruction == 'R': self.move_right()

    
alist = [line.rstrip().split(' ') for line in open('Day9/input.txt')]
    
head = rope_end()
tail = rope_end()
coordinates = {(0,0)}
for instruction in alist:
    for times in range(0,int(instruction[1])):
        head.read_instruction(instruction[0])
        tail.follow_end(head)
        coordinates.add((tail.coord_x(),tail.coord_y()))
        
print(len(coordinates))