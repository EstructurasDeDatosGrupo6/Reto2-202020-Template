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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator
assert config
from time import process_time 

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def cmpProducers(key,element):
    if (int(key) == int(me.getKey(element))):
        return 0
    elif (int(key) > int(me.getKey(element))):
        return 1
    else:
        return -1
    
def newCatalog():
    t1_start = process_time()
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
                'moviesCast': None,
               'moviesIds': None,
               'directors': None,
               'tags': None,
               'tagIds': None,
               'years': None,
               'producerMovies': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesCast'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesIds'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['directors'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    catalog['tags'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareTagNames)
    catalog['tagIds'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareTagIds)
    catalog['years'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapYear)
    catalog['producerMovies'] = mp.newMap(10000,maptype='PROBING',loadfactor=0.5,comparefunction=cmpProducers)
    catalog['casting']=lt.newList('SINGLE_LINKED', None)
    catalog['listaFinal']=lt.newList('SINGLE_LINKED', None)
    #t1_stop = process_time() #tiempo final
    #print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 
   
    return catalog


def newDirector(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "movies": None,  "average_rating": 0}
    author['name'] = name
    author['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return author


def newTagMovie(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_movies': 0,
           'movies': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['movies'] = lt.newList()
    return tag


# Funciones para agregar informacion al catalogo


def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    #mp.put(catalog['moviesIds'], movie['id'], movie)
    #addMovieYear(catalog, movie)


def addMovieYear(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    years = catalog['years']
    pubyear = movie['release_date']
    pubyear=pubyear[6:len(pubyear)]
    pubyear = int(float(pubyear))
    existyear = mp.contains(years, pubyear)
    if existyear:
        entry = mp.get(years, pubyear)
        year = me.getValue(entry)
    else:
        year = newYear(pubyear)
        mp.put(years, pubyear, year)
    lt.addLast(year['movies'], movies)


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "movies": None}
    entry['year'] = pubyear
    entry['movies'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry


def addMovieDirector(catalog, directorname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    # directors = catalog['directors']
    # existdirector = mp.contains(directors, directorname)
    # if existdirector:
    #     entry = mp.get(directors, directorname)
    #     director = me.getValue(entry)
    # else:
    #     director = newDirector(directorname)
    #     mp.put(directors, directorname, director)
    # lt.addLast(director['movies'], movie)

    # directavg = directors['vote_average']
    # movieavg = movie['vote_average']
    # if (directhavg == 0.0):
    #     directors['vote_average'] = float(movieavg)
    # else:
    #     directors['vote_average'] = (directavg + float(movieavg)) / 2

def addCasting(catalog, movie):
    lt.addLast(catalog['casting'], movie)

def addInfo(catalog, movie):
    lt.addLast(catalog['listaFinal'], movie)

def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagMovie(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)


def addMovieTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    movieid = tag['id']
    castingid = tag['id']
    entry = mp.get(catalog['tagIds'], castingid)

    if entry:
        tagmovie = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagmovie['value']['total_books'] += 1
        tagmovie['value']['count'] += int(tag['count'])
        movie = mp.get(catalog['moviesIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['movies'], book['value'])


# ==============================
# Funciones de consulta
# ==============================

def moviesFromproducer (productora, CatalogMovies):
    
    lst_productora = lt.newList(datastructure='SINGLE_LINKED',cmpfunction=None)
    iter = listiterator.newIterator(CatalogMovies["movies"])
    while listiterator.hasNext(iter):
        movie = listiterator.next(iter)
        if movie["production_companies"] == productora:
            lt.addLast(lst_productora,movie)
    
    return lst_productora

def moviesFromdirector(director, CatalogMovies):
    lst_director = lt.newList(datastructure='SINGLE_LINKED',cmpfunction=None)
    iter = listiterator.newIterator(CatalogMovies["movies"])
    while listiterator.hasNext(iter):
        movie = listiterator.next(iter)
        if movie["director_name"] == director:
            lt.addLast(lst_director,movie)
    return lst_director

def moviesByActor(actor, CatalogMovies):
    lst_actor = lt.newList(datastructure='SINGLE_LINKED',cmpfunction=None)
    iter = listiterator.newIterator(CatalogMovies["movies"])
    while listiterator.hasNext(iter):
        movie = listiterator.next(iter)
        if movie ["actor1_name"] or movie ["actor2_name"] or movie ["actor3_name"] or movie ["actor4_name"] or movie ["actor5_name"] == actor:
            lt.addLast(lst_actor,movie)
    return lst_actor

def moviesByGenre(genero, CatalogMovies):
    lst_genero= lt.newList(datastructure="SINGLE_LINKED", cmpfunction=None)
    iter=listiterator.newIterator(CatalogMovies["listaFinal"])
    while listiterator.hasNext(iter):
        movie = listiterator.next(iter)
        if movie["genres"] == genero:
            lt.addLast(lst_genero,movie)
    
    return lst_genero

def moviesByCountry(pais, CatalogMovies):
    lst_paises=  lt.newList(datastructure="SINGLE_LINKED", cmpfunction=None)
    iter=listiterator.newIterator(CatalogMovies['listaFinal'])
    while listiterator.hasNext(iter):
        movie = listiterator.next(iter)
        if movie["production_countries"] == pais:
            lt.addLast(lst_paises,movie)
            
    
    return lst_paises
        






# ==============================
# Funciones de Comparacion
# ==============================


def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    directentry = me.getKey(director)
    if (keyname == directentry):
        return 0
    elif (keyname > directentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0





