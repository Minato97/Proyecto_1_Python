from os import system
lista_estudiantes=[]

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


def crear():
    estudianteT=Estudiantes(input("Nombre:"),int(input("Edad:")),input("Genero:"),float(input("Promedio:")))
    lista_estudiantes.append(estudianteT)
    #Estudiantes.contadorEstudiantes=lista_estudiantes.index(estudianteT)+1

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

def modificar():
    try:
        elemento=int(input("Ingrese el ID del elemento que desea modificar: "))
        estudianteT = Estudiantes(input("Nombre:"),int(input("Edad:")),input("Genero:"),float(input("Promedio:")))
        lista_estudiantes[elemento-1]=estudianteT
        Estudiantes.contadorEstudiantes=elemento
        
    except IndexError:
        print("\n\nNo existe registro con el ID ingresado\n\n")
        modificar()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        modificar()

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
        else:
            print("\n\nOpción inválida\n\n")
            menu()
    except ValueError:
        print("\n\nOpción inválida\n\n")
        menu()

def burbuja():
    print("Burbuja")
def seleccion():
    print("Selección")
def insercion():
    print("Inserción")
def quicksort():
    print("QuickSort")
def mergesort():
    print("MergeSort")
def shellsort():
    print("ShellSort")
def countsort():
    print("CountSort")
def radixsort():
    print("RadixSort")

print("******Bienvenido*******")
menu()
