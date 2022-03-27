

from pickle import TRUE


personajes = []

p = { "Nombre":"Aragon","Numero":1}

personajes.append(p)

p = { "Nombre":"ricar","Numero":2}
personajes.append(p)

p = { "Nombre":"homero","Numero":3}
personajes.append(p)
p = { "Nombre":"homero","Numero":4}
personajes.append(p)

def busquedaBinaria(lista,key,num,inicio,fin,iteraciones):
    centro=int((fin-inicio)/2)+inicio
    if centro>len(lista)-1 or inicio>fin:
        return (False,iteraciones)
    if num>lista[centro][key]:
        return busquedaBinaria(lista,key,num,centro+1,fin,iteraciones+1)
    elif num<lista[centro][key]:
        return busquedaBinaria(lista,key,num,inicio,centro-1,iteraciones+1)
    else:
        return (True,iteraciones)

while True:
    num=int(input("indica un numero a buscar: "))
    if num=="":
        break
    try:
        num=int(num)
    except:
        print("El valor tienes que ser numerico")
        continue
    conseguido,iteraciones=busquedaBinaria(personajes,"Numero",num,0,len(personajes),1)
    if conseguido:
        print("Encontrado en {} iteraciones".format(iteraciones))
    else:
        print("El valor introducido no se encuentra en la lista de valores. Se han necesitado {} iteraciones".format(iteraciones))