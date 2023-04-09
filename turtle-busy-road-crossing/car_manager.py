from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_QUADRANTS = ()


# Class CarManager generates random cars and moves them across the screen.


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.old_cars = []  # a list for car objects to be reused by the program

    def create_car(self):
        # Creates a new car if no cars.
        if self.old_cars:
            new_car = self.old_cars.pop()
            print("Reusing old car")
        else:
            new_car = Turtle("square")
            print("New car")

        new_car.shapesize(stretch_wid=1, stretch_len=2)  # creates a narrow rectangle
        new_car.color(random.choice(COLORS))
        new_car.penup()

        # New cars are being generated along Y=axis, screen is 600 x 600
        rand_y = random.randint(-250, 250)
        new_car.goto(300, rand_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # Check if beyond the screen.
            if car.xcor() < -310:
                self.remove_car(car)
            car.backward(self.car_speed)

    def remove_car(self, car):
        """Transfers the car to the old_cars list so the object can be reused in the game."""
        self.all_cars.remove(car)
        self.old_cars.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

