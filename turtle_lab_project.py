import turtle
import time
import random

def main():
    turtle.setup(800, 600)
    time.sleep(2)
    CollectGems()
    CrossRiver()
    EatFlower()
    BuildHouse()

def ResetTurtle():
    turtle.reset()
    turtle.penup()
    turtle.shape("classic")
def DisplayMessage(message):
    turtle.pencolor("black")
    turtle.write(message, align = "right", font = ('Arial', '16', 'bold'))
    time.sleep(3)
def DisplayMessageLeft(message):
    turtle.pencolor("red")
    turtle.write(message, align = "left", font = ('Arial', '12', 'bold'))
    time.sleep(0)
#creat a function for rhombus
def Rhombus():
    turtle.right(60)
    turtle.forward(30)
    turtle.right(80)
    turtle.forward(30)
    turtle.right(100)
    turtle.forward(30)
    turtle.right(80)
    turtle.forward(30)
    turtle.right(60)
#creat a function for Square(wall)
def Square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
#creat a function for Triangle(roof)
def Triangle():
    turtle.forward(142)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
#creat a function for Rectangle(door)
def Rectangle():
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)

# In the 1st function, it will draw 5 colorful gems in different locations
# And show turtle is collecting them as it passes by
# Here we will use list of colors for the gems.    
def CollectGems():
    ResetTurtle()
    #draw gems
    color = ["red", "MediumBlue", "gold", "aquamarine", "darkOrchid1"]
    x = [-270, -140, 30, 150, 250]
    y = [100, -10, 20, 120, -30]
    turtle.speed(0)
    for i in range(0,5):
        turtle.fillcolor(color[i])
        turtle.pensize(1)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x[i],y[i])
        turtle.pendown()
        turtle.begin_fill()
        Rhombus()
        turtle.end_fill()
    # display turtle
    #show turtle is collecting the gems as he walk by
    turtle.shape("turtle")
    turtle.fillcolor("green")
    turtle.pensize(8)
    turtle.pencolor("black")
    turtle.turtlesize(2)
    turtle.right(-90)
    #creat a new list where the turtle needs to go and collect the gems
    x = [-290, -173, -10, 100, 220]
    y = [50, -50, -20, 80, -50]
    turtle.speed(0)
    for i in range(0,5):
        #draw white circles so it will look like turtle is collecting them
        
        turtle.pensize(3) 
        turtle.fillcolor("white")
        turtle.pencolor("white")
        turtle.penup()
        turtle.goto(x[i],y[i])
        turtle.pendown()
        turtle.showturtle()
        
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        turtle.pencolor("black")
        turtle.fillcolor("green")
        time.sleep(2)
    #display the message
    DisplayMessage("Yay, I got all the gems!")

#In the 2nd function, it will swim across the river
#For which, we will use a single loop to create a river
#then make the turtle swim over it
def CrossRiver():
    ResetTurtle()
    #Move the pen
    turtle.penup()
    turtle.goto(-400, -80)
    turtle.pendown()
    #hide turtle
    turtle.hideturtle()
    #get the pencolor, pensize, and fillcolor
    turtle.fillcolor("DeepSkyblue2")
    turtle.pencolor("green3")
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.speed(0)
    # creat a single loop to display the river
    for i in range(0, 2):
        turtle.forward(800)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    turtle.delay(0)
    turtle.begin_fill
    turtle.shape("turtle")
    turtle.color("green")
    turtle.turtlesize(2)
    turtle.pensize(8)
    #move the pen
    turtle.penup()
    turtle.goto(0, -160)
    turtle.pendown()
    #display turtle
    turtle.showturtle()
    #show turtle is swiming across the river
    turtle.left(90)
    time.sleep(1)
    #waking
    turtle.pencolor("white")
    turtle.forward(27)
    time.sleep(1)
    turtle.forward(27)
    time.sleep(1)
    turtle.forward(26)
    time.sleep(1)
    #swimming
    turtle.pencolor("DeepSkyblue")
    turtle.forward(31)
    time.sleep(1)
    turtle.forward(31)
    time.sleep(1)
    turtle.forward(31)
    time.sleep(1)
    turtle.forward(31)
    time.sleep(1)
    turtle.forward(32)
    time.sleep(1)
    #walking
    turtle.pencolor("white")
    turtle.forward(30)
    time.sleep(1)
    turtle.forward(30)
    time.sleep(1)
    #display the message
    DisplayMessage("Yay! I made it to the other side!")

#In the 3rd function, turtle will eat a flower.
#First, we will create a flower then the flower will disappear as the turtle eat it.
#Here we will use a nested loop to draw the flower. 
def EatFlower():
    ResetTurtle()
    turtle.speed(0)
    turtle.hideturtle()
    #draw flower
    #creat a nested loop so the flower will look more real
    for i in range(0,3):
        x = 0
        y = 0
        turtle.fillcolor("purple")
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.begin_fill()
        for j in range(0,7):
            Rhombus() 
        turtle.end_fill()
    #make a small circle at the middle of the flower
    turtle.fillcolor("orange")
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-10,-4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    #draw a stem for the flower
    turtle.pencolor("green")
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(0, -40)
    turtle.pendown()
    turtle.right(30)
    turtle.forward(50)
    time.sleep(2)
    
    #creat list of locations where the turtle needs to go and eat the entir flower
    x = [50, 50, -15, -8, -20]
    y = [0, 10, 0, -20, 0]
    for i in range(0,5):
        #display turtle eating the flower
        turtle.showturtle()
        turtle.shape("turtle")
        #change the size of turtle
        turtle.turtlesize(3)
        turtle.fillcolor("green")
        turtle.pensize(5)
        # turn right(90) so it will look like turtle is mobving and eating
        turtle.right(90)
        turtle.penup()
        turtle.goto(x[i],y[i])
        turtle.pendown()
        #make circles so it will look like turtle is eating the flower
        turtle.fillcolor("white")
        turtle.pencolor("white")
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        turtle.pencolor("black")
        turtle.fillcolor("green")
        time.sleep(2)
    DisplayMessage("Yum! Yum!")

#Finally, for the 4th function, turtle will build a house so he can live in.
#we will use multi-alternative If structure with the input and output statement.
def BuildHouse():
    ResetTurtle()
    #Deaclare Variable
    ResetTurtle()
    choice = str()
    #hide turtle
    turtle.hideturtle()
    #move the pen and display the instructions of how to make the house
    turtle.penup()
    turtle.goto(-300, 220)
    turtle.pendown()
    DisplayMessageLeft("Instructions for building a House")

    turtle.penup()
    turtle.goto(-300, 180)
    turtle.pendown()
    DisplayMessageLeft("Build 1st:\t wall")
    
    turtle.penup()
    turtle.goto(-300, 160)
    turtle.pendown()
    DisplayMessageLeft("Build 2nd:\t door")

    turtle.penup()
    turtle.goto(-300, 140)
    turtle.pendown()
    DisplayMessageLeft("Build 3rd:\t roof")

    #creat a loop so the input statement will appear 3 times
    for i in range(0,3):
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.showturtle()
        turtle.begin_fill()
        turtle.shape("turtle")
        turtle.color("green")
        turtle.pencolor("black")
        turtle.pensize(2)
        turtle.end_fill()
        #make the turtle build "wall" 1st, "door" 2nd, and then the "roof"
        choice = str(input("What do you wanna build (wall, door, and roof)?: "))
        #use multi-alternative If structure
        if choice == "wall":
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            turtle.begin_fill()
            
            Square()
            turtle.fillcolor("burlywood")
            turtle.end_fill()
        elif choice == "door":
            
            turtle.penup()
            turtle.goto(40,0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.left(90)
            Rectangle()
            turtle.fillcolor("tan3")
            turtle.end_fill()
        elif choice == "roof":
           
            turtle.penup()
            turtle.goto(-20,100)
            turtle.pendown()
            turtle.begin_fill()
            turtle.left(90)
            Triangle()
            turtle.fillcolor("coral3")
            turtle.end_fill()
        
    #move the pen
    turtle.penup()
    turtle.goto(-20,-10)
    turtle.pendown()
    turtle.begin_fill
    turtle.shape("turtle")
    turtle.color("green")
    turtle.right(140)
    turtle.pencolor("black")
    turtle.end_fill()
    #display message
    DisplayMessage("Finally made my sweet HOME!")
main()
 
