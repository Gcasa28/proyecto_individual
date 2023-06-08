Proyecto individual
Gabriel Casanova

Contexto:
Tienes tu modelo de recomendación dando unas buenas métricas, y ahora, cómo lo llevas al mundo real?
El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

Objetivo:
Hacer un ETL, para luego realizar un EDA y por ultimo crear un modelo de recomendación utilizando machine learning.

Procedimiento:
Comenzando por descargar el data que proposiono la empresa y convertir el archivo ".csv" en un dataset de pandas para comenzar a visualizarlo, luego de esto vemos varias columnas del data set anidados como lo eran "belongs_to_collection", "genres", "production_companies", "production_countries", "spoken_languages".
Luego revisar si habian datos "nulos" o "vacios" en las columnas en la cual considerara importantes, ya que con datos faltantes en las columnas que tomaramos en cuenta, el modelo de ML podria fallar o no ser tan acertado, luego separamos la columna "release_date" en otras 3 columnas para que fuese mas sencillo trabajar con las funciones, despues de este paso de separar "release_date", calculo una columna llamara "return" con el promedio de retorno que utilizo en las funciones.
Importe un nuevo dataset llamado "credits" con pandas, donde tenia sus columnas anidadas tambien y el paso siguientes fue trabajar en ellas para dejarlas como una columna de listas para poder hacer las busquedas con las funciones de manera mas sencilla, ya una vez hecho este paso para desanidar estas columnas, procedi a unir ambos datasets para trabajar mas comodamente con uno, y luego hacer las funciones requeridas para los endpoints que son las siguientes:

- def cantidad_filmaciones_mes(mes): Determina la cantidad de películas que se estrenaron en el mes dado.

- def cantidad_filmaciones_dia(dia): Determina la cantidad de películas que se estrenaron en el día dado.

- def score_titulo(titulo_de_la_filmacion): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

- def votos_titulo(titulo_de_la_filmacion): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.

- def get_actor(nombre_actor): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.

- def get_director(nombre_director): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

- def recomendacion(titulo): Recomienda 5 peliculas con respecto a la proporcionada en la funcion.