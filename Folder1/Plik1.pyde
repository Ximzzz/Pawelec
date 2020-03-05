def setup():
    size(400,600)
    point(50,100)
    rectMode(CORNERS)
def draw():
    print(mouseX,mouseY,mousePressed)
    rect(width/2,height/2,300,400)
    rect(width/2,height/2,50,50)
    if mousePressed:
       circle(200,200,200)
       line(mouseY,mouseX,mouseX,mouseY)
