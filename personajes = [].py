personajes = []

p = { "Nombre":"Aragon","Numero":10}

personajes.append(p)

p = { "Nombre":"ricar","Numero":2}
personajes.append(p)

p = { "Nombre":"homero","Numero":7}
personajes.append(p)
#print(personajes)
def particionado(lista):

    menores = []
    mayores = []
    pivote = lista[0]
    for i in range(1,len(lista)):
        if lista[i]["Numero"] < pivote["Numero"]:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores

def quicksort(lista):
    if len(lista) < 2 :
        return lista
    else:
        menores,pivote,mayores = particionado(lista)
        lista=quicksort(menores) + [pivote] + quicksort(mayores)
        return lista


print(quicksort(personajes))




#print(personajes[0]["Numero"])