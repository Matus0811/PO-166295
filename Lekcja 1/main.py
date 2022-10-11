#zadanie 1
# lista1a = [x for x in range(1,11)]
# print(lista1a)
#
# lista1b = [x*2 for x in range(0,11)]
# print(lista1b)
#
# lista1c = [x**2 for x in range(1,11)]
# print(lista1c)
#
# lista1d = [x*0 for x in range(1,10)]
# print(lista1d)
#
# lista1e = [x%2 for x in range(1,10)]
# print(lista1e)
#
# lista1f = [x%5 for x in range(1,10)]
# print(lista1f)

#zadanie 2
# lista2a = []
# x = 0
# while x <11:
#  lista2a.append(x)
#  x+=1
# print(lista2a)
#
# lista2b = []
# x = 0
# while x <11:
#  lista2b.append(x*2)
#  x+=1
# print(lista2b)
#
# lista2c = []
# x = 1
# while x <11:
#  lista2c.append(x**2)
#  x+=1
# print(lista2c)
#
# lista2d = []
# x = 0
# while x <10:
#  lista2d.append(x*0)
#  x+=1
# print(lista2d)
#
# lista2e = []
# x = 0
# while x <10:
#  lista2e.append(x%2)
#  x+=1
# print(lista2e)
#
# lista2f = []
# x = 0
# while x <10:
#  lista2f.append(x%5)
#  x+=1
# print(lista2f)

#Zadanie 3
# def ujemne(lista):
#  x=0
#  for i in lista:
#   if i<0:
#    x += 1
#  return x
#
# lista3 = [0,1,2,-1,-2]
# print(ujemne(lista3))

#Zadanie 4
# def iloczyn(lista):
#  x = 1
#  for i in lista:
#   x *= i
#  return x
#
# lista4 = [1,3,5,2]
# print(iloczyn(lista4))

#Zadanie 5
def minmax(lista):
    min = 0
    max = 0
    for i in lista:
        if max<i:
            max = i
        if min>i:
            min = i
    krotka = (min , max)
    return krotka
lista5 = [1,12,31,-4]
print(minmax(lista5))
