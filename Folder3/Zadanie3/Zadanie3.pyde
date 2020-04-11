def setup():
    size(480,150)
    background(0,0,0) # wystarczy zadeklarować te rzeczy raz, nie ma potrzeby co klatkę
    textSize(100)
    
def draw():
    if (mouseX > 110 and mouseX < 150 and mouseY > 30 and mouseY < 100):
        fill(255,0,0) 
        text("R", 100, 100)
    
    else:
        if ((keyPressed) and (keyCode == LEFT)):
            fill(0,0,139) 
            text("R", 100,100)    
        else:
            fill(255,255,224) 
            text("R", 100,100)           
    
    
    if ((keyPressed) and ((key == 'p') or (key == 'P'))):   
        fill(255,255,0)
        text("P", 300, 100)                                    
    else:   
        if ((keyPressed) and (keyCode == RIGHT)):
            fill(255,0,255) 
            text("P", 300, 100)                
        else:
            fill(255,255,224) 
            text("P", 300, 100)
            
    fill(0)
    line(100, 110, 170, 110) # linia jest kształtem standardowym, liczyłam na coś ciekawszego ;)
    stroke(0,0,128)
    line(300, 110, 370, 110)
    stroke(0,255,0)
    
#litery reagują na strzałki rónież gdy nic nie jest zaznaczone
#1,5p
