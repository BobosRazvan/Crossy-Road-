import turtle


class Car(turtle.Turtle):

    def __init__(self, color, x_position,y_position):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.penup()
        self.color(color)
        self.left(180)
        self.setposition(x_position,y_position)


    def move(self,car_speed):
        self.forward(car_speed)
