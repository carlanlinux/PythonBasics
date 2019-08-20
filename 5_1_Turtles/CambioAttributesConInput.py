import turtle

bgclor = input("Indique el color de ventana deseado")
wn = turtle.Screen()
wn.bgcolor(bgclor)

tess = turtle.Turtle()
tess.forward(100)
tesscolor = input("Indoque el color deseado de la tortuga")
tess.color(tesscolor)
tess.left(90)
tess.forward(45)
pensize = int(input("Introducir el tamaño del lápiz"))
tess.pensize(pensize)
tess.right(90)
tess.forward(100)

wn.exitonclick()