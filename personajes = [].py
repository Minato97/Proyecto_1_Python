personajes = []

p = { "Nombre":"Aragon","Numero":10}

personajes.append(p)

p = { "Nombre":"ricar","Numero":2}
personajes.append(p)

p = { "Nombre":"homero","Numero":7}
personajes.append(p)
#print(personajes)
def conteo(a):
    n= len(a)
    maximo=0
    for y in range(0, n):
        if a[y]["Numero"] > maximo:
            maximo = a[y]["Numero"]
    
    c_arr = []
    for j in range(0, maximo + 1):
        p= { "Nombre":"","Numero":0}
        c_arr.append(p)
    print(c_arr)
    for i in range (0, n):
        c_arr[a[i]]["Numero"] = c_arr[a[i]]["Numero"] + 1
    i = maximo
    j = 0
    while i > 0:
        if c_arr[i]["Numero"] > 0:
            a[j] = i
            j+= 1
            c_arr[i] = c_arr[i] - 1
        else:
            i-= 1
    return a

print(conteo(personajes))




#print(personajes[0]["Numero"])