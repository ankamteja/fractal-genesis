import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
t = turtle.Turtle()
t.speed(0)
t.dot(5, "red")

def draw_triangle(length, depth):
	for i in range(3):
		
		koch(length, depth)
		t.left(120)
		if i==0:
			t.dot(5, "blue")	
		elif i==1:
			t.dot(5, "yellow")
		else:
			pass


def koch(length, depth):
	if depth == 0:
		t.forward(length)
	else:
		koch(length/3, depth-1)
		t.left(60)
		koch(length/3, depth-1)
		t.right(120)
		koch(length/3, depth-1)
		t.left(60)
		koch(length/3, depth-1)		


length = int(input("enter the len: "))
depth = int(input("enter the depth: "))
draw_triangle(length, depth)
turtle.done()
