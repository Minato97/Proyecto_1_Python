from os import system
import pprint
import sys

#Andrea explica la estructura de la lista de diccionarios y el metodo mostrar
lista_estudiantes = list()
estudiante = {}
contador_Id = 0

def mostrar(lista):
    for est in lista:
        print("Nombre: ", est["A)Nombre"], "- Edad: ", est["B)Edad"], "- Genero: ",est["C)Genero"], "- Promedio: ", est["D)Promedio"], "- ID: ", est["E)Id"])
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Bredant los metodos crear, eliminar y modificar
def crear():
    estudiante = {}
    global contador_Id 
    contador_Id += 1 
    #Id = len(lista_estudiantes)
    estudiante["A)Nombre"] = input("Nombre: ")
    estudiante["B)Edad"] = int(input("Edad: "))
    estudiante["C)Genero"] = input("Genero: ")
    estudiante["D)Promedio"] = int(input("Promedio: "))
    #Id += 1
    estudiante["E)Id"] = contador_Id

    lista_estudiantes.append(estudiante)


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

        estudiante["A)Nombre"] = input("Nombre: ")
        estudiante["B)Edad"] = int(input("Edad: "))
        estudiante["C)Genero"] = input("Genero: ")
        estudiante["D)Promedio"] = int(input("Promedio: "))
        estudiante["E)Id"] = elemento
        lista_estudiantes[elemento-1] = estudiante

    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        modificar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        modificar()
        
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Giovanny explica la navegación en los menus
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
            mostrar(lista_estudiantes)
            eliminar()
            print(
                "\nEliminado exitosamente\nLa lista actualizada se muestra a continuación: \n")
            mostrar(lista_estudiantes)
            menu()
        elif opcion == 3:
            print("\nLos registros actuales son:\n")
            mostrar(lista_estudiantes)
            modificar()
            print("\nLa lista actualizada se muestra a continuación: \n")
            mostrar(lista_estudiantes)
            menu()
        elif opcion == 4:
            print("\nLos registros actuales son:\n")
            mostrar(lista_estudiantes)
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
        
#Menu de ordenamiento
def ordenar():
    try:
        print("**********Menú de Ordenamiento*********")
        print("Presione el número correspondiente según el método que desea implementar:\n\n1. Burbuja.\n2. Selección .\n3. Inserción .\n4. QuickSort .\n5. MergeSort.\n6. ShellSort.\n7. CountSort.\n8. RadixSort.\n9. Regresar al menú principal.")
        opcion = int(input("Por favor ingrese una opción:"))

        if opcion == 1: #burbuja
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  # Burbuja por promedio ascendente
                burbuja_a(lista_estudiantes, "D)Promedio")
            elif key == 1 and orden == 2:  # Burbuja por promedio descendente
                burbuja_d(lista_estudiantes, "D)Promedio")
            elif key == 2 and orden == 1:  # Burbuja por edad ascendente
                burbuja_a(lista_estudiantes, "B)Edad")
            elif key == 2 and orden == 2:  # Burbuja por edad descendente
                burbuja_d(lista_estudiantes, "B)Edad")
            elif key == 3 and orden == 1:  # Burbuja por ID ascendente
                burbuja_a(lista_estudiantes, "E)Id")
            elif key == 3 and orden == 2:  # Burbuja por ID descendente
                burbuja_d(lista_estudiantes, "E)Id")
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 2: #seleccion
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  # Seleccion por promedio ascendente
                seleccion_a(lista_estudiantes, "D)Promedio")
            elif key == 1 and orden == 2:  # Seleccion por promedio descendente
                seleccion_d(lista_estudiantes, "D)Promedio")
            elif key == 2 and orden == 1:  # Seleccion por edad ascendente
                seleccion_a(lista_estudiantes, "B)Edad")
            elif key == 2 and orden == 2:  # Seleccion por edad descendente
                seleccion_d(lista_estudiantes, "B)Edad")
            elif key == 3 and orden == 1:  # Seleccion por ID ascendente
                seleccion_a(lista_estudiantes, "E)Id")
            elif key == 3 and orden == 2:  # Seleccion por ID descendente
                seleccion_d(lista_estudiantes, "E)Id")
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 3: #inserción
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  # Insercion por promedio ascendente
                insercion_a(lista_estudiantes, "D)Promedio")
            elif key == 1 and orden == 2:  # Insercion por promedio descendente
                insercion_d(lista_estudiantes, "D)Promedio")
            elif key == 2 and orden == 1:  # Insercion por edad ascendente
                insercion_a(lista_estudiantes, "B)Edad")
            elif key == 2 and orden == 2:  # Insercion por edad descendente
                insercion_d(lista_estudiantes, "B)Edad")
            elif key == 3 and orden == 1:  # Insercion por ID ascendente
                insercion_a(lista_estudiantes, "E)Id")
            elif key == 3 and orden == 2:  # Insercion por ID descendente
                insercion_d(lista_estudiantes, "E)Id")
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 4: #Quicksort
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  #Quicksort por promedio ascendente
                quicksort_a(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 1 and orden == 2:  #Quicksort por promedio descendente
                quicksort_d(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 1:  #Quicksort por edad ascendente
                quicksort_a(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 2:  #Quicksort por edad descendente
                quicksort_d(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 1:  #Quicksort por ID ascendente
                quicksort_a(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 2:  #Quicksort por ID descendente
                quicksort_d(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 5: #merge
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  #Mergesort por promedio ascendente
                mergesort_a(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 1 and orden == 2:  #Mergesort por promedio descendente
                mergesort_d(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 1:  #Mergesort por edad ascendente
                mergesort_a(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 2:  #Mergesort por edad descendente
                mergesort_d(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 1:  #Mergesort por ID ascendente
                mergesort_a(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 2:  #Mergesort por ID descendente
                mergesort_d(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 6: #shell
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  #Shellsort por promedio ascendente
                shellsort_a(lista_estudiantes, "D)Promedio")
            elif key == 1 and orden == 2:  #Shellsort por promedio descendente
                shellsort_d(lista_estudiantes, "D)Promedio")
            elif key == 2 and orden == 1:  #Shellsort por edad ascendente
                shellsort_a(lista_estudiantes, "B)Edad")
            elif key == 2 and orden == 2:  #Shellsort por edad descendente
                shellsort_d(lista_estudiantes, "B)Edad")
            elif key == 3 and orden == 1:  #Shellsort por ID ascendente
                shellsort_a(lista_estudiantes, "E)Id")
            elif key == 3 and orden == 2:  #Shellsort por ID descendente
                shellsort_d(lista_estudiantes, "E)Id")
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 7: #conteo
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  # conteo por promedio ascendente
                conteo_a(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 1 and orden == 2:  # conteo por promedio descendente
                conteo_d(lista_estudiantes, "D)Promedio")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 1:  # conteo por edad ascendente
                conteo_a(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 2 and orden == 2:  # Insercion por edad descendente
                conteo_d(lista_estudiantes, "B)Edad")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 1:  # conteo por ID ascendente
                conteo_a(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            elif key == 3 and orden == 2:  # conteo por ID descendente
                conteo_d(lista_estudiantes, "E)Id")
                mostrar(lista_estudiantes)
                system("pause")
                system("cls")
                ordenar()
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 8: #radix
            key,orden = opcion_de_ordernado()
            if key == 1 and orden == 1:  #Radixsort por promedio ascendente
                radixSort_a(lista_estudiantes, "D)Promedio")
            elif key == 1 and orden == 2:  #Radixsort por promedio descendente
                radixSort_d(lista_estudiantes, "D)Promedio")
            elif key == 2 and orden == 1:  #Radixsort por edad ascendente
                radixSort_a(lista_estudiantes, "B)Edad")
            elif key == 2 and orden == 2:  #Radixsort por edad descendente
                radixSort_d(lista_estudiantes, "B)Edad")
            elif key == 3 and orden == 1:  #Radixsort por ID ascendente
                radixSort_a(lista_estudiantes, "E)Id")
            elif key == 3 and orden == 2:  #Radixsort por ID descendente
                radixSort_d(lista_estudiantes, "E)Id")
            else:
                print("\n\nOpción inválida\n\n")
                opcion_de_ordernado()
        elif opcion == 9:
            menu()
        else:
            print("\n\nOpción inválida\n\n")
            ordenar()

    except ValueError:
        print("\n\nOpción inválida\n\n")
        ordenar()

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
                conseguido,iteraciones=busquedaBinaria(lista_estudiantes,"E)Id",num,0,len(lista_estudiantes),1)
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
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Vladimir explica los metodos de busqueda

#Funcion de busqueda secuencial
def busquedaSecuencial():
    try:
        num = int(input("\nIngrese el ID del elemento que desea buscar: "))
        for est in lista_estudiantes:
            if num == est["E)Id"]:
                print("Nombre: ", est["A)Nombre"], "- Edad: ", est["B)Edad"], "- Genero: ",est["C)Genero"], "- Promedio: ", est["D)Promedio"], "- ID: ", est["E)Id"])
            
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

#Funcion de busqueda binaria
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


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nacho explica el protocolo de uso de los metodos de ordenamiento

# Declaración de metodo de ordenamiento
def opcion_de_ordernado():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n4. Regresar al menu de ordenamiento.")
        opcion1 = int(input("Por favor ingrese una opción:"))
        if opcion1 == 4:
            ordenar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        opcion_de_ordernado()
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        system("pause")
        buscar()
        
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
        opcion2 = int(input("Por favor ingrese una opción:"))
            
    except ValueError:
        print("\n\nOpción inválida\n\n")
        opcion_de_ordernado()
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        system("pause")
        buscar()


    return opcion1,opcion2

# Burbuja ascendente        
def burbuja_a(lista, key):  
    tamano = len(lista) 
    i = 0
    while i < tamano:       # recorremos i de 0 hasta el tamaño -1
        j = 0
        while j < (tamano-1):                     # recorremos j de 0 hasta el tamaño -1 
            if lista[j+1][key] < lista[j][key]:     # si el valor en la posición j+1 de la lista es menor al valor anterior
                bucket = lista[j]                       # guardamos en una cubeta el valor anterior
                lista[j] = lista[j+1]                   # reemplazamos el valor que guardamos en la cubeta por el que le sigue
                lista[j+1] = bucket                     # colocamos en la posicion que sigue el valor que guardamos en la cubeta
            j += 1
        i += 1
    mostrar(lista)
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
    mostrar(lista)
    system("pause")
    system("cls")
    ordenar()
    
#Selección ascendente
def seleccion_a(lista, key):
    n = len(lista)
    for i in range(0, n):                              # recorremos i desde 0 hasta el tamaño de la lista
        posicion = i
        for j in range(0, n):                          # recorremos J desde 0 hasta el tamaño de la lista
            if lista[j][key] > lista[posicion][key]:    # si el valor en la posición j es mayor al valor en la posición i (que no cambia hasta que llega a n)
                posicion = j                                # la posición cambia su valor a j 
                temp = lista[i]                             # guardamos en una variable temporal el valor de la lista en la posición i (si es la primera iteración)
                lista[i] = lista[posicion]                  # entonces es el valor en la posición inical 
                lista[posicion] = temp                      # intercambiamos el valor que encontró mayor al inicial y el que está en la variable temporal toma su lugar
    mostrar(lista)
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
    mostrar(lista)
    system("pause")
    system("cls")
    ordenar()
    
#Incersión ascendente
def insercion_a(Arreglo,key):
    for i in range(1, len(Arreglo)):                                          #recorremos i de 1 hasta el tamaño de la lista
        copia_valor=Arreglo[i]                                                #copiamos el primer valor de la lista en una variable
        posicion=i                                                            #la variable posición toma el valor actual de i
        while (posicion>0) and (Arreglo[posicion-1][key] > copia_valor[key]): #mientras que la variable posicion > 0 y el arreglo en la posición i-1 es mayor al valor que 
            Arreglo[posicion] = Arreglo[posicion-1]                           # copiamos (el primer valor de la lista ([0])) 
            Arreglo[posicion-1] = copia_valor                                   #intercambiamos los valores 
            posicion=posicion-1                                                 #la variable posición se reduce en 1
        Arreglo[posicion]=copia_valor
    mostrar(Arreglo)
    system("pause")
    system("cls")
    ordenar()


#Incersión descendente
def insercion_d(Arreglo,key):
    for i in range(1, len(Arreglo)):
        copia_valor=Arreglo[i]
        posicion=i
        while (posicion>0) and (Arreglo[posicion-1][key] < copia_valor[key]):
            Arreglo[posicion] = Arreglo[posicion-1]
            Arreglo[posicion-1] = copia_valor
            posicion=posicion-1
        Arreglo[posicion]=copia_valor
    mostrar(Arreglo)
    system("pause")
    system("cls")
    ordenar()

#Función de apoyo para quicksort
def particionado(lista,key):             #El algoritmo Quick Sort consiste en elegir un elemento, llamado pivote y ordenar los 
    menores = []                         #elementos de tal forma que todos los menores queden a la izquierda y todos los mayores a la
    mayores = []                         #derecha, y a continuación ordenar de la misma forma cada una de las dos sublistas formadas.
    pivote = lista[0]
    for i in range(1,len(lista)):
        if lista[i][key] < pivote[key]:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores

#Quicksort ascendente
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
    for i in range(1, n):
        valor = lista[i]                    # toma el siguiente valor a ser isnertado
        posicion = i                        # indice  donde se insertará el vavlor

        while posicion > 0 and lista[posicion -1][key] > valor[key]: #si la posicion es mayor a 0 Y los numeros en la posicion[posicion - 1] es mayor a el valor
            lista[posicion] = lista[posicion -1]                     # numeros[posicion] = numeros[posicion - 1]
            posicion -= 1                                            # posicion decrementa en 1
            lista[posicion] = valor                                  # numeros[posicion] = valor
    mostrar(lista)
    system("pause")
    system("cls")
    ordenar()
    
#Shellsort decreciente
def shellsort_d(lista,key):
    n = len(lista)
    for i in range(1, n):
        valor = lista[i] 
        posicion = i 

        while posicion > 0 and lista[posicion -1][key] < valor[key]:
            lista[posicion] = lista[posicion -1] 
            posicion -= 1 
            lista[posicion] = valor
    mostrar(lista)
    system("pause")
    system("cls")
    ordenar()
    
#Mergesort Ascendente
def mergesort_a(lista,key):                     #La idea de los algoritmos de ordenación por mezcla es dividir la matriz 
    if len(lista) > 1:                          #por la mitad una y otra vez hasta que cada pieza tenga solo un elemento de 
        mitad = len(lista) // 2                 #longitud. Luego esos elementos se vuelven a juntar (mezclados) en orden de clasificación.
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

#conteo ascendente
def conteo_a (lista, key):
    maximo = 0
    for y in range(len(lista)):
        if lista[y][key] > maximo:      #sacamos el mayor valor de la lista
            maximo = lista[y][key]
    maximo += 1

    conteo= [0] * maximo               #creamos una lista llena de ceros dependiendo el número que nos haya proporcionado el mayor
    w = 0                                                 
    while w < len(lista):                         
        conteo[lista[w][key]] += 1     #contamos el número de veces que aparece un número en la lista original, en la posición que nos marca ese valor
        w+=1                           #vamos a colocar el número de apariciones (si el número 2 aparece 3 veces en la lista, en la posición 2 de la lista de ceros
                                        #se le sumará 3 porque aparece 3 veces, la lista de ceros queda como el conteo de veces que apareció ese número en la posición marcada)
    nueva_lista = []

    for w in range(maximo):                                        #recorremos con una variable de 0 hasta el núemro maximo que contiene nuestra lista y en las posiciones
        if conteo[w] >= 1:                                          #donde haya apariciones insertará en la lista de salida en orden el valor en el que se encuentra nuestra
            est = list(filter(lambda item: item[key] == w, lista))  #primer variable el número de veces que se supone aparece en la lista original desordenada
            nueva_lista.append(est)
    return nueva_lista
#conteo descendente 
def conteo_d (lista, key):
    maximo = 0
    for y in range(len(lista)):
        if lista[y][key] > maximo:
            maximo = lista_estudiantes[y][key]
    maximo += 1

    conteo= [0] * maximo
    w = 0                                                 
    while w < len(lista):                         
        conteo[lista[w][key]] += 1
        w+=1                                   

    nueva_lista = []

    for w in range(maximo):
        if conteo[w] == 1:
            est = list(filter(lambda item: item[key] == w, lista))
            nueva_lista.append(est)

    lista= nueva_lista
    lista.reverse()
    return lista

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

    mostrar(nueva_lista)
    system("pause")
    system("cls")
    ordenar()
#Función de apoyo para radixsort decreciente
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

def radixSort_d(lista, key):
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
    lista = nueva_lista
    lista.reverse()
    mostrar(lista)
    system("pause")
    system("cls")
    ordenar()


print("******Bienvenido*******")
estudiante={"A)Nombre": "Manuel Medrano", "B)Edad": 56, "C)Genero": "M", "D)Promedio": 96, "E)Id": 1}
lista_estudiantes.append(estudiante)

estudiante={"A)Nombre": "Leonel Castillo", "B)Edad": 45, "C)Genero": "M", "D)Promedio": 86, "E)Id": 2}
lista_estudiantes.append(estudiante)

estudiante={"A)Nombre": "Jose Luís Guerrero", "B)Edad":34, "C)Genero": "M", "D)Promedio":77, "E)Id": 3}
lista_estudiantes.append(estudiante)

estudiante={"A)Nombre": "Martín Andrade", "B)Edad":25, "C)Genero": "F", "D)Promedio":64, "E)Id": 4}
lista_estudiantes.append(estudiante)

estudiante={"A)Nombre": "Michael Jordan", "B)Edad":78, "C)Genero": "M", "D)Promedio":49, "E)Id": 5}
lista_estudiantes.append(estudiante)
menu()
