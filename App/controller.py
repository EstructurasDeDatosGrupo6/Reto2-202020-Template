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

def initCatalog():
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

def loadData(catalog, moviesfile, tagsfile, moviestagsfile):

    loadMovies(catalog, moviesfile)
    loadTags(catalog, tagsfile)
    loadMoviesTags(catalog, moviestagsfile)


def loadMovies(catalog, moviesfile):
    moviesfile= cf.data_dir + moviesfile
    input_file= cvs.DictReader(open(moviesfile))
    for movies in input_file:
        model.addMovie(catalog, movie)
        directors= movie["director"].split(",")
        for director in directors:
            model.addMovieDirector(catalog, director.strip(), movie)


def loadTags(catalog, tagsfile):
    tagsfile= cf.data_dir + tagsfile
    input_file= cvs.DictReader(open(tagsfile))
    for tag in input_file:
        model.addTag(catalog, tag)


def loadMoviesTags(catalog, moviestagsfile):
    moviestagsfile= cf.data_dir + moviestagsfile
    input_file = cvs.DictReader(open(moviestagsfile))
    for tag in input_file:
        model.addMovieTag(catalog, tag)


        
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














