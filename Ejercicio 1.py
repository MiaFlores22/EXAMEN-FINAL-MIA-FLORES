import random
lista = []
def numeros():
    for i in range(10):
        numeros_aleatorios = int(random.uniform(0,100))
        lista.append(numeros_aleatorios)
    print(lista)

print("Los numeros aleatorios son: ")
numeros()
print()
def numero_no_repetidos():
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
    print(lista)

print("Lista con los numero no repetidos")
numero_no_repetidos()
print()

def numero_ascendentes():
    print("Los numeros en orden de menor a mayor son: ")
    lista.sort()
    print(lista)

numero_ascendentes()
print()

def numeros_descendentes():
    print("Los numeros en orden de mayor a menor son: ")
    numeros_descendentes = sorted(lista, reverse=True)
    print(numeros_descendentes)

numeros_descendentes()
print()

def numero_mayor():
    print("El numero mayor de lista es: {}".format(max(lista)))

numero_mayor()