from os import system
import pprint
import sys
lista_estudiantes = list()
estudiante = {}
Id = 0


def crear():
    estudiante = {}

    Id = len(lista_estudiantes)
    estudiante["1 Nombre"] = input("Nombre: ")
    estudiante["2 Edad"] = int(input("Edad: "))
    estudiante["3 Genero"] = input("Genero: ")
    estudiante["4 Promedio"] = int(input("Promedio: "))
    Id += 1
    estudiante["5 Id"] = Id

    lista_estudiantes.append(estudiante)


def mostrar():
    for est in lista_estudiantes:
        print("Nombre: ", est["1 Nombre"], "- Edad: ", est["2 Edad"], "- Genero: ",est["3 Genero"], "- Promedio: ", est["4 Promedio"], "- ID: ", est["5 Id"])


def eliminar():
    try:
        elemento = int(input("Ingrese el ID del elemento que desea eliminar: "))
        removedElement = lista_estudiantes.pop(elemento-1)
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        eliminar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        eliminar()


def modificar():
    try:
        elemento = int(input("Ingrese el ID del elemento que desea modificar: "))

        estudiante["1 Nombre"] = input("Nombre: ")
        estudiante["2 Edad"] = int(input("Edad: "))
        estudiante["3 Genero"] = input("Genero: ")
        estudiante["4 Promedio"] = int(input("Promedio: "))
        estudiante["5 Id"] = elemento
        lista_estudiantes[elemento-1] = estudiante

    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        modificar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        modificar()


def ordenar():
    try:
        print("**********Menú de Ordenamiento*********")
        print("Presione el número correspondiente según el método que desea implementar:\n\n1. Burbuja.\n2. Selección .\n3. Inserción .\n4. QuickSort .\n5. MergeSort.\n6. ShellSort.\n7. CountSort.\n8. RadixSort.\n9. Regresar al menú principal.")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:
            burbuja()
        elif opcion == 2:
            seleccion()
        elif opcion == 3:
            insercion()
        elif opcion == 4:
            quicksort()
        elif opcion == 5:
            mergesort()
        elif opcion == 6:
            shellsort()
        elif opcion == 7:
            countsort()
        elif opcion == 8:
            radixsort()
        elif opcion == 9:
            menu()
        else:
            print("\n\nOpción inválida\n\n")
            ordenar()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        ordenar()

# Burbuja ascendente
def burbuja_a(lista, key):
    tamano = len(lista)
    i = 0
    while i < tamano:
        j = 0
        while j < (tamano-1):
            if lista[j+1][key] < lista[j][key]:
                bucket = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = bucket
            j += 1
        i += 1
    mostrar()
    system("pause")
    system("cls")
    ordenar()
    
# Burbuja descendente
def burbuja_d(lista, key):
    tamano = len(lista)
    i = 0
    while i < tamano:
        j = 0
        while j < (tamano-1):
            if lista[j+1][key] > lista[j][key]:
                bucket = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = bucket
            j += 1
        i += 1
    mostrar()
    system("pause")
    system("cls")
    ordenar()
    
#Selección ascendente
def seleccion_a(lista, key):
    n = len(lista)
    for i in range(0, n):
        posicion = i
        for j in range(0, n):
            if lista[j][key] > lista[posicion][key]:
                posicion = j
                temp = lista[i]
                lista[i] = lista[posicion]
                lista[posicion] = temp
    mostrar()
    system("pause")
    system("cls")
    ordenar()

#Selección descendente
def seleccion_d(lista, key):
    n = len(lista)
    for i in range(0, n):
        posicion = i
        for j in range(0, n):
            if lista[j][key] < lista[posicion][key]:
                posicion = j
                temp = lista[i]
                lista[i] = lista[posicion]
                lista[posicion] = temp
    mostrar()
    system("pause")
    system("cls")
    ordenar()
    
#Incersión ascendente
def insercion_a(lista,key):
    tam= len(lista)
    for i in range(1, tam):
        cvalue = lista[i]
        posicion = i
        while posicion > 0 and lista[posicion-1][key] > lista[i][key]:
            lista[posicion] = lista[posicion-1]
            posicion-= 1
        lista[posicion] = cvalue
    mostrar()
    system("pause")
    system("cls")
    ordenar()


#Incersión descendente
def insercion_d(lista,key):
    tam= len(lista)
    for i in range(1, tam):
        cvalue = lista[i]
        posicion = i
        while posicion > 0 and lista[posicion-1][key] < lista[i][key]:
            lista[posicion] = lista[posicion-1]
            posicion-= 1
        lista[posicion] = cvalue
    mostrar()
    system("pause")
    system("cls")
    ordenar()

#Función de apoyo para quicksort
def particionado(lista,key):
    menores = []
    mayores = []
    pivote = lista[0]
    for i in range(1,len(lista)):
        if lista[i][key] < pivote[key]:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores

#Quicksort ascendente
def quicksort_a(lista,key):
    if len(lista) < 2 :
        return lista
    else:
        menores,pivote,mayores = particionado(lista,key)
        menores= quicksort_a(menores,key) 
        mayores= quicksort_a(mayores,key)
        lista=menores + [pivote] + mayores
        return lista

#Quicksort decreciente
def quicksort_d(lista,key):
    if len(lista) < 2 :
        return lista
    else:
        menores,pivote,mayores = particionado(lista,key)
        lista=quicksort_d(mayores,key) + [pivote] + quicksort_d(menores,key)
        return lista

#Shellsort creciente
def shellsort_a(lista,key):
    n = len(lista)
    #print(n)
    for i in range(1, n):
        valor = lista[i] #toma el siguiente valor a ser isnertado
        #print("valor", nums[i])
        posicion = i # indice  donde se insertará el vavlor
        #print("posicion", posicion)

        while posicion > 0 and lista[posicion -1][key] > valor[key]: #si la posicion es mayor a 0 Y los numeros en la posicion[posicion - 1] es mayor a el valor
            lista[posicion] = lista[posicion -1] # numeros[posicion] = numeros[posicion - 1]
            #print("valor cambiado", nums[posicion])
            posicion -= 1 # posicion decrementa en 1
            lista[posicion] = valor # numeros[posicion] = valor
    mostrar()
    system("pause")
    system("cls")
    ordenar()
    
#Shellsort decreciente
def shellsort_d(lista,key):
    n = len(lista)
    #print(n)
    for i in range(1, n):
        valor = lista[i] #toma el siguiente valor a ser isnertado
        #print("valor", nums[i])
        posicion = i # indice  donde se insertará el vavlor
        #print("posicion", posicion)

        while posicion > 0 and lista[posicion -1][key] < valor[key]: #si la posicion es mayor a 0 Y los numeros en la posicion[posicion - 1] es mayor a el valor
            lista[posicion] = lista[posicion -1] # numeros[posicion] = numeros[posicion - 1]
            #print("valor cambiado", nums[posicion])
            posicion -= 1 # posicion decrementa en 1
            lista[posicion] = valor # numeros[posicion] = valor
    mostrar()
    system("pause")
    system("cls")
    ordenar()
    
#Mergesort Ascendente
def mergesort_a(lista,key):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        mergesort_a(primera_mitad,key)
        mergesort_a(segunda_mitad,key)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i][key] < segunda_mitad[j][key]:
                lista[k] = primera_mitad[i]
                i+= 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k+= 1
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i+=1
            k+=1
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j+=1
            k+=1
        return lista
#Mergesort Descendente
def mergesort_d(lista,key):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        mergesort_d(primera_mitad,key)
        mergesort_d(segunda_mitad,key)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i][key] > segunda_mitad[j][key]:
                lista[k] = primera_mitad[i]
                i+= 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k+= 1
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i+=1
            k+=1
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j+=1
            k+=1
        return lista
    
#Función de apoyo para radixsort
def countingSortForRadix(lista, placeValue,key):
    countArray = [0] * 10
    tamano = len(lista)
    
    for i in range(tamano): 
        placeElement = (lista[i][key] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    nueva_lista = [0] * tamano
    i = tamano - 1
    while i >= 0:
        currentEl = lista[i]
        placeElement = (lista[i][key] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        nueva_lista[newPosition] = currentEl
        i -= 1
        
    return nueva_lista

#Rdixsort ascendente
def radixSort_a(lista,key):
    
    maximo=0
    for elemento in lista:
        if elemento[key] > maximo:
            maximo = elemento[key]
    D = 1
    while maximo > 0:
        maximo /= 10
        D += 1
    
    placeVal = 1

    nueva_lista = lista
    while D > 0:
        nueva_lista = countingSortForRadix(nueva_lista, placeVal,key)
        placeVal *= 10  
        D -= 1

    return nueva_lista

#Declaración de menú de busqueda
def buscar():
    try:
        print("\n**********Menú de Búsqueda*********")
        print("Presione el número correspondiente según el método de búsqueda que desea implementar:\n\n1. Búsqueda secuencial con centinela.\n2. Búsqueda binaria.\n3. Regresar al menú principal.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:
            busquedaSecuencial()
        elif opcion == 2:
            while True:
                num=int(input("indica un numero a buscar: "))
                if num=="":
                    break
                try:
                    num=int(num)
                except:
                    print("El valor tienes que ser numerico")
                    continue
                conseguido,iteraciones=busquedaBinaria(lista_estudiantes,"5 Id",num,0,len(lista_estudiantes),1)
                if conseguido:
                    print("Encontrado en {} iteraciones".format(iteraciones))
                else:
                    print("El valor introducido no se encuentra en la lista de valores. Se han necesitado {} iteraciones".format(iteraciones))
        elif opcion == 3:
            menu()
        else:
            print("\n\nOpción inválida\n\n")
            buscar()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        buscar()

# Declaración de metodo de ordenamiento
def burbuja():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # Burbuja por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Burbuja por promedio ascendente
                    burbuja_a(lista_estudiantes, "4 Promedio")

                elif opcion == 2:  # Burbuja por promedio descendente
                    burbuja_d(lista_estudiantes, "4 Promedio")
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Burbuja por edad ascendente
                    burbuja_a(lista_estudiantes, "2 Edad")
                elif opcion == 2:  # Burbuja por edad descendente
                    burbuja_d(lista_estudiantes, "2 Edad")
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Burbuja por ID ascendente
                    burbuja_a(lista_estudiantes, "5 Id")
                elif opcion == 2:  # Burbuja por ID descendente
                    burbuja_d(lista_estudiantes, "5 Id")
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            burbuja()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        burbuja()


def seleccion():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # Selección por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Selección por promedio ascendente
                    seleccion_a(lista_estudiantes,"4 Promedio")
                elif opcion == 2:  # Selección por promedio descendente
                    seleccion_d(lista_estudiantes,"4 Promedio")
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Selección por edad ascendente
                    seleccion_a(lista_estudiantes,"2 Edad")
                elif opcion == 2:  # Selección por edad descendente
                    seleccion_d(lista_estudiantes,"2 Edad")
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # Selección por ID ascendente
                    seleccion_a(lista_estudiantes,"5 Id")
                elif opcion == 2:  # Selección por ID descendente
                    seleccion_d(lista_estudiantes,"5 Id")
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            seleccion()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        seleccion()


def insercion():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # insercion por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # insercion por promedio ascendente
                    insercion_a(lista_estudiantes,"4 Promedio")
                elif opcion == 2:  # insercion por promedio descendente
                    insercion_d(lista_estudiantes,"4 Promedio")
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # insercion por edad ascendente
                    insercion_a(lista_estudiantes,"2 Edad")
                elif opcion == 2:  # insercion por edad descendente
                    insercion_d(lista_estudiantes,"2 Edad")
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # insercion por ID ascendente
                    insercion_a(lista_estudiantes,"5 Id")
                elif opcion == 2:  # insercion por ID descendente
                    insercion_d(lista_estudiantes,"5 Id")
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            insercion()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        insercion()


def quicksort():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # quicksort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # quicksort por promedio ascendente
                    pprint.pprint(quicksort_a(lista_estudiantes,"4 Promedio"))
    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # quicksort por promedio descendente
                    pprint.pprint(quicksort_d(lista_estudiantes,"4 Promedio"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # quicksort por edad ascendente
                    pprint.pprint(quicksort_a(lista_estudiantes,"2 Edad"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # quicksort por edad descendente
                    pprint.pprint(quicksort_d(lista_estudiantes,"2 Edad"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # quicksort por ID ascendente
                    pprint.pprint(quicksort_a(lista_estudiantes,"5 Id"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # quicksort por ID descendente
                    pprint.pprint(quicksort_d(lista_estudiantes,"5 Id"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()
        
            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()
        elif opcion == 4:
            ordenar()

        else:
            print("\n\nOpción inválida\n\n")
            quicksort()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        quicksort()


def mergesort():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # mergesort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # mergesort por promedio ascendente
                    pprint.pprint(mergesort_a(lista_estudiantes,"4 Promedio"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # mergesort por promedio descendente
                    pprint.pprint(mergesort_d(lista_estudiantes,"4 Promedio"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # mergesort por edad ascendente
                    pprint.pprint(mergesort_a(lista_estudiantes,"2 Edad"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # mergesort por edad descendente
                    pprint.pprint(mergesort_d(lista_estudiantes,"2 Edad"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # mergesort por ID ascendente
                    pprint.pprint(mergesort_a(lista_estudiantes,"5 Id"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # mergesort por ID descendente
                    pprint.pprint(mergesort_d(lista_estudiantes,"5 Id"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            mergesort()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        mergesort()


def shellsort():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # shellsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # shellsort por promedio ascendente
                    shellsort_a(lista_estudiantes,"4 Promedio")
                elif opcion == 2:  # shellsort por promedio descendente
                    shellsort_d(lista_estudiantes,"4 Promedio")
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # shellsort por edad ascendente
                    shellsort_a(lista_estudiantes,"2 Edad")
                elif opcion == 2:  # shellsort por edad descendente
                    shellsort_d(lista_estudiantes,"2 Edad")
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # shellsort por ID ascendente
                    shellsort_a(lista_estudiantes,"5 Id")
                elif opcion == 2:  # shellsort por ID descendente
                    shellsort_d(lista_estudiantes,"5 Id")
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            shellsort()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        shellsort()


def countsort():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # countsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # countsort por promedio ascendente
                    pass
                elif opcion == 2:  # countsort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # countsort por edad ascendente
                    pass
                elif opcion == 2:  # countsort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # countsort por ID ascendente
                    pass
                elif opcion == 2:  # countsort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            countsort()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        countsort()


def radixsort():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1:  # radixsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # radixsort por promedio ascendente
                    pprint.pprint(radixSort_a(lista_estudiantes,"4 Promedio"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # radixsort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()

        elif opcion == 2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # radixsort por edad ascendente
                    pprint.pprint(radixSort_a(lista_estudiantes,"2 Edad"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # radixsort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()

        elif opcion == 3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion = int(input("Por favor ingrese una opción:"))

                if opcion == 1:  # radixsort por ID ascendente
                    pprint.pprint(radixSort_a(lista_estudiantes,"5 Id"))
                    
                    system("pause")
                    system("cls")
                    ordenar()
                elif opcion == 2:  # radixsort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()

            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()
        elif opcion == 4:
            ordenar()
        else:
            print("\n\nOpción inválida\n\n")
            radixsort()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        radixsort()




def busquedaSecuencial():
    try:
        num = int(input("\nIngrese el ID del elemento que desea buscar: "))
        for est in lista_estudiantes:
            if num == est["5 Id"]:
                print("Nombre: ", est["1 Nombre"], "- Edad: ", est["2 Edad"], "- Genero: ",est["3 Genero"], "- Promedio: ", est["4 Promedio"], "- ID: ", est["5 Id"])
            
        system("pause")
        buscar()
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        system("pause")
        buscar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        system("pause")
        buscar()


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
    



def menu():
    print("\n")
    # system("pause")
    # system("cls")
    try:

        print("\n\n**********Menú Principal*********")
        print("Presione el número correspondiente según lo que desee hacer:\n\n1. Crear un registro.\n2. Eliminar un registro.\n3. Modificar un registro.\n4. Mostrar registros.\n5. Ordenar los registros.\n6. Buscar por ID.\n7. Salir del programa.")
        opcion = int(input("\nPor favor ingrese una opción:"))

        if opcion == 1:
            crear()
            menu()
        elif opcion == 2:
            print("\nLos registros actuales son:\n")
            mostrar()
            eliminar()
            print(
                "\nEliminado exitosamente\nLa lista actualizada se muestra a continuación: \n")
            mostrar()
            menu()
        elif opcion == 3:
            print("\nLos registros actuales son:\n")
            mostrar()
            modificar()
            print("\nLa lista actualizada se muestra a continuación: \n")
            mostrar()
            menu()
        elif opcion == 4:
            print("\nLos registros actuales son:\n")
            mostrar()
            system("pause")
            menu()
        elif opcion == 5:
            ordenar()
        elif opcion == 6:
            buscar()
        elif opcion == 7:
            print("\nSaliendo del programa...")
            print(sys.exit())
        else:
            print("\n\nOpción inválida\n\n")
            menu()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        menu()


print("******Bienvenido*******")
menu()
