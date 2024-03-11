# ACTIVIDAD 3: LIBRERÍA PANDAS
# ADVERTENCIA: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# ADVERTENCIA: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# ADVERTENCIA: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# ADVERTENCIA: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

import pandas as pd

## ACTIVIDADES ##
# Visite la documentación de Pandas para obtener más información sobre los métodos utilizados en esta actividad: 
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html

# 1. Leer el archivo CSV
# Utilizar el método read_csv() para leer el archivo "datos.csv" y almacenarlo en una variable llamada df.

import pandas as pd
df = pd.read_csv("datos.csv")

# 2. Mostrar los primeros 5 registros
# Utilizar el método head() para imprimir por consola los primeros 5 registros del DataFrame.

import pandas as pd
df = pd.read_csv("datos.csv")
print(df.head(5))


# 3. Mostrar los últimos 5 registros
# Utilizar el método tail() para imprimir por consola los últimos 5 registros del DataFrame.

import pandas as do
do = do.read_csv("datos.csv")
print(do.tail(5))

# 4. Mostrar la cantidad de filas y columnas
# Utilizar el atributo shape para imprimir por consola la cantidad de filas y columnas del DataFrame.

import pandas as de
de = de.read_csv("datos.csv")
print(de.shape)

# 5. Mostrar la descripción estadística
# Utilizar el método describe() para imprimir por consola la descripción estadística del DataFrame.

import pandas as du
du= du.read_csv("datos.csv")
print(du.describe())

# 6. Filtrar los registros donde la columna "Producto" sea igual a "Naranja"
# Utilizar el método loc() para obtener los registros donde la columna "Producto" sea igual a "Naranja" y almacenarlos en una variable llamada naranjas.
# Imprimir por consola los registros obtenidos.

import pandas as ju
ju= ju.read_csv("datos.csv")
naranjas =ju.loc[(ju.Producto == "Naranja")]
print (naranjas)

# 7. Filtrar los registros donde la columna "Precio" sea mayor a 10
# Utilizar el método loc() para obtener los registros donde la columna "Precio" sea mayor a 10 y almacenarlos en una variable llamada precios_altos.
# Imprimir por consola los registros obtenidos.


import pandas as ja
ja= ja.read_csv("datos.csv")
precios_altos = ja.loc[(ju.Precio > 10)]
print (precios_altos)


# 8. Filtrar los registros donde la columna "Cantidad" sea mayor a 10 y la columna "Precio" sea igual mayor a 10
# Utilizar el método loc() para obtener los registros donde la columna "Cantidad" sea mayor a 10 y la columna "Precio" sea igual mayor a 10 y almacenarlos en una variable llamada filtro_cantidad_precio.
# Imprimir por consola los registros obtenidos.

import pandas as ja
ja= ja.read_csv("datos.csv")
precios_altos = ja.loc[(ja.Cantidad > 10) & (ja.Precio >=10)]
print (precios_altos)

# 9. Eliminar la columna "Precio"
# Utilizar el método drop() para eliminar la columna  del DataFrame.
# Imprimir por consola el DataFrame resultante.

import pandas as MEME
MEME= MEME.read_csv("datos.csv")
precio = MEME.drop(columns= ['Precio'])
print (precio)


# 10. Eliminar los registros donde se repita el valor de la columna "Producto"
# Utilizar el método drop_duplicates() para eliminar los registros donde se repita el valor de la columna "Producto" del DataFrame.
# Imprimir por consola el DataFrame resultante.

import pandas as MEMA
MEMA= MEMA.read_csv("datos.csv")
MEMA = MEMA.drop_duplicates("Producto")
print (MEMA)

# Visite la documentación de Pandas para obtener más información sobre el método drop_duplicates():
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
