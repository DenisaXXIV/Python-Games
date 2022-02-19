from random import randrange
from turtle import *

from freegames import square, vector

apple = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x <190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        "When the snake bites itself "
        square(head.x, head.y, 9, 'yellow')
        update()
        return
    snake.append(head)

    if head == apple:
        print('Snake:', len(snake))
        apple.x = randrange(-15, 15) * 10
        apple.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        "The color of the snake "
        square(body.x, body.y, 9, 'green')

    "Snake food color (default: red apples) "
    square(apple.x, apple.y, 9, 'red')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()