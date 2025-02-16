import turtle
import random

tom = turtle.Turtle()
turtle.colormode(255)
tom.shape('turtle')

rgb_colors = [   (37, 95, 182), (233, 164, 79), (243, 223, 87), (100, 195, 231), (213, 71, 106), (248, 52, 23),
                 (199, 71, 24), (236, 110, 145), (183, 48, 90), (144, 232, 215), (251, 137, 166), (165, 175, 232),
                 (65, 45, 14), (77, 204, 170), (82, 187, 102), (22, 155, 52), (168, 27, 9), (24, 36, 85),
                 (104, 39, 44), (252, 219, 0), (249, 150, 3), (111, 212, 247), (24, 151, 227), (253, 12, 3),
                 (37, 50, 98), (239, 165, 156), (99, 101, 183), (84, 34, 38), (65, 70, 40), (252, 9, 13), (23, 103, 34)]
random_colors = random.choice(rgb_colors)

tom.penup()
tom.goto(-250,-200)
def size(rows,columns):
    for row in range(rows):
        for column in range(columns):

            random_colors = random.choice(rgb_colors)
            tom.dot(10,random_colors)
            tom.forward(50)

        tom.goto(-250,-200+50*(row+1))
size(10,10)

my_screen = turtle.Screen()
my_screen.exitonclick()