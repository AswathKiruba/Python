import turtle

def draw_square(some):

    for i in range(1,5):    
        some.forward(100)
        some.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(2)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    
    window.exitonclick()

    
draw_art()
