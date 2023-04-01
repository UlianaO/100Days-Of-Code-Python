# This project is for Turtle GUI practice.
# Turtle documentation: https://docs.python.org/3/library/turtle.html
# Python packages: https://pypi.org/

import turtle as t
import random
import colorgram  # to extract RGB values from images

title_turtle = t.Turtle()
tommy = t.Turtle()
my_screen = t.Screen()
directions = [0, 90, 180, 270]
tommy.shape("turtle")
tommy.color("aquamarine4")

# Per documentation, the module(not the object) colorcode has to be modified to use RGB.
t.colormode(255)


def random_color():
    """ Returns a tuple of RGB: (0, 239, 255) """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color

#
# # Drawing shapes on top of each other
# title_turtle.penup()
# title_turtle.hideturtle()
# title_turtle.goto(0.0, 250.0)
# title_turtle.write("Drawing Shapes", align="center", font=("Cooper Black", 15, "italic"))
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tommy.forward(100)
#         tommy.right(angle)
#
# for shape_sides_num in range(3, 11):
#     tommy.color(random_color())
#     draw_shape(shape_sides_num)
#
# # ******************************************************************************************** #
#
# # Drawing a Random Walk
# title_turtle.penup()
# title_turtle.hideturtle()
# title_turtle.goto(-100.0, -250.0)
# title_turtle.write("Drawing a Random Walk", align="center", font=("Cooper Black", 15, "italic"))
# tommy.speed("fastest")
# for _ in range(200):
#     tommy.pensize(10)
#     tommy.forward(50)
#     tommy.setheading(random.choice(directions))
#     tommy.color(random_color())
#
# # ******************************************************************************************** #
#
# # Draw a Spirograph
# title_turtle.penup()
# title_turtle.hideturtle()
# title_turtle.goto(0.0, 250.0)
# title_turtle.write("Drawing a Spirograph", align="center", font=("Cooper Black", 15, "italic"))
#
# # only do one full cycle - so 360/10 = 36 circles)
# gap_size = 10
# for _ in range(int(360/gap_size)):
#     tommy.color(random_color())
#     tommy.speed("fastest")
#     tommy.circle(100)
#     current_heading = tommy.heading()
#     tommy.setheading(current_heading + gap_size)


# Extract RGB values from Images using 'colorgram' package
colors_from_image = []


def get_img_colors(image):
    """ Takes in a path/name to the image from which colors are to be extracted.
    Returns a list of colors in RGB param --> [(x,y,z), (x1,y1,z1), ..)]"""
    colors = colorgram.extract(image, 100)
    # To use with turtle object, need a format: [(x,y,z), (x1,y1,z1), ..)]
    for color in colors:
        # print(rgb_colors) # gives [Rgb(r=208, g=151, b=119)]
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        colors_from_image.append(new_color)
    return colors_from_image


# Drawing A MILLION DOLLAR PAINTING FROM DOTS

tommy.penup()
tommy.speed("fastest")
total_dots = 100
color_schema = get_img_colors('sunset.jpg')
tommy.setheading(220)
tommy.forward(400)
tommy.setheading(0)

# Dot_count for creating a square shape.
for dot_count in range(1, total_dots+1):
    tommy.pendown()
    tommy.dot(20, random.choice(color_schema))
    tommy.penup()
    tommy.forward(50)

# Every 10 dots, go up 50 paces.
    if dot_count % 10 == 0:
        tommy.setheading(90)
        tommy.forward(50)
        tommy.setheading(180)
        tommy.forward(500)
        tommy.setheading(0)

# Manipulate the GUI screen.
my_screen.exitonclick()
