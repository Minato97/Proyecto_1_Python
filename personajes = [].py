from pickle import TRUE


personajes = []

p = { "Nombre":"Aragon","Numero":10}

personajes.append(p)

p = { "Nombre":"ricar","Numero":2}
personajes.append(p)

p = { "Nombre":"homero","Numero":7}
personajes.append(p)
p = { "Nombre":"homero","Numero":4}
personajes.append(p)

#print(personajes)
def countingSortForRadix(lista, placeValue):
    countArray = [0] * 10
    tamano = len(lista)

    for i in range(tamano): 
        placeElement = (lista[i]["Numero"] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    nueva_lista = [0] * tamano
    i = tamano - 1
    while i >= 0:
        currentEl = lista[i]
        placeElement = (lista[i]["Numero"] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        nueva_lista[newPosition] = currentEl
        i -= 1
        
    return nueva_lista

def radixSort(lista):
    
    maximo=0
    for elemento in lista:
        if elemento["Numero"] > maximo:
            maximo = elemento["Numero"]
    D = 1
    while maximo > 0:
        maximo /= 10
        D += 1
    
    placeVal = 1

    nueva_lista = lista
    while D > 0:
        nueva_lista = countingSortForRadix(nueva_lista, placeVal)
        placeVal *= 10  
        D -= 1

    return nueva_lista

print(radixSort(personajes))

# print("antes de ordenar")
# print(personajes)
# print("despues de ordenar")
# print(mergesort_d(personajes,"Numero"))

#print(shell(personajes))




#print(personajes[0]["Numero"])