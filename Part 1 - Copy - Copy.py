import turtle

window = turtle.Screen()
window.colormode(255)
window.bgcolor("black")

gay = turtle.Turtle()
gay.speed(0)

r = 255
b = 255
g = 0

for i in range(1000):
    gay.color(r, g, b)
    gay.forward(i * 2)
    gay.right(121)
    r = r - 1
    b = b - 1
    g = g + 1


    
turtle.done()
