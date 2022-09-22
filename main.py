from turtle import Turtle, Screen

johnny = Turtle()
screen = Screen()


def move_forwards():
    johnny.forward(20)


def move_backwards():
    johnny.backward(20)


def turn_left():
    johnny.left(30)


def turn_right():
    johnny.right(30)

def clear_screen(x, y):
    johnny.clear() # erase all drawings made with that turtle
    johnny.pu()
    johnny.home() # moves the turtle to the origin coordinates 0,0 unless otherwise changed\
    johnny.pd()


screen.listen() # 1.activating listening to events to control the screen
screen.onclick(clear_screen) ###2a. activating a listener: "onclick()" method to register function draw to the event mouse click
screen.onkey(screen.bye, "q") # 2b. activating a listener: "onkey()" method to register function exit to event "q" key press
screen.onkey(key="w", fun=move_forwards) # 2c. activating a listener: "onkey()" method that needs to be bound to a function
                                        #i dont add () after name of function inside a listener method, or it'd be triggered there and then
screen.onkey(key="s", fun=move_backwards) # OR: screen.onkey(move_backwards, "s")
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.mainloop()
#screen.exitonclick()
