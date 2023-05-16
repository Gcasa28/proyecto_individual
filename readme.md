Proyecto individual
Gabriel Casanova

Contexto:
Tienes tu modelo de recomendación dando unas buenas métricas, y ahora, cómo lo llevas al mundo real?
El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

Objetivo:
Hacer un ETL, para luego realizar un EDA y por ultimo crear un modelo de recomendación utilizando machine learning.

Procedimiento:
Comencé descargando el dataset en el cual hice hice una rapida visualizacion para ver en que estado estaban esos datos, vi que la madurez de los mismo era poca o nula, datos anidados, sin transformar, sin procesos automatizados para la actualizacion de nuevas peliculas, luego de un largo trabajo de ETL se dejaron los datos necesarios y limpios para empezar a la realizacion de la API, por supuesto realizando primero las funciones que necesitaba, luego haciendo el procedimiento para su deploy y consumo de la API.

funciones:

- def peliculas_mes(mes) = Determina la cantidad de películas que se estrenaron en el mes dado.

- def peliculas_dia(dia) = Determina la cantidad de películas que se estrenaron en el día dado.

- def franquicia(franquicia) = Determina la cantidad de películas que pertenece a la franquicia dada, la ganancia total y la ganancia promedio.

- def peliculas_pais(pais) = Determina la cantidad de películas producidas en el país dado.

- def productoras(productora) = Determina la ganancia total y la cantidad de películas de la productora dada.

- def retorno(pelicula) = Determina la inversion, la ganancia, el retorno de inversión y el año en el que se lanzo la pelicula dada.

- def recomendaciones(titulo_pelicula) = Recomienda 5 peliculas con respecto a la proporcionada en la funcion.

