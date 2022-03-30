# personajes = []

# p = { "Nombre":"Aragon","Numero":10}

# personajes.append(p)

# p = { "Nombre":"ricar","Numero":2}
# personajes.append(p)

# p = { "Nombre":"homero","Numero":7}
# personajes.append(p)
# #print(personajes)
# def burbuja(lista):
#     tamano = len(lista)
#     print(tamano)
#     i= 0
#     while i < tamano:
#         j= 0
        
#         while j < (tamano-1):
#             if lista[j+1]["Numero"] > lista[j]["Numero"]:
#                 bucket = lista[j]
#                 lista[j] = lista[j+1]
#                 lista[j+1] = bucket
#             j+= 1
#         i+= 1
#     return lista


# print(burbuja(personajes))

# print(personajes[0]["Numero"])


monos = []

p = { "Nombre":"martin","edad":20}

monos.append(p)

p = { "Nombre":"nacho","edad":35}
monos.append(p)

p = { "Nombre":"chelis","edad":22}
monos.append(p)

p = { "Nombre":"geo","edad":21}
monos.append(p)

p = { "Nombre":"leo","edad":54}
monos.append(p)

# #que tome los valores por los cuales quiere hacer el ordenamiento, edad, id, promedio
# #si de manera creciente o decreciente

# def shell(monos):
#     n = len(monos)

#     for i in range(1, n):
#       #que tome la lista a ser evaluada y acceda a el valor correspondiente
#         valor = monos[i] #toma el siguiente valor a ser isnertado

#         posicion = i # indice  donde se insertará el vavlor

#         while posicion > 0 and monos[posicion]["edad"]-1 > valor["edad"]: #si la posicion es mayor a 0 Y los numeros en la posicion[posicion - 1] es mayor a el valor
#             print("ingresa al while")
#             monos[posicion] = monos[posicion]-1 # numeros[posicion] = numeros[posicion - 1]
#             posicion -= 1 # posicion decrementa en 1
#             monos[posicion] = valor # numeros[posicion] = valor
#     return monos


# def radixi(monos):
#     opcion= int(input())
#     if opcion == 1:
#         opcion = str("promedio")
#     elif opcion == 2:
#         opcion = str("edad")
#     elif opcion == 3:
#         opcion = str("ID")
#     n= len(monos)
#     listaDeValores= []
#     for i in range(0, n):
#         listaDeValores.append(monos[i][opcion])
#     maximo = max(listaDeValores)
#     digitos = len(str(maximo))
#     bins = [10]

#     for i in range(0, digitos):
#         for j in range(0, n):
#             e= (monos[j][opcion] / (10**i)) % 10
#             bins[e].append(monos[j][opcion])
#         k= 0
#         for x in range(0, 10):
#             if len(bins[x]) > 0:
#                 for y in range(0, len(bins[x])):
#                     monos[k] = bins[x].pop()
#                     k+= 1
#     return monos

# print(radixi(monos))

def radixi(valores):
    #opcion= int(input())
    # if opcion == 1:
    #     opcion = str("promedio")
    # elif opcion == 2:
    #     opcion = str("edad")
    # elif opcion == 3:
    #     opcion = str("ID")
    n= len(valores)
    maximo = max(valores)
    print(maximo)
    digitos = len(str(maximo))
    print(digitos)
    bins = []

    for i in range(0, digitos-1):
        for j in range(0, n-1):
            e= int((valores[j] / (10**i)) % 10)
            print(e)
            #bins[e].append(valores[j])
        k= 0
        for x in range(0, 10):
            if len(bins[x]) > 0:
                for y in range(0, len(bins[x])):
                    valores[k] = bins[x].pop()
                    k+= 1
    return valores

valores = [10,8,9,7,5,6,4,3,1,2]
print(radixi(valores))