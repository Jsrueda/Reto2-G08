﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(maptype, numelements):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(maptype, numelements) 
    return control

def selector_maptype(input):
    if input == "1":
        maptype = "CHAINING"
    elif input == "2":
        maptype = "PROBING"
    return maptype

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, filename):
    """
    Carga los datos
    """
    size = controller.load_data(control, filename)
    return size

def print_maptypes():
    print("1. CHAINING")
    print("2. PROBING")

def print_opciones_archivo():
    print('1. 0.5% ')
    print('2. 5% ')
    print('3. 10% ')
    print('4. 20% ')
    print('5. 30% ')
    print('6. 50% ')
    print('7. 80% ')
    print('8. 100% ') 

def seleccionar_archivo(opt):
    filename = "Salida_agregados_renta_juridicos_AG"
    filename_modificado = ''
    porcentaje_seleccionado = ''
    if opt == 1:
        filename_modificado = filename + "-small.csv"
        porcentaje_seleccionado = '0.5%'
    if opt == 2:
        filename_modificado = filename + "-5pct.csv"
        porcentaje_seleccionado = '5%'
    elif opt == 3:
        filename_modificado = filename + "-10pct.csv"
        porcentaje_seleccionado = '10%'
    elif opt == 4:
        filename_modificado = filename + "-20pct.csv"
        porcentaje_seleccionado = '20%'
    elif opt == 5:
        filename_modificado = filename + "-30pct.csv"
        porcentaje_seleccionado = '30%'
    elif opt == 6:
        filename_modificado = filename + "-50pct.csv"
        porcentaje_seleccionado = '50%'
    elif opt == 7:
        filename_modificado = filename + "-80pct.csv"
        porcentaje_seleccionado = '80%'
    elif opt == 8:
        filename_modificado = filename + "-large.csv"
        porcentaje_seleccionado = '100%'

    return filename_modificado, porcentaje_seleccionado

def print_opt1():
    print_maptypes()
    entrada = input("Elija el tipo de mapa que desea: ")
    maptype = selector_maptype(entrada)
    print("\n")
    print_opciones_archivo()
    opt = int(input("Elija el porcentaje del archivo a cargar: "))
    control = new_controller(maptype, 0)
    filename, porcentaje = seleccionar_archivo(opt)
    print(f"Cargando el {porcentaje} de la información")
    size = load_data(control, filename)
    print("Total de filas cargadas:" + str(size))
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
#control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                control = print_opt1()
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
