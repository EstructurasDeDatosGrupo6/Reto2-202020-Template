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

import config as cf
from App import model
import csv
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(catalog, moviesfile,moviesCasting):
    loadMovies(catalog,moviesfile, moviesCasting)
    loadCasting(catalog, moviesCasting)
    unirListas(catalog, catalog['movies'], catalog['casting'])
    

def loadMovies(catalog, moviesfile,moviesCasting):
    moviesfile= cf.data_dir + moviesfile
    with open(moviesfile, newline='',encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';')
        for movie in reader:
            model.addMovie(catalog, movie)

def loadCasting(catalog, moviesCasting):
    moviescast= cf.data_dir+ moviesCasting
    with open(moviescast, newline='',encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';')
        for movie in reader:
            model.addCasting(catalog, movie)

def unirListas(catalog, lista1, lista2):
    
    iter1=it.newIterator(lista1)
    
    while it.hasNext(iter1):
        movie=it.next(iter1)
        iter2=it.newIterator(lista2)
        while it.hasNext(iter2):
            cast=it.next(iter2)
            if movie['id']==cast['id']:
                moviesInfo=model.addInfo(catalog, {**movie, **cast})
                

    return moviesInfo



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def moviesSize(catalog):
    return model.moviesSize(catalog)


def directorsSize(catalog):
    return model.directorsSize(catalog)

def tagsSize(catalog):
    return model.tagsSize(catalog)

def getMoviesByDirector(catalog, directorname):
    directorinfo= model.getMoviesByDirector(catalog, directorname)
    return directorinfo

def getMoviesByTag(catalog, tagname):
    movies= model.getMoviesByTag(catalog, tagname)
    return movies

def getMoviesByYear(catalog, year):
    movies= model.getMoviesByYear(catalog, year)
    return movies

def getMoviesByProducer (producer,catalog):
    movies = model.moviesFromproducer(producer,catalog)
    return movies
def getMoviesByDirector(director,catalog):
    movies = model.moviesFromdirector(director,catalog)
    return movies 
def getMoviesByActor(actor,catalog):
    movies = model.moviesFromActor(actor, catalog)
    return movies 

def getMoviesByGenre (genre, catalog):
    movies=model.moviesByGenre(genre, catalog)
    return movies

def getMoviesByCountry(country, catalog):
    movies=model.moviesByCountry(country, catalog)
    return movies













