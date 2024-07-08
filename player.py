import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.setposition(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reached_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.setposition(STARTING_POSITION)
