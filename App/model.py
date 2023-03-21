"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs_map(maptype, numelements):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    adt = mp.newMap(maptype= maptype, numelements= numelements)
    return adt

def new_data_structs_list(data_type, cmpfunction_):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=data_type,
                                     cmpfunction=cmpfunction_)

    return data_structs

def datos_filtrados(dict_anios, llaves_a_incluir):
    list_values = []
    #Extrae los tres primeros y últimos datos de cada año
    #Ordena los datos de cada año por Código de actividad económica
    datos_filtrados = dict_anios.copy()
    
    for año in datos_filtrados:
        #sort(datos_filtrados[año], 'MergeSort', cmp_impuestos_by_CAE)
        list_complete = []
        first_three = lt.subList(datos_filtrados[año]['data'], 1, 3) 
          
        last_three = lt.subList(datos_filtrados[año]['data'], datos_filtrados[año]['data']['size']-2, 3)
        
        for i in range(3):
            dato = lt.getElement(first_three, i+1)
            list_complete.append(dato)
        
        for i in range(3):
            dato = lt.getElement(last_three, i+1)
            list_complete.append(dato)
        list_values.extend(list_complete)
        
    list_values_info = []
    #Añade en una lista otra lista que contiene la informacion de cada dato. Esto es para usar tabulate en view
    for data in list_values:
        data_copy = data['info'].copy()
        data_copy_2 ={}
        for llave in data_copy:
            if llave in llaves_a_incluir:
                data_copy_2[llave]=data_copy[llave]
        list_data = list(data_copy_2.values())
        list_values_info.append(list_data)
    return list_values_info 


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])

# Funciones para agregar informacion al modelo

def add_data_list(data_structs, data, id):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data_list(id, data)
    lt.addLast(data_structs["data"], d)

    return data_structs

# Funciones para creacion de datos

def new_data_list(id=0, info=""):
    """
    Crea una nueva estructura para modelar los datos
        data["id"] = id
    data["info"] = info
    """
    data = {'id': id, "info": info}

    return data

def put(map, key, value):
    """
    Añade al map una pareja llave valor
    """
    mp.put(map, key, value)
    return map
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2): 
    """ Devuelve verdadero (True) si el año de impuesto1 es menor 
    que el de impuesto2, en caso de que sean iguales tenga en cuenta 
    el código de la actividad económica, de lo contrario devuelva falso (False). 
    
    Args: 
        impuesto1: información del primer registro de impuestos que incluye el “Año” 
            y el “Código actividad económica” 
        impuesto2: información del segundo registro de 
            impuestos que incluye el “Año” y el “Código actividad económica” """ 
            
    if int(impuesto1['info']['Año'])<int(impuesto2['info']['Año']):
        return True
    elif int(impuesto1['info']['Año'])==int(impuesto2['info']['Año']):
        return sort_criteria_1(impuesto1, impuesto2)
    else:
        return False 
    
# Funciones de ordenamiento
def organizar_por_anio(map, list_datos):
    """
       Retorna un Map el cual tiene como llaves los diferentes años y 
       como valores un DT lista con sus datos ordenados por codigo act. económica
       
        if map_anios["type"] == "CHAINING":
        
        return map_anios
    """
    map_anios = map["model"]
    for dato in list_datos["data"]["elements"]:
        mp.put(map_anios, dato["info"]["Año"], dato["info"])
    #Añade al map las llaves con los años
    anios = mp.keySet(map_anios)["elements"]
    for i in anios:
        dt_anio = new_data_structs_list("ARRAY_LIST", cmp_impuestos_by_anio_CAE)
        for dato in list_datos["data"]["elements"]:
            if dato["info"]["Año"] == i:
                add_data_list(dt_anio, dato["info"], i)
            sort(dt_anio, "MergeSort", cmp_impuestos_by_anio_CAE)
            mp.put(map_anios, i, dt_anio)
    return map_anios



def sort_criteria_1(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Usado para la comparación de códigos de actividad económica que tienen varios valores.
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    codigo_1 = data_1['info']['Código actividad económica'] 
    codigo_2 = data_2['info']['Código actividad económica']
    centinela = True
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    codigo_1_final = ""
    i=0
    while i < len(codigo_1) and centinela:
        if codigo_1[i] in digitos:
            codigo_1_final = codigo_1_final + codigo_1[i]
        else:
            centinela = False
        i+=1
    centinela = True
    codigo_2_final = ""
    i=0
    while i < len(codigo_2) and centinela:
        if codigo_2[i] in digitos:
            codigo_2_final = codigo_2_final + codigo_2[i]
        else:
            centinela = False
        i+=1
    return int(codigo_1_final) <= int(codigo_2_final)

def sort(data_structs, algorithm, cmpfunction):
    """
    Función encargada de ordenar la lista con los datos
    """
    if algorithm == 'Selection':
        se.sort(data_structs["data"], cmpfunction)
    elif algorithm == 'Insertion':
        ins.sort(data_structs["data"], cmpfunction)
    elif algorithm == 'Shell':
        sa.sort(data_structs["data"], cmpfunction)
    elif algorithm == "MergeSort":
        merg.sort(data_structs["data"], cmpfunction)
    elif algorithm == "QuickSort":
        quk.sort(data_structs["data"], cmpfunction)
