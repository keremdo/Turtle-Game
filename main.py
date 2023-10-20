import time
import turtle
import random

FONT = ('Arial',30,'normal')
FONT2 = ('Arial',25,'normal')
gameScreen = turtle.Screen()
gameScreen.bgcolor("#CDFAD5")
gameScreen.title("Catch Game")
top_heigh = gameScreen.window_height()

score = 0
TimerNote = 5

# score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.color("#132043")
y = top_heigh * 0.85 / 2
score_turtle.setpos(0, y)

score_turtle.write(arg=f"SCORE : {score}", move=False, align="center", font=FONT)

# time turtle
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.color("#132043")
y = top_heigh * 0.75 / 2
time_turtle.setpos(0, y)
time_turtle.write(arg=f"TIME : {TimerNote}", move=False, align="center", font=FONT2)

def timerFun():
    global score_turtle
    global score
    global TimerNote
    global time_turtle
    while TimerNote > 0:
        time.sleep(1)
        TimerNote -= 1
        time_turtle.clear()
        time_turtle.write(arg=f"TIME : {TimerNote}", move=False, align="center", font=FONT2)
        if TimerNote == 0:
            time_turtle.clear()
            time_turtle.write(arg="TIME : Game Over", move=False, align="center", font=FONT2)
            score_turtle.clear()
            score_turtle.write(arg="SCORE: 0", move=False, align="center", font=FONT)


# catch_turtle turtle
catch_turtle = turtle.Turtle()
catch_turtle.penup()
catch_turtle.color("#132043")
catch_turtle.shape("turtle")

def handleClick(x,y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(arg=f"SCORE: {score}", move=False, align="center", font=FONT)
    #print(x, y)

catch_turtle.onclick(handleClick)

def set_turtle_position():
    x = random.randrange(-300, 270)
    y = random.randrange(-300, 270)
    catch_turtle.goto(x, y)
    gameScreen.ontimer(set_turtle_position, 5000)




def game_starting():
    set_turtle_position()
    timerFun()
    gameScreen.mainloop()


game_starting()

turtle.mainloop()