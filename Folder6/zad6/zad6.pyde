class Kwadrat(): # bez edytowania istniejącej części, ale jeśli uznasz to za zasadne, możesz coś dopisać
    def __init__(self, bok):
        self.bok = bok
    def rysowanie(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class Kwadrat1(Kwadrat):
    def rysuj(self): # nie używajcie nazw wbudowanych metod
        self.rysowanie(30,30) # to nie wnosi żadnej funkcjonalności, jedynie wywołuje metodę z klasy wyżej... co podsumowując w tej postaci jest bez sensu

class Kwadrat2(Kwadrat): # wygląda tak samo jak ta wyżej, a więc nie jest zasadne jej wydzielanie, to można osiągnąć przez wywołanie metody rysuj na obiekcie, nie trzeba do tego dodatkowych klas,a wręcz utrudniają, klasa ma być przepisem na typ obiektu, po co nam dwa razy taki sam przepis o różńej nazwie? kilka ciast z tego przepisu ma sens...
    def rysuj(self):
        self.rysowanie(20,130) # wywołanie z argumentami na sztywno uniemożliwia tworzenie większej ilości obiektów tej klasy (odnosząc się do analogii z ciastami, nie można stworzyć więcej niż jednego ciasta z tego przepisu)
        
def setup():
    size(130,260)
    fill(34,139,34) # jeśli chcesz aby były kolorowe, to może stwórz taką metodę w klasie KolorowyKwadrat ? to jeden z pomysłów...
    kwadrat1=Kwadrat1(70)
    kwadrat1.rysuj()
    fill(0,0,139)
    kwadrat2=Kwadrat2(90)
    kwadrat2.rysuj()
    
# w tej postaci 0,5pkt, masz jeszcze czas poprawić
