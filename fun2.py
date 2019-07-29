##import turtle
##turtle.goto (0,0)
##def up ():
##    print ("you pressed the up key.")
##turtle.onkey (up,"Up")
##turtle.goto (0,0)
##turtle.lis
import turtle
turtle.goto (0,0)
turtle.direction = None



def on_move ():
    pos =turtle.pos ()
    x= pos [0]
    y=pos[1]
    if turtle.direction == "Up":
        turtle.goto (x , y+100)
    if turtle.direction == "Right":
        turtle.goto (x+100 , y)
    if turtle.direction == "Down":
        turtle.goto (x , y-100)
    if turtle.direction == "Left":
        turtle.goto (x-100 , y)

        
def up ():
     turtle.direction = "Up"
     on_move ()
     print ("you pressed the up key ")
turtle.onkey (up ,"Up")
turtle.listen()

def down ():
     turtle.direction = "Down"
     on_move ()
     print ("you pressed the down key ")
turtle.onkey (down ,"Down")
turtle.listen()

def left ():
     turtle.direction = "Left"
     on_move ()
     print ("you pressed the left key ")
turtle.onkey (left ,"Left")
turtle.listen()
    
def right ():
     turtle.direction = "Right"
     on_move ()
     print ("you pressed the Right key ")
turtle.onkey (right ,"Right")
turtle.listen()
        
    
        
     
