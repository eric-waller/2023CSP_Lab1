# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()
lines.speed(0)

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()

# begin x = -490  begin y = -300
# Code for 80 point version goes here
def v80(begin_x, begin_y):
   start_x = begin_x
   start_y = begin_y
   lines.penup()
   lines.goto(start_x, start_y)
   lines.pendown()
   end_x = start_x + 980
   end_y = start_y + 10
   for line in range(32):
       lines.goto(end_x, end_y)
       lines.goto(start_x, start_y)
       start_x += 30
       end_y += 20
       lines.goto(start_x, start_y)




# Code for the 90 point version goes here
def v90(begin_x, begin_y):
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80(begin_x, begin_y)
    start_x = begin_x + 980
    start_y = begin_y
    lines.goto(start_x, start_y)
    end_x = start_x - 980
    end_y = start_y + 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x -= 30
        end_y += 20
        lines.goto(start_x, start_y)




# Code for the 100 point version here
def v100(begin_x, begin_y):
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90(begin_x, begin_y)
    start_x = begin_x
    start_y = begin_y + 630
    lines.goto(start_x, start_y)
    end_x = start_x + 980
    end_y = start_y - 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x += 30
        end_y -= 20
        lines.goto(start_x, start_y)
    start_x = begin_x + 980
    start_y = begin_y + 630
    lines.goto(start_x, start_y)
    end_x = start_x - 980
    end_y = start_y - 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x -= 30
        end_y -= 20
        lines.goto(start_x, start_y)





# Code for the 110 point version here
def v110(begin_x, begin_y):
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100(begin_x, begin_y)
    start_x = begin_x + 200
    start_y = begin_y + 200
    lines.penup()
    lines.goto(start_x, start_y)
    lines.pendown()
    end_x = start_x + 580
    end_y = start_y + 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x += 18
        end_y += 7
        lines.goto(start_x, start_y)
    start_x = begin_x + 780
    start_y = begin_y + 200
    lines.goto(start_x, start_y)
    end_x = start_x - 580
    end_y = start_y + 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x -= 18
        end_y += 7
        lines.goto(start_x, start_y)
    start_x = begin_x + 200
    start_y = begin_y + 430
    lines.goto(start_x, start_y)
    end_x = start_x + 580
    end_y = start_y - 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x += 18
        end_y -= 7
        lines.goto(start_x, start_y)
    start_x = begin_x + 780
    start_y = begin_y + 430
    lines.goto(start_x, start_y)
    end_x = start_x - 580
    end_y = start_y - 10
    for line in range(32):
        lines.goto(end_x, end_y)
        lines.goto(start_x, start_y)
        start_x -= 18
        end_y -= 7
        lines.goto(start_x, start_y)



setupScreen()
setupBox()
v110(-490, -300)





wn.mainloop()