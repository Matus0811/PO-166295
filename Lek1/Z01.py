

#zadanie 1
# lista = []
# lista = [ x for x in range (1,11)]
# lista = [ x*2 for x in range (0,11)]
# lista = [ x**2 for x in range (1,11)]
# lista = [ x*0 for x in range (1,11)]
# lista = [ x%2 for x in range (0,10)]
# lista = [ x%5 for x in range (0,10)]
# print(lista)

#zadanie 2
# lista_2 = []
#
# x = 0
# while x < 11:
#     lista_2.append(x)
#     x+=1
# print(lista_2)
#
# lista_2 = []
# x = 0
# while x < 11:
#     lista_2.append(x*2)
#     x+=1
# print(lista_2)
#
# lista_2 = []
# x = 1
# while x < 11:
#     lista_2.append(x**2)
#     x+=1
# print(lista_2)
#
# lista_2 = []
# x = 1
# while x < 11:
#     lista_2.append(x*0)
#     x+=1
# print(lista_2)
#
# lista_2 = []
# x = 0
# while x < 10:
#     lista_2.append(x%2)
#     x+=1
# print(lista_2)
#
# lista_2 = []
# x = 0
# while x < 10:
#     lista_2.append(x%5)
#     x+=1
# print(lista_2)

#zadanie 3
# def ile_ujemnych(lista):
#     x = 0
#     for i in lista:
#         if i < 0:
#             x += 1
#     return x
#
#
# lista_3 = [-11,-2,3]
# print(ile_ujemnych(lista_3))

#zadanie 4
# def iloczyn(lista):
#     x = 1
#     for i in lista:
#         x *= i
#     return x
#
#
# lista_4 = [1,2,4]
# print(iloczyn(lista_4))

#zadanie 5
# def minmax(lista):
#   min = 0
#   max = 0
#   for i in lista:
#       if min> i:
#           min = i
#   for i in lista:
#       if max< i:
#           max = i
#   return(min,max)
#
# lista_5=[4,3,1,-3,8,0]
# print(minmax(lista_5))

#zadanie 6
# def przemiana(listunia):
#     znaczek = 1;
#     sumcia = 0
#     for i in listunia:
#         sumcia += i * znaczek
#         znaczek = -znaczek
#     return(sumcia)
# lista_6=[4,2,1,3,11,1]
# print(przemiana(lista_6))

#zadanie 7
def czyjest(liczba, lista):
    for i in lista:
        if i == liczba:
            return True
        else:
            return False
    

def dodawanieliczb(lista):
    while len(lista) < 11:
        c = int(input("Podaj liczbe: "))




