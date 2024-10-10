from turtle import * 
# მივეცი მაქსიმალური სიჩქარე

speed(0)

# მივეცი ფუნჯს სიგრძე

width(8) 

# ვხაზავთ სახლისთვის კუბს
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)

# ჩვენი ფუნჯი გადაგვაქ კარის დასახაზ ადგილას

penup()
goto(130, 0)
pendown()

# ვხაზავთ კარს
color("blue")
begin_fill()
left(180)
forward(100)

left(90)
forward(50)

left(90)
forward(100)
end_fill()
# გადაგვაქ ფუნჯი ფანჯრების დასახაზად

penup()
goto(180, 180)
pendown()

# ვხაზავთ პირველ ფანჯარას

color("pink")
begin_fill()
right(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
left(90)
forward(40)

end_fill()

# გადამაქ ფუნჯი მეორე ფანჯრის დასახაზად

penup()
goto(20, 180)
pendown()

# ვხაზავ მეორე ფანჯარას
begin_fill()
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()
# გადამაქ ფუნჯი სახურავის დასახაზად

penup()
goto(200, 200)
pendown()

# ვიწყებ სახურავის ხაზვას
color("orange")
begin_fill()
left(135)
forward(140)

left(90)
forward(140)
end_fill()


exitonclick()