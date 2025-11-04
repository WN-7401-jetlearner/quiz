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
qbox=Rect(0,100,550,150)
opt1=Rect(0,250,250,90)
opt2=Rect(300,250,250,90)
opt3=Rect(0,350,250,90)
opt4=Rect(300,350,250,90)
marquee_box=Rect((0,0),(700,100))
T=Rect(580,100,90,90)
marquee_message="welcome to the quiz"
sbox=Rect(580,250 ,100,190)

def move():
    marquee_box.x+=-5
    if marquee_box.right<0:
        marquee_box.left=700

def update():
    move()





def draw():
    screen.fill(BLACK)
    screen.draw.filled_rect(marquee_box,"WHITE")
    screen.draw.filled_rect(qbox,"  BLUE")
    screen.draw.filled_rect(opt1,"ORANGE")
    screen.draw.filled_rect(opt2,"PINK")
    screen.draw.filled_rect(opt3,"PURPLE")
    screen.draw.filled_rect(opt4,"Yellow")
    screen.draw.filled_rect(sbox,"RED")
    screen.draw.filled_rect(T,"GREEN")
    screen.draw.textbox("SKIP ME",sbox,color="BLACK")
    
#trectangleeeeeeee
    #textboxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    screen.draw.textbox(marquee_message,marquee_box,color=BLACK)
    #screen.draw.filled_rect(,BLUE)
    



pgzrun.go()