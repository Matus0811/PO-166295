'''
1. Napisz klasę Wymierna reprezentującą liczby wymierne p/q. Liczby p i q powinny być
pamiętane jako względnie pierwsze z dodatnim q. Zaimplementuj:

(a) Inicjalizator z dwoma argumentami całkowitymi, licznik i mianownik, przy czym
domyslną wartoscią licznika powinno być zero a mianownika jeden. Inicjalizator po-
winien działać poprawnie również jeżeli podane argumenty nie są względnie pierwsze
lub mianownik jest ujemny.

(b) Funkcje składowe get_licznik i get_mianownik zwracające odpowiednio licznik
i mianownik liczby.

(c) Funkcję składową __repr__ zwracającą łańcuch znaków reprezentujący liczbę wy-
mierną.

(d) Funkcję składową __float__ zwracającą wartość typu float odpowiadającą danej
liczbie wymiernej.

(e) Funkcje składowe __add__ oraz __sub__.

(f) Funkcje składowe __eq__, __ne__, __lt____le____gt____ge__

W funkcji main wczytaj licznik i mianownik dla dwóch liczb wymiernych, utwórz z wczy-
tanych liczb dwie liczby wymierne, a następnie wypisz w kolejnych liniach wyniki uzyskane

z zastosowania zdefiniowanych operatorów.
'''


class wymierna():
    def __init__(self, p, q):
        if q<0 and q != int:
            print("q musi być większe od 0 oraz musi być to liczba pierwsza")
        else:
            self.licznik = p
            self.mianownik = q

    def get_licznik(self):
        return self.licznik

    def get_mianownik(self):
        return self.mianownik

    def __repr__(self):
        return print(self.licznik,"/",self.mianownik)

    def __float__(self):
        zp = self.licznik/self.mianownik
        return zp
    def __add__(self, liczba):
        zp = self.licznik / self.mianownik
        return zp + liczba
    def __sub__(self, liczba):
        zp = self.licznik / self.mianownik
        return zp - liczba

wym1 = wymierna(4,10)
liczba = 2/4
print(wym1.__add__(liczba))


