def setup():
    size(400,400)
    global zdjecie
    zdjecie = loadImage("pingwinek.JPG")
    strokeWeight(8)
    
def draw():
    global zdjecie
    wysokoscObrysu = 400
    szerokoscObrysu = 400
    try:
        image(zdjecie,0,0, szerokoscObrysu, wysokoscObrysu) # tylko tą część sprawdzamy pod kątem błędu
    except:
        fill(0,0,0)
        textSize(26)
        fill(123,104,238)
        text("Nie znaleziono obrazka", 50, 200)
        stroke(255, 0, 0)
    else:
        stroke(0,0,255)
    finally:
        noFill()
        rect(0, 0, szerokoscObrysu, wysokoscObrysu)
        
#1,5pkt
