from turtle import Turtle
import turtle
class Ball(Turtle):
	def __init__(self,radius,color,dx,dy):
		Turtle.__init__(self)
		self.radius = radius
		self.color = color
		self.dx = dx
		self.dy = dy
		self.penup()
		self.shape('circle')
		self.shapesize(10)
	def move(self,screen_width,screen_height):
		current_x = self.dx
		new_x = current_x + dx
		current_y = self.yx
		new_y = current_y + dy
		right_side_ball = new_x + radius
		left_side_ball= new_x - radius
		top_side_ball = new_y + radius
		bottom_side_ball = new_y - radius
		x = [right_side_ball,left_side_ball]
		y = [top_side_ball,bottom_side_ball]
		self.goto(x,y)
		ball_sides = [right_side_ball,left_side_ball,top_side_ball,bottom_side_ball]
		if ball_sides> screen_width and screen_height:
			self.backward()
		screen_width = turtle.canvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2


ball1= Ball(1,'yellow',2,0)
print(ball1)
