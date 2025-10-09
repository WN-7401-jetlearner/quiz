import pgzrun

WIDTH =700
HEIGHT = 600

# Colours
WHITE = (238,232,240)
BLUE = (0,0,200)
DARKBLUE = ( 0,0, 97)
ORANGE = (0,250, 130)
GREEN = ( 0,180, 0)
BLACK=(0,0,0)
marquee_box=Rect((0,0),(700,100))
marquee_message="welcome to the quiz"

def move():
    marquee_box.x+=-5
    if marquee_box.right<0:
        marquee_box.left=700
def update():
    move()





def draw():
    screen.fill(BLACK)
    screen.draw.filled_rect(marquee_box,"WHITE")
#trectangleeeeeeee
    #textboxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    screen.draw.textbox(marquee_message,marquee_box,color=BLACK)



pgzrun.go()