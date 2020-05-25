# nie usuwasz, wszystko jest w historii
class Kwadrat(): 
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class KolorowyKwadrat(Kwadrat): # nazwa klasy nie powinna zawierać czasownika, od tego by coś wykonywać są metody i to one powinny być czasownikami

    def kolorowanie(self,x,y,z):
        fill(x,y,z)
     
def setup():
    size(130,260)
    kwadrat1=KolorowyKwadrat(70)
    kwadrat1.kolorowanie(34,139,34)
    kwadrat1.sketch(30,30) # metoda była niepotrzebnie powielona, bo nic nie zmieniała
    kwadrat2=KolorowyKwadrat(90)
    kwadrat2.kolorowanie(0,0,139)
    kwadrat2.sketch(20,130)
    
# 1,5pkt
