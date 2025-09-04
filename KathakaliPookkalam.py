#Pookkalam design with Kathakali
import turtle
import math

#Setup
W = 1000
screen = turtle.Screen()
screen.setup(W, W)
screen.title("Code a Pookkalam - Kathakali Edition")
screen.bgcolor("white")
t = turtle.Turtle(visible=False)
t.speed(0)
turtle.colormode(255)

def move(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def circle_at(cx, cy, r, fill=None, outline=None, pensize=1):
    if outline is not None:
        t.pencolor(outline)
    t.pensize(pensize)
    if fill is not None:
        t.fillcolor(fill); t.begin_fill()
    move(cx, cy - r)
    t.setheading(0)
    t.circle(r)
    if fill is not None:
        t.end_fill()

def poly(points, fill=None, outline=None, pensize=1):
    if outline is not None:
        t.pencolor(outline)
    t.pensize(pensize)
    if fill is not None:
        t.fillcolor(fill); t.begin_fill()
    move(points[0][0], points[0][1])
    for x, y in points[1:]:
        t.goto(x, y)
    t.goto(points[0][0], points[0][1])
    if fill is not None:
        t.end_fill()

def ring_star_zig(radius_outer, radius_inner, spikes, palette):
    step = 360 / spikes
    for band, col in enumerate(palette):
        r1 = radius_outer - band * 22
        r2 = r1 - 18
        pts = []
        ang = 0
        for i in range(spikes):
            a1 = math.radians(ang)
            a2 = math.radians(ang + step/2)
            a3 = math.radians(ang + step)
            pts.append((r1*math.cos(a1), r1*math.sin(a1)))
            pts.append((r2*math.cos(a2), r2*math.sin(a2)))
            pts.append((r1*math.cos(a3), r1*math.sin(a3)))
            ang += step
        poly(pts, fill=col, outline=col)

    circle_at(0, 0, radius_inner, fill="lavender", outline="black")

def petal_ring(r_base, petal_len, petals, color):
    step = 360 / petals
    for i in range(petals):
        a = math.radians(i * step)
        aL = math.radians(i * step + step/2)
        base = (r_base*math.cos(a), r_base*math.sin(a))
        tip = ((r_base+petal_len)*math.cos(aL), (r_base+petal_len)*math.sin(aL))
        a2 = math.radians((i+1)*step)
        base2 = (r_base*math.cos(a2), r_base*math.sin(a2))
        poly([base, tip, base2], fill=color, outline=color)

def leaf_ring(r, leaves, leaf_len, leaf_w, color):
    step = 360 / leaves
    for i in range(leaves):
        a = math.radians(i * step)
        c = (r*math.cos(a), r*math.sin(a))
        a2 = a + math.radians(step/2)
        tip = ((r+leaf_len)*math.cos(a2), (r+leaf_len)*math.sin(a2))
        left = ((r+leaf_w)*math.cos(a2+0.25), (r+leaf_w)*math.sin(a2+0.25))
        right = ((r+leaf_w)*math.cos(a2-0.25), (r+leaf_w)*math.sin(a2-0.25))
        poly([c, left, tip, right], fill=color, outline=color)

def torch_ring(r, count, shaft, flame, shaft_color=(120,50,40)):
    step = 360 / count
    for i in range(count):
        a = math.radians(i * step)
        base = (r*math.cos(a), r*math.sin(a))
        mid = ((r+shaft)*math.cos(a), (r+shaft)*math.sin(a))
        poly([
            (base[0]-6*math.sin(a), base[1]+6*math.cos(a)),
            (base[0]+6*math.sin(a), base[1]-6*math.cos(a)),
            (mid[0]+4*math.sin(a), mid[1]-4*math.cos(a)),
            (mid[0]-4*math.sin(a), mid[1]+4*math.cos(a))
        ], fill=shaft_color, outline=shaft_color)
        flame_base = ((r+shaft+6)*math.cos(a), (r+shaft+6)*math.sin(a))
        flame_tip = ((r+shaft+flame)*math.cos(a), (r+shaft+flame)*math.sin(a))
        poly([flame_base,
              ((flame_base[0]+flame_tip[0])/2, (flame_base[1]+flame_tip[1])/2 + 8),
              flame_tip],
             fill=(255,140,0), outline=(255,140,0))
        poly([((flame_base[0]+flame_tip[0])/2, (flame_base[1]+flame_tip[1])/2 + 2),
              ((flame_base[0]+flame_tip[0])/2, (flame_base[1]+flame_tip[1])/2 + 12),
              (flame_tip[0], flame_tip[1]-2)],
             fill=(255,220,80), outline=(255,220,80))
        circle_at(flame_tip[0], flame_tip[1], 4, fill="white", outline="white")

# Base disc
circle_at(0, 0, 380, fill="#B7410E", outline="#B7410E")

#Outer Bands
palette = [
    (180, 30, 30),
    (255, 90, 0),
    (255, 170, 30),
    (255, 255, 255),
    (80, 110, 210),
    (30, 40, 60),
]
ring_star_zig(radius_outer=355, radius_inner=225, spikes=24, palette=palette)

circle_at(0, 0, 220, fill=(120, 60, 160), outline=(120, 60, 160))
leaf_ring(r=230, leaves=12, leaf_len=18, leaf_w=10, color=(40,120,40))
torch_ring(r=255, count=12, shaft=38, flame=26)
circle_at(0, 0, 210, fill="coral", outline="coral")
petal_ring(r_base=120, petal_len=70, petals=16, color=(200, 40, 50))
circle_at(0, 0, 110, fill="gold", outline="gold")

#Kathakali face
FACE_YSHIFT = -25
def adj(y): return y + FACE_YSHIFT

#Face base
poly([(-55, adj(-10)), (55, adj(-10)), (55, adj(55)), (35, adj(70)), (-35, adj(70)), (-55, adj(55))],
     fill=(40, 140, 70), outline=(0, 80, 40))

#Face cheeks
circle_at(-40, adj(10), 18, fill=(50,150,70), outline=(0,80,40))
circle_at( 40, adj(10), 18, fill=(50,150,70), outline=(0,80,40))

#Face chin
poly([(-20,adj(-10)),(0,adj(-25)),(20,adj(-10)),(0,adj(0))],
     fill=(30,120,60), outline=(0,80,40))

#Eyes
poly([(-32,adj(36)),(-14,adj(28)),(-10,adj(34)),(-28,adj(44))],
     fill=(0,70,120), outline=(0,50,90))
poly([( 32,adj(36)),( 14,adj(28)),( 10,adj(34)),( 28,adj(44))],
     fill=(0,70,120), outline=(0,50,90))
circle_at(-22, adj(35), 4, fill="black", outline="black")
circle_at( 22, adj(35), 4, fill="black", outline="black")

#Nose
poly([(-8,adj(18)),(0,adj(10)),(8,adj(18)),(0,adj(26))],
     fill=(0,100,50), outline=(0,80,40))

#Mouth
poly([(-16,adj(0)),(-6,adj(-4)),(6,adj(-4)),(16,adj(0)),(4,adj(6)),(-4,adj(6))],
     fill=(200, 20, 40), outline=(120,0,0))
circle_at(-7,adj(1),1.5, fill="white", outline="white")
circle_at( 7,adj(1),1.5, fill="white", outline="white")

#Forehead bands
poly([(-70,adj(70)),(70,adj(70)),(70,adj(76)),(-70,adj(76))],
     fill=(255,255,255), outline=(200,200,200))
poly([(-70,adj(76)),(70,adj(76)),(70,adj(82)),(-70,adj(82))],
     fill=(230,60,60), outline=(180,30,30))
poly([(-70,adj(82)),(70,adj(82)),(70,adj(88)),(-70,adj(88))],
     fill=(255,230,70), outline=(200,160,40))

#Crown layers
poly([(-70,adj(70)),(70,adj(70)),(70,adj(80)),(-70,adj(80))],
     fill=(230,60,60), outline=(180,30,30))
poly([(-60,adj(80)),(60,adj(80)),(60,adj(90)),(-60,adj(90))],
     fill=(255,230,70), outline=(200,160,40))
poly([(-50,adj(90)),(50,adj(90)),(50,adj(100)),(-50,adj(100))],
     fill=(120,60,160), outline=(80,40,120))

#Crest
poly([(-20,adj(100)),(0,adj(118)),(20,adj(100))],
     fill=(255,90,0), outline=(160,50,0))
poly([(-32,adj(100)),(-6,adj(110)),(-20,adj(96))],
     fill=(255,255,255), outline=(180,180,180))
poly([( 32,adj(100)),( 6,adj(110)),( 20,adj(96))],
     fill=(255,255,255), outline=(180,180,180))

#Happy Onam text
t.penup()
t.goto(0, -83)   
t.color((183, 65, 14))  
t.write("ഓണാശംസകൾ", align="center", font=("Karthika", 11, "bold"))
t.pendown()

t.hideturtle()
turtle.done()