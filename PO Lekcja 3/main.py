'''
1. Dodaj do klasy Punkt statyczną metodę distance, która oblicza długość odcinka łączą-
cego dwa punkty będące argumentami tej metody. W funkcji main utwórz obiekt klasy
Punkt oraz obiekt klasy NazwanyPunkt, a następnie wypisz rezultat wywołania metody
distance dla tych obiektów.
'''
# import math
# class punkt():
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#
#
# def odleglosc(p1x, p1y, p2x, p2y):
#     wx = p1x - p2x
#     wy = p1y - p2y
#     wynik = math.sqrt((wx)**2 + (wy)**2)
#     return wynik
#
#
#
# punkt1 = punkt(1,2)
# punkt2 = punkt(4,3)
# punkt3 = punkt(4,6)
#
# print(odleglosc(punkt1.x,punkt1.y,punkt3.x,punkt3.y))

'''
2. Zaimplementuj klasę Adres. Adres zawiera numer domu, ulicę, opcjonalnie numer miesz-
kania, miasto i kod pocztowy. Zdefiniuj inicjalizator tak, aby obiekt mógł zostać utworzony

na jeden z dwóch sposobów: z numerem mieszkania lub bez niego. Dostarcz metodę show,

która wypisuje adres z ulicą w jednym wierszu oraz kodem pocztowym i miastem w następ-
nej linii. Dostarcz metodę comes_before(self, other), która sprawdza, czy dany

adres jest przed innym, gdy porównujemy go według kodu pocztowego
'''
class adres:
    def __init__(self,numerdomu: int, ulica:str, miasto:str, kodpocztowy:str, numermieszkania=None):
        self.nr_domu = numerdomu
        self.ulica = ulica
        self.miasto = miasto
        self.kodpocztowy = kodpocztowy
        if numermieszkania is not None:
            self.nr_mieszkania = numermieszkania

def show(adres):
    print(adres.ulica, adres.nr_domu)
    print(adres.kodpocztowy, adres.miasto)

def czywczesniej(adresnr1,adresnr2):



adres1 = adres(4,"Matusa","Ciechanów","06-400", 5)
adres2 = adres(6,"Matusasusa","Ciechanowiec","06-406")
print(show(adres1))