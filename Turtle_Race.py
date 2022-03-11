from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
puntata = screen.textinput(title = "Puntata", prompt="Scegli il colore della tartaruga: ")
colori = ["red", "green", "purple","yellow", "blue", "magenta"]
pos_y = [0, -25, -50, 25, 50, 75]

turtles = []
for num in range(6):
    t = Turtle(shape = "turtle")
    t.color(colori[num])
    t.penup()
    t.speed(3)
    t.goto(x = -240, y = pos_y[num])
    turtles.append(t)

def game_over(turtlewin):
    fine = Turtle()
    fine.penup()
    fine.hideturtle()
    tw = ""
    cont = 0
    for singleturtlewin in turtlewin:
        if cont % 2 == 0 and len(turtlewin) > 1:
            tw += "\n"
        cont += 1
        tw += f"{singleturtlewin.pencolor()}" + " " 
    fine.write(f"GAME OVER \n The {tw} turtle has won", align = 'center' , font = ('Times New Roman', 20, 'normal'))
    
def win(turtlewin):
    vinto = Turtle()
    vinto.penup()
    vinto.hideturtle() 
    tw = ""
    cont = 0
    for singleturtlewin in turtlewin:
        if cont % 2 == 0:
            tw += "\n"
        cont += 1
        tw += f"{singleturtlewin.pencolor()}" + " " 
    vinto.write(f"WINNER \n You win! \n The winner is {tw} turtle", align = 'center' , font = ('Times New Roman', 20, 'normal'))

start = True
while start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            turtlewin = []
            for turtle2 in turtles:
                if turtle.xcor() == turtle2.xcor():
                    turtlewin.append(turtle2)
            start = False
            if len(turtlewin) == 1:
                if puntata == turtle.pencolor():
                    print (f"Hai vinto! ha vinto il colore {turtle.pencolor()}")
                    win(turtlewin)
                else:
                    print(f"Hai perso! ha vinto il colore {turtle.pencolor()}")
                    game_over(turtlewin)
                break
            else:
                iswin = False
                for singleturtlewin in turtlewin:
                    if puntata == singleturtlewin.pencolor():
                        iswin = True
                        print (f"Hai vinto ma hanno vinto insieme a te anche le tartarughe ")
                for singleturtlewin in turtlewin:
                    print(f"{singleturtlewin.pencolor()}")
                if iswin:
                    win(turtlewin)
                else:
                    game_over(turtlewin)
                break
        turtle.forward(randint(0,10))
        

screen.exitonclick()    