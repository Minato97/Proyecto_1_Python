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
p = { "Nombre":"homero","Numero":9}
personajes.append(p)
#Ignacio Andrade
def insercion_a(Arreglo,key):
    for i in range(1, len(Arreglo)):
        copia_valor=Arreglo[i]
        posicion=i
        while (posicion>0) and (Arreglo[posicion-1][key] > copia_valor[key]):
            Arreglo[posicion] = Arreglo[posicion-1]
            Arreglo[posicion-1] = copia_valor
            posicion=posicion-1
        Arreglo[posicion]=copia_valor
    return Arreglo

def insercion_d(Arreglo,key):
    for i in range(1, len(Arreglo)):
        copia_valor=Arreglo[i]
        posicion=i
        while (posicion>0) and (Arreglo[posicion-1][key] < copia_valor[key]):
            Arreglo[posicion] = Arreglo[posicion-1]
            Arreglo[posicion-1] = copia_valor
            posicion=posicion-1
        Arreglo[posicion]=copia_valor
    return Arreglo


print("---------------------")
print(insercion(personajes))
print(insercion2(personajes))