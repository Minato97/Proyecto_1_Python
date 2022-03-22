personajes = []

p = { "Nombre":"Aragon","Numero":10}

personajes.append(p)

p = { "Nombre":"ricar","Numero":2}
personajes.append(p)

p = { "Nombre":"homero","Numero":7}
personajes.append(p)
#print(personajes)
def burbuja(lista,key):
    tamano = len(lista)
    print(tamano)
    i= 0
    while i < tamano:
        j= 0
        
        while j < (tamano-1):
            if lista[j+1][key] > lista[j][key]:
                bucket = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = bucket
            j+= 1
        i+= 1
    return lista


print(burbuja(personajes,"Numero"))

print(personajes[0]["Numero"])