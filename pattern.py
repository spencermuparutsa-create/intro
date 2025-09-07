import pgzrun

WIDTH = 700
HEIGHT = 700

def draw():
    screen.fill("green")
    w = 699
    h = 200
    for i in range(100):
        r = Rect((350,350),(w,h))
        r.center = 350,350
        screen.draw.rect(r,"black")
        w = w - 3
        h = h + 3

pgzrun.go()