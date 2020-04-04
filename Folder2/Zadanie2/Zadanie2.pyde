def setup():
    global b
    b=40    
    global y, x
    global kieruneky, kierunekx
    kieruneky=1
    kierunekx=1
    size(400,400)
    frameRate(90)
    global slownik_kolorow 
    slownik_kolorow ={"żółty":(255,255,0), "niebieski":(30,144,255)}
    rectMode(CENTER)
    x=20
    y=200
    
def draw():
    global x,y,kierunekx,kieruneky                        
    background(10)
    x=x+kierunekx 
    y=y+kieruneky 
    if (x>width-(b/2) or x<b/2):
        kierunekx *=-1
        fill(*slownik_kolorow["żółty"])
    if (y>height-(b/2) or y<b/2):
        kieruneky *=-1
        fill(*slownik_kolorow["niebieski"])
    rect(x,y,b,b)
    if mousePressed:
        exit()
