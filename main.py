from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

df = pd.read_csv("data_con_EDA.csv")


app = FastAPI()

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes):
    '''Determina la cantidad de películas que se estrenaron en el mes dado'''
   
    peliculas_mes = df['id'][df['release_month'] == mes].count()
    return f"{int(peliculas_mes)} es la cantidad de películas que fueron estrenadas en el mes de {mes}"

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia):
    '''Determina la cantidad de películas que se estrenaron en el día dado'''
   
    peliculas_dia = df['id'][df['release_day'] == dia].count()
    return f"{int(peliculas_dia)} es la cantidad de películas que fueron estrenadas en los días {dia}"

@app.get("/score_titulo/{titulo_de_la_filmacion}")
def score_titulo(titulo_de_la_filmacion):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.'''

    titulo = titulo_de_la_filmacion
    anio_estreno = df["release_year"][df["title"] == titulo_de_la_filmacion]
    score = df["popularity"][df["title"] == titulo_de_la_filmacion]

    return f"La película {str(titulo)} fue estrenada en el año {int(anio_estreno)} con un score/popularidad de {float(score)}"

@app.get("/votos_titulo/{titulo_de_la_filmacion}")
def votos_titulo(titulo_de_la_filmacion):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.'''

    titulo = titulo_de_la_filmacion
    anio_estreno = int(df["release_year"][df["title"] == titulo_de_la_filmacion])
    cantidad_votos = int(df["vote_count"][df["title"] == titulo_de_la_filmacion])
    votos_promedio = float(df["vote_average"][df["title"] == titulo_de_la_filmacion])

    if cantidad_votos < 2000:
        return "Esta peliculas no cumple con la valoracion necesaria para una opinion objetiva"

    return f"La película {titulo} fue estrenada en el año {anio_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {votos_promedio}"

@app.get("/get_actor/{get_actor}")
def get_actor(nombre_actor):
    
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.'''

    contador = 0
    ganancia = 0
    retorno = 0

    for i in range(df["cast_names"].size):
        if nombre_actor in df["cast_names"][i]:
            ganancia += df.iloc[i, 10]
            retorno += df.iloc[i, 20]
            contador += 1
            prom_retorno = retorno / contador


    return f"El actor {nombre_actor} ha participado de {contador} filmaciones, el mismo ha conseguido un retorno de {ganancia} con un promedio de {prom_retorno} por filmación"

@app.get("/get_director/{get_director}")
def get_director(nombre_director): 
    '''Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''

    retorno = 0

    titulo_pelicula = ""
    fecha_lanzamiento = ""
    retorno_ind = 0
    costo = 0
    peliculas = []

    for i in range(df["crew_names"].size):
        if nombre_director in df["crew_names"][i]:
            retorno += df.iloc[i, 10]

            titulo_pelicula =  peliculas.append(df.iloc[i, 14])
            fecha_lanzamiento =  peliculas.append(df.iloc[i, 9])
            retorno_ind =  peliculas.append(df.iloc[i, 10])
            costo = peliculas.append(df.iloc[i, 1])

    return f"Para el Director {nombre_director} el retorno a traves de su carrera fue de {retorno}, y aca informacion sobre sus peliculas: \n {peliculas}"


@app.get("/recomendacion/{titulo}")
def recomendacion(titulo):

    num_recommendations=5
    # Cargar los datos de películas
    movies = pd.read_csv("data_con_EDA.csv")

    # Crear una matriz TF-IDF a partir de los títulos de las películas
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(movies["title"].values.astype('U'))

    # Entrenar un modelo de clustering (K-Means)
    kmeans = KMeans(n_clusters=10, random_state=42)
    kmeans.fit(tfidf_matrix)

    # Encontrar el cluster más cercano al título de la película proporcionado
    movie_vector = vectorizer.transform([titulo])
    cluster_label = kmeans.predict(movie_vector)[0]

    # Filtrar las películas en el mismo cluster que la película de interés
    cluster_movies = movies[kmeans.labels_ == cluster_label]

    # Excluir la película de interés de las recomendaciones
    cluster_movies = cluster_movies[cluster_movies["title"] != titulo]

    # Ordenar las películas por su similitud al título de interés
    cluster_movies["similitud"] = kmeans.transform(vectorizer.transform(cluster_movies["title"].values.astype('U'))).sum(axis=1)
    cluster_movies = cluster_movies.sort_values("similitud", ascending=False).head(num_recommendations)

    # Devolver las películas recomendadas
    recommendations = cluster_movies["title"].tolist()
    return recommendations