import turtle
import car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed=10
        for _ in range(3):
            self.generate_new_car()

    def generate_new_car(self):
        color = random.choice(COLORS)
        y_position = random.randint(-250, 250)
        x_position = random.randint(270, 290)
        new_car = car.Car(color,x_position, y_position)
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.move(self.car_speed)

    def check_if_made_contact(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:
                return True
        return False
