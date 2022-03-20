from os import system
#Declaración de lista vacia
lista_estudiantes=[]

#Declaración de clase con constructor y metodo de mostrar datos
class Estudiantes:
    contadorEstudiantes=1
    def __init__(self, nombre="", edad=0, genero="", promedio=0.0):
        self.__Nombre=nombre
        self.__Edad=edad
        self.__Genero=genero
        self.__Promedio = promedio
        self.__ID = Estudiantes.contadorEstudiantes
        
    
    
    def mostrar(self):
        print("\nNombre: ",self.__Nombre, " |Edad: ",self.__Edad," |Genero: ",self.__Genero,"|Promedio: ",self.__Promedio,"|ID: ",self.__ID)
    def getPromedio(self):
        return self.__Promedio
#Declaración de metodo crear
def crear():
    estudianteT=Estudiantes(input("Nombre:"),int(input("Edad:")),input("Genero:"),float(input("Promedio:")))
    lista_estudiantes.append(estudianteT)
    
#Declaración de metodo eliminar
def eliminar():
    try:
        elemento=int(input("Ingrese el ID del elemento que desea eliminar: "))
        removedElement= lista_estudiantes.pop(elemento-1)
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        eliminar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        eliminar()
        

#Declaración de metodo modificar
def modificar():
    try:
        elemento=int(input("Ingrese el ID del elemento que desea modificar: "))
        Estudiantes.contadorEstudiantes=elemento
        estudianteT = Estudiantes(input("Nombre:"),int(input("Edad:")),input("Genero:"),float(input("Promedio:")))
        
        lista_estudiantes[elemento-1]=estudianteT
        
        
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        modificar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        modificar()

#Declaración de metodo ordenar
def ordenar():
    try:
        print("**********Menú de Ordenamiento*********")
        print("Presione el número correspondiente según el método que desea implementar:\n\n1. Burbuja.\n2. Selección .\n3. Inserción .\n4. QuickSort .\n5. MergeSort.\n6. ShellSort.\n7. CountSort.\n8. RadixSort.")
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:
            burbuja()
        elif opcion==2:
            seleccion()
        elif opcion==3:
            insercion()
        elif opcion==4:
            quicksort()
        elif opcion==5:
            mergesort()
        elif opcion==6:
            shellsort()
        elif opcion==7:
            countsort()
        elif opcion==8:
            radixsort()
        else:
            print("\n\nOpción inválida\n\n")
            ordenar()
                    
    except ValueError:
        print("\n\nOpción inválida\n\n")
        ordenar()
        
#Declaración de menú de busqueda
def buscar():
    try:
        print("**********Menú de Búsqueda*********")
        print("Presione el número correspondiente según el método de búsqueda que desea implementar:\n\n1. Búsquea secuencial con centinela.\n2. Búsqueda binaria.\n")
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:
            busquedaSecuencial()
        elif opcion==2:
            busquedaBinaria()
        else:
            print("\n\nOpción inválida\n\n")
            buscar()
                    
    except ValueError:
        print("\n\nOpción inválida\n\n")
        buscar()


#Declaración de funcion de menú principal
def menu():
    print("\n")
    system("pause")
    system("cls")
    try:
        
        print("\n\n**********Menú Principal*********")
        print("Presione el número correspondiente según lo que desee hacer:\n\n1. Crear un registro.\n2. Eliminar un registro.\n3. Modificar un registro.\n4. Mostrar registros.\n5. Ordenar los registros.")
        opcion=int(input("\nPor favor ingrese una opción:"))

        if opcion==1:
            crear()
            Estudiantes.contadorEstudiantes+=1
            menu()
        elif opcion==2:
            print("\nLos registros actuales son:\n")
            for estudiante in lista_estudiantes:
                estudiante.mostrar()
            eliminar()
            print("\nEliminado exitosamente\nLa lista actualizada se muestra a continuación: \n")
            for estudiante in lista_estudiantes:
                estudiante.mostrar()
            menu()
        elif opcion==3:
            print("\nLos registros actuales son:\n")
            for estudiante in lista_estudiantes:
                estudiante.mostrar()
            modificar()
            print("\nLa lista actualizada se muestra a continuación: \n")
            for estudiante in lista_estudiantes:
                estudiante.mostrar()
            menu()
        elif opcion==4:
            print("\nLos registros actuales son:\n")
            for estudiante in lista_estudiantes:
                estudiante.mostrar()
            menu()
        elif opcion==5:
            ordenar()
        elif opcion==6:
            buscar()
        else:
            print("\n\nOpción inválida\n\n")
            menu()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        menu()


#Declaración de metodo de ordenamiento
def burbuja():
    print("\n")
    system("cls")
    try:
        print("Presione el número correspondiente según el atributo al que desee implementar el método:\n\n1. Ordenar por promedio.\n2. Ordenar por edad.\n3. Ordenar por ID.\n")
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #Burbuja por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Burbuja por promedio ascendente
                    tamano = len(lista_estudiantes)
                    i= 0
                    while i < tamano:
                        j= 0
                        while j < (tamano-1):
                            if lista_estudiantes[j+1].Estudiantes.getPromedio() < lista_estudiantes[j].Estudiantes.getPromedio():
                                bucket = lista_estudiantes[j]
                                lista_estudiantes[j] = lista_estudiantes[j+1]
                                lista_estudiantes[j+1] = bucket
                        j+= 1
                    i+= 1
                    k=0
                    for k in range(k,tamano):
                        Estudiantes.mostrar() 
                            
                
                elif opcion==2: #Burbuja por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Burbuja por edad ascendente
                    pass
                elif opcion==2: #Burbuja por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Burbuja por ID ascendente
                    pass
                elif opcion==2: #Burbuja por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    burbuja()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                burbuja()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #Selección por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Selección por promedio ascendente
                    pass
                elif opcion==2: #Selección por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Selección por edad ascendente
                    pass
                elif opcion==2: #Selección por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #Selección por ID ascendente
                    pass
                elif opcion==2: #Selección por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    seleccion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                seleccion()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #insercion por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #insercion por promedio ascendente
                    pass
                elif opcion==2: #insercion por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #insercion por edad ascendente
                    pass
                elif opcion==2: #insercion por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #insercion por ID ascendente
                    pass
                elif opcion==2: #insercion por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    insercion()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                insercion()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #quicksort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #quicksort por promedio ascendente
                    pass
                elif opcion==2: #quicksort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #quicksort por edad ascendente
                    pass
                elif opcion==2: #quicksort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #quicksort por ID ascendente
                    pass
                elif opcion==2: #quicksort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    quicksort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                quicksort()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #mergesort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #mergesort por promedio ascendente
                    pass
                elif opcion==2: #mergesort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #mergesort por edad ascendente
                    pass
                elif opcion==2: #mergesort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #mergesort por ID ascendente
                    pass
                elif opcion==2: #mergesort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    mergesort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                mergesort()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #shellsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #shellsort por promedio ascendente
                    pass
                elif opcion==2: #shellsort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #shellsort por edad ascendente
                    pass
                elif opcion==2: #shellsort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #shellsort por ID ascendente
                    pass
                elif opcion==2: #shellsort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    shellsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                shellsort()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #countsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #countsort por promedio ascendente
                    pass
                elif opcion==2: #countsort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #countsort por edad ascendente
                    pass
                elif opcion==2: #countsort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #countsort por ID ascendente
                    pass
                elif opcion==2: #countsort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    countsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                countsort()
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
        opcion=int(input("Por favor ingrese una opción:"))

        if opcion==1:  #radixsort por promedio
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #radixsort por promedio ascendente
                    pass
                elif opcion==2: #radixsort por promedio descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()
                
        elif opcion==2:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #radixsort por edad ascendente
                    pass
                elif opcion==2: #radixsort por edad descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()
                
        elif opcion==3:
            print("\n")
            system("cls")
            try:
                print("Presione el número correspondiente según el orden que desea implementar:\n\n1. Orden Ascendente.\n2. Orden Descendente.\n")
                opcion=int(input("Por favor ingrese una opción:"))

                if opcion==1: #radixsort por ID ascendente
                    pass
                elif opcion==2: #radixsort por ID descendente
                    pass
                else:
                    print("\n\nOpción inválida\n\n")
                    radixsort()
                    
            except ValueError:
                print("\n\nOpción inválida\n\n")
                radixsort()
        else:
            print("\n\nOpción inválida\n\n")
            radixsort()
                    
    except ValueError:
        print("\n\nOpción inválida\n\n")
        radixsort() 
    
def busquedaSecuencial():
    print("encontrado")
def busquedaBinaria():
    print("encontrado")
    


print("******Bienvenido*******")
menu()