class Przyciski():
    is_pressed = 0
 
    def __init__(self, x, y, w):
        self.x=x # powiedziałabym ,że atrybuty mocno inspirowane moimi ;)
        self.y=y
        self.w=w
        
    def rysowanie(self):
        if self.is_pressed:
            fill(123,56,79)
        circle(self.x, self.y, self.w)
 
def setup():
    size(400,200)
    global duzy_przycisk
    global maly_przycisk
    duzy_przycisk=Przyciski(170,100, 70)
    maly_przycisk=Przyciski(50,30, 50)
 
def mouseClicked():
    if (mouseX>25 and mouseX<75 and mouseY>5 and mouseY<60):
        maly_przycisk.is_pressed = not maly_przycisk.is_pressed
 
def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            duzy_przycisk.x = duzy_przycisk.x+2
        elif keyCode == LEFT:
            duzy_przycisk.x = duzy_przycisk.x-2
        if keyCode == UP:
            duzy_przycisk.y = duzy_przycisk.y-2
        elif keyCode == DOWN:
            duzy_przycisk.y = duzy_przycisk.y+2
 
def draw():
    background(0,0,0)
    fill(255, 0, 0)
    maly_przycisk.rysowanie()
    fill(0, 255, 0)
    duzy_przycisk.rysowanie()

# większą część kodu możnaby zawrzeć w kasie jakoatrybuty klasy i metody klasy
# 1,75p
