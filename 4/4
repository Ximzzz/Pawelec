import random
add_library('pdf')

def setup():
    global img
    global img2
    global img3
    global img4
    global img5
    size(400,520)
    img=loadImage("https://fotokrzyki.pl/wp-content/uploads/2018/01/zdjecie-do-dowodu-osobistego.jpg")
    img2= loadShape("https://upload.wikimedia.org/wikipedia/commons/9/9d/Sunglasses_%28example%29.svg")
    img3= loadShape("https://upload.wikimedia.org/wikipedia/commons/4/43/Mostacho.svg")
    img4= loadShape("https://upload.wikimedia.org/wikipedia/commons/4/47/Make_America_Great_Again_%28MAGA%29_hat.svg")
    img5= loadShape ("https://upload.wikimedia.org/wikipedia/commons/d/d0/Emoji_u1f576.svg")
    beginRecord(PDF, "zdjecie.pdf")
    
def draw():
    image(img, 0,0) 

    if (mouseX>10 and mouseX<50 and mouseY>10 and mouseY<50):
        fill(255,255,0)
        r1=rect(10,10,40,40)
        shape(img2,80, 235, 255, 90)
        shape(img3,130, 355, 155, 45)
    else:
        fill(255,255,224) 
        r1=rect(10,10,40,40)
    
    if (mouseX>345 and mouseX<385 and mouseY>10 and mouseY<50):
        fill(0,0,255)
        r2=rect(345,10,40,40)
        shape(img4,35,0,340,180)
        shape(img5,70, 145, 280, 260)
    else:
        fill(100,149,237) 
        r2=rect(345,10,40,40)
    
    if mousePressed:
        fill(255,255,255)
        noStroke()
        r1=rect(10,10,40,40)
        r2=rect(345,10,40,40)
              
def mouseClicked(r1):
    endRecord()
    exit()

def mouseClicked(r2):
    endRecord()
    exit()    
    
    #Nie wiem jak to będzie wyglądało u Pani w związku z tworzeniem się pdf-u. U mnie lokalnie, plik tworzył się 
    #w folderze, w którym zapisywał się cały program. Mam nadzieję, że wszystko zadziała poprawnie.  
