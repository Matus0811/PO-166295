'''
1. Napisz funkcje mult, która przyjmuje jeden argument tylko pozycyjny. Załóz, ̇ ze ten  ̇
argument jest niepustym obiektem iterowalnym typu krotka, lista, zbiór lub zakres. Jako
wynik funkcja zwraca iloczyn elementów swojego argumentu.
'''
def mult(argumencik):
    x = 1
    for i in argumencik:
        x *= i
    return x
lista1 = [3,5,7]
print(mult(lista1))

'''
2. Napisz funkcje mult_ints, która przyjmuje jeden argument tylko pozycyjny. Załóz,
ze ten argument jest niepustym obiektem iterowalnym typu krotka, lista, zbiór lub zakres.
Jako wynik zwraca iloczyn tych argumentów, które sa˛ typu całkowitego.
'''
def mult_ints(argumencik):
    x = 1
    for i in argumencik:
        if type(i) == int:
            x *= i
    return x
lista2 = [2,5,7,3.14,21]
print(mult_ints(lista2))

'''
3. Napisz funkcje˛ multiply, która przyjmuje dowolna˛ liczbe˛ argumentów nienazwanych,
a jako wynik zwraca iloczyn tych argumentów.
'''
def multiply(*arg):
    x = 1
    for i in arg:
        x *= i
    return x
print(multiply(1,4,6,))
'''
4. Napisz funkcje˛ multiply_ints, która przyjmuje dowolna˛ liczbe˛ argumentów nienazwanych,
a jako wynik zwraca iloczyn tych argumentów, które sa˛ typu całkowitego.
'''
def multiply_ints(*arg):
    x = 1
    for i in arg:
        if type(i) == int:
            x *= i
    return x

print(multiply_ints(1,3.14,2,6))
'''
5. Napisz funkcj˛e make_car, która przyjmuje dwa obligatoryjne argumenty: firma
i model, oraz dowolna˛ liczbe˛ argumentów nazwanych. Funkcja make_car jako swój
wynik zwraca słownik opisuja˛cy konkretny samochód.
'''
def make_car(firma,model,**kwargs):
    kwargs['firma'] = firma
    kwargs['model'] = model
    return kwargs

print(make_car(firma = "Mazda", model = "6", cena = 1500, kolor = "Piorunowy"))

'''
1. Utwórz dwuwymiarowa˛tablice˛ liczb całkowitych o trzech wierszach. Wpierwszymwierszu
tablicy umie´s´c liczby od 1 do 10, w drugim kwadraty tych liczb, a w trzecim sze´sciany
liczb z pierwszego wiersza. Napisz program tworza˛cy i wys´wietlaja˛cy te˛ tablice˛ w konsoli
'''
lista31 = [[x for x in range(1,11)],[x**2 for x in range(1,11)],[x**3 for x in range(1,11)]]
print(lista31)

'''
2. W tablicy dwuwymiarowej nie wszystkie wiersze musza˛ miec´ ten sam rozmiar. Napisz
program, który utworzy tablic˛e liczb całkowitych o dziesi˛eciu wierszach. Wypełnij tablice
˛ kolejnymi liczbami naturalnymi, zaczynaja˛c od liczby 1. W pierwszym wierszu
umies´c´ jedna˛ liczbe˛, w drugim dwie liczby, w trzecim trzy itd. – w dziesia˛tym dziesie˛c´
liczb. Oblicz sumy liczb w kolejnych wierszach i sum˛e wszystkich liczb zapisanych w
tablicy. Wy´swietl w konsoli tablic˛e liczb oraz obliczone sumy.
'''

lista32 = [[x for x in range(1,2)],[x for x in range(1,3)],[x for x in range(1,4)],[x for x in range(1,5)],[x for x in range(1,6)],[x for x in range(1,7)],[x for x in range(1,8)],[x for x in range(1,9)],[x for x in range(1,10)],[x for x in range(1,11)]]
print(lista32)

'''
1. Napisz funkcje˛ sum(a, b) dodaja˛ca˛ dwie macierze. Funkcja powinna zwracac´ jako
swój wynik macierz be˛da˛ca˛ suma˛ macierzy. Napisz program demonstruja˛cy działanie
funkcji sum(a, b).
'''
# def sum(a,b):
#     macierz = []
#     for i in range(len(a)):
#
#         for j in range(len(a[0])):
#             macierz = a[i][j] + b[i][j]
#     return macierz
#
# macierza = [[1,1],[1,2]]
# macierzb = [[1,2],[1,0]]
#
# print(sum(macierza,macierzb))