from fastapi import FastAPI
import pandas as pd
import numpy as np

df = pd.read_csv("data_con_EDA.csv")

app = FastAPI()

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes):
    '''Determina la cantidad de películas que se estrenaron en el mes dado'''
   
    respuesta = df['id'][df['release_month'] == mes].count()
    return {'mes': mes, 'cantidad': str(respuesta)}

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia):
    '''Determina la cantidad de películas que se estrenaron en el día dado'''
   
    respuesta = df['id'][df['release_day'] == dia].count()
    return {'dia': dia, 'cantidad': str(respuesta)}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia):
    '''Determina la cantidad de películas que pertenece a la franquicia dada, la ganancia total y la ganancia promedio'''
   
    respuesta1 = df['id'][df['belongs_to_collection'] == franquicia].count()
    respuesta2 = np.sum(df['return'][df['belongs_to_collection'] == franquicia])
    respuesta3 = np.mean(df['return'][df['belongs_to_collection'] == franquicia])
    return {'franquicia': franquicia, 'cantidad': respuesta1, 'ganancia_total': respuesta2, 'ganancia_promedio': respuesta3}

@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais):
    '''Determina la cantidad de películas producidas en el país dado'''

    respuesta = 0
    n = df['production_countries'].size
    for i in range(n):
        if pais in df.iloc[i, 8]:
            respuesta += 1
    return {'pais': pais, 'cantidad': respuesta}

@app.get("/productoras/{productora}")
def productoras(productora):
    '''Determina la ganancia total y la cantidad de películas de la productora dada'''

    respuesta1 = 0
    respuesta2 = 0
    n = df['production_companies'].size
    for i in range(n):
        if productora in df.iloc[i, 7]:
            respuesta1 += df.iloc[i, 20]
            respuesta2 += 1
    return {'productora': productora, 'ganancia_total': respuesta1, 'cantidad': respuesta2}


@app.get("/pelicula/{pelicula}")
def retorno(pelicula):
    '''Determina la inversion, la ganancia, el retorno de inversión y el año en el que se lanzo la pelicula dada'''

    respuesta1 = 0
    respuesta2 = 0
    respuesta3 = 0
    respuesta4 = 0
    n = df['title'].size
    for i in range(n):
        if df.iloc[i, 15] == pelicula:
            respuesta1 += df.iloc[i, 1]
            respuesta2 += df.iloc[i, 10]
            respuesta3 += df.iloc[i, 20]
            respuesta4 = df.iloc[i, 17]
    return {'pelicula':pelicula, 'inversion':respuesta1, 'ganacia':respuesta2,'retorno':respuesta3, 'anio':int(respuesta4)}