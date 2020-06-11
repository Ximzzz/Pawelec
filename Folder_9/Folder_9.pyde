def setup():
    size(400,400)
    global zdjecie
    zdjecie = loadImage("pingwinek.JPG")
    
def draw():
    global zdjecie
    wysokoscObrysu = 400
    szerokoscObrysu = 400
    try:
        image(zdjecie,0,0, szerokoscObrysu, wysokoscObrysu)
        stroke(0,0,255)
    except:
        fill(0,0,0)
        textSize(26)
        fill(123,104,238)
        text("Nie znaleziono obrazka", 50, 200)
        stroke(255, 0, 0)
    noFill()
    strokeWeight(8)
    rect(0, 0, szerokoscObrysu, wysokoscObrysu)
