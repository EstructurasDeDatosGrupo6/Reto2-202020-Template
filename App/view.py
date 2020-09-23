"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """



import sys
sys.setrecursionlimit(1500)

import config
from DISClib.ADT import list as lt
from App import controller
from DISClib.DataStructures import listiterator
assert config
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me





"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
movies = 'SmallMoviesDetailsCleaned.csv'
moviesCasting = 'MoviesCastingRaw-small.csv'


# ___________________________________________________
#  Funciones para imprimir la información de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido, por favot ejecute las primeras dos opciones antes de continuar")
    print("1- Inicializar catalogo")
    print("2- Cargar lista de peliculas ")
    print("3- Conocer productoras ")
    print("4- Conocer a un actor")
    print("5- Entender un género cinmatográfico")
    print("6- Encontrar películas por país")


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
       

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont,movies,moviesCasting)
        #print('Peliculas cargadas: ' + str(controller.moviesSize(cont)))
        #print('Autores cargados: ' + str(controller.authorsSize(cont)))
        #print('Géneros cargados: ' + str(controller.tagsSize(cont)))
        

    elif int(inputs[0]) == 3:
        print("Cargando datos...")
        productora = str(input("Ingrese la productora: "))
        retorno = controller.getMoviesByProducer(productora,cont)
        promedio = 0
        suma = 0
        iter = listiterator.newIterator(retorno)
        while listiterator.hasNext(iter):
            movie = listiterator.next(iter)
            print(movie["title"])
            suma += float(movie["vote_average"])
        promedio = suma/lt.size(retorno)
        print("Cantidad : ",lt.size(retorno))
        print("Promedio: ",str(promedio))
        
        
    # elif int(inputs[0]) == 4:
        
        
    elif int(inputs[0]) == 5:
        
        genero=str(input("Ingrese el género a conocer: "))
        print("GENERO"+"\t"+"\t"+ "PELÍCULA" +"\t"+"\t"+ "\t"+ "VOTE_COUNT"+"\n"+\
            "------------------------------------------------------------")
        retorno=controller.getMoviesByGenre(genero, cont)
        promedio=0
        suma=0
        iter= listiterator.newIterator(retorno)
        while listiterator.hasNext(iter):
            movie=listiterator.next(iter)
            suma+=int(movie["vote_count"])
            print(movie["genres"]+"\t"+"\t"+ movie["title"]+"\t"+"\t"+ "\t"+(movie["vote_average"]))
        promedio=suma/lt.size(retorno)
        
        print("TOTAL PELICULAS: "+ str(lt.size(retorno)))
        print("PROMEDIO DE VOTOS: "+ str(promedio)+"\n")
    
    elif int(inputs[0]) == 6:
        pais=str(input("Ingrese el país de interés: "))
        print("AÑO" +"\t"+ "\t"+"PELÍCULA"+"\t"+ "\t"+"DIRECTOR"+"\n"+\
            "------------------------------------------------------")
        retorno=controller.getMoviesByCountry(pais, cont)
        iter= listiterator.newIterator(retorno)
        while listiterator.hasNext(iter):
            movie=listiterator.next(iter)
            anio=str(movie['release_date'])
            anio=anio[6:10]
            print(anio+"\t"+"\t"+movie['title']+"\t"+"\t"+"\t"+movie["director_name"]) 
        
    else:
        sys.exit(0)
sys.exit(0)
