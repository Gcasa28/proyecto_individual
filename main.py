from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

df = pd.read_csv("data_con_EDA.csv")
movies = pd.read_csv("movies.csv")

app = FastAPI()

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes):
    '''Determina la cantidad de películas que se estrenaron en el mes dado'''
   
    peliculas_mes = df['id'][df['release_month'] == mes].count()
    return {'mes': mes, 'cantidad': int(peliculas_mes)}

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia):
    '''Determina la cantidad de películas que se estrenaron en el día dado'''
   
    peliculas_dia = df['id'][df['release_day'] == dia].count()
    return {'dia': dia, 'cantidad': int(peliculas_dia)}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia):
    '''Determina la cantidad de películas que pertenece a la franquicia dada, la ganancia total y la ganancia promedio'''
   
    cantidad_peliculas = df['id'][df['belongs_to_collection'] == franquicia].count()
    ganacia_total = np.sum(df['return'][df['belongs_to_collection'] == franquicia])
    ganacia_promedio = np.mean(df['return'][df['belongs_to_collection'] == franquicia])
    return {'franquicia': franquicia, 'cantidad': int(cantidad_peliculas), 'ganancia_total': ganacia_total, 'ganancia_promedio': ganacia_promedio}

@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais):
    '''Determina la cantidad de películas producidas en el país dado'''

    cantidad_peliculas = 0
    n = df['production_countries'].size
    for i in range(n):
        if pais in df.iloc[i, 8]:
            cantidad_peliculas += 1
    return {'pais': pais, 'cantidad': cantidad_peliculas}

@app.get("/productoras/{productora}")
def productoras(productora):
    '''Determina la ganancia total y la cantidad de películas de la productora dada'''

    ganancia_total = 0
    cantidad_peliculas = 0
    n = df['production_companies'].size
    for i in range(n):
        if productora in df.iloc[i, 7]:
            ganancia_total += df.iloc[i, 20]
            cantidad_peliculas += 1
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad_peliculas}


@app.get("/pelicula/{pelicula}")
def retorno(pelicula):
    '''Determina la inversion, la ganancia, el retorno de inversión y el año en el que se lanzo la pelicula dada'''

    inversion = 0
    ganancia = 0
    retorno = 0
    anio = 0
    n = df['title'].size
    for i in range(n):
        if df.iloc[i, 15] == pelicula:
            inversion += df.iloc[i, 1]
            ganancia += df.iloc[i, 10]
            retorno += df.iloc[i, 20]
            anio = df.iloc[i, 17]
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'anio':int(anio)}

@app.get("/recomendacion/{titulo_pelicula}")
def recomendacion(titulo_pelicula):

    num_recommendations=5
    # Crear una matriz TF-IDF a partir de los títulos de las películas
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(movies["title"])

    # Entrenar un modelo de clustering (K-Means)
    kmeans = KMeans(n_clusters=10, random_state=42)
    kmeans.fit(tfidf_matrix)

    # Encontrar el cluster más cercano al título de la película proporcionado
    movie_vector = vectorizer.transform([titulo_pelicula])
    cluster_label = kmeans.predict(movie_vector)[0]

    # Filtrar las películas en el mismo cluster que la película de interés
    cluster_movies = movies[kmeans.labels_ == cluster_label]

    # Excluir la película de interés de las recomendaciones
    cluster_movies = cluster_movies[cluster_movies["title"] != titulo_pelicula]

    # Ordenar las películas por su similitud al título de interés
    cluster_movies["similitud"] = kmeans.transform(vectorizer.transform(cluster_movies["title"])).sum(axis=1)
    cluster_movies = cluster_movies.sort_values("similitud", ascending=False).head(num_recommendations)

    # Devolver las películas recomendadas
    recommendations = cluster_movies["title"].tolist()
    return recommendations