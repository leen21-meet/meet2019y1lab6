##import turtle
##num_pts = 5
##for i in range(num_pts):
##    turtle.left (360/num_pts)
##    turtle.forward (100)
##turtle.mainloop



##n=10
##result =[]
##for count in range(1,n):
##    if count % 3==0 :
##        result.append ('fizz')
##    else :
##        result.append(count)
##print (result)



##import turtle
##turtle.tracer(1)
##rounds = 10
##size = 10
##mike = turtle.clone()
##steve = turtle.clone()
##turtle.bgcolor("white")
##turtle.hideturtle()
##mike.color("gold")
##steve.color("blue")
##steve.goto(5,5)
##while True:
##    mike.forward(size)
##    mike.left(90)
##    steve.forward(-size)
##    steve.left(-90)
##    size += 10
##turtle.mainloop()



hour = 60
time =0
while hour <100000 :
    hour = hour +60
    time = time +1
the_days = time%24
print (the_days)

