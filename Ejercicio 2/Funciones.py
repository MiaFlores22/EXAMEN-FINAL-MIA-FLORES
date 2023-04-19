import random
lista = []
def numeros(tamaño):
    for i in range(tamaño):
        numeros_aleatorios = int(random.uniform(0,100))
        lista.append(numeros_aleatorios)
    return  lista

def numeros_raiz():
    nueva_lista = []
    for i in lista:
        a = pow(i,0.5)
        nueva_lista.append(a)
    print(nueva_lista)

    file = open("notas.txt", "w")
    file.write("La  lista con los numeros aleatorios son: {}".format(lista))
    file.write("\nLa nueva lista con sus respectivas raices son: {}".format(nueva_lista))
    file = open("notas.txt", "r")