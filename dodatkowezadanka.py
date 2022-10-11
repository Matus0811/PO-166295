'''
1. Przygotować funkcję, która przyjmie argumenty x, y typu całkowitego oraz operator typu tekstowego (dodawanie, odejmowanie).
Funkcja zwróci wynik dodawania lub odejmowania argumentów x i y w zależności od znaku działania przekazanego w argumencie operator.
'''
x = int(input("Podaj liczbę pierwszą: "))
y = int(input("Podaj liczbę drugą: "))
argument = str(input("Podaj operator: "))
def dzial(x,y,arg):
    ode = str("-")
    doda = str("+")
    arg = str(arg)
    if arg == ode:
        return x - y
    elif arg == doda:
        return x + y
    else:
        print("Podano złe działanie")

print(dzial(x,y,argument))
