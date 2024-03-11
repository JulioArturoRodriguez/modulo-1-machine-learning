# ACTIVIDAD 2: LIBRERÍAS NUMPY Y MATPLOTLIB
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES CON NUMPY ##
# Visite la documentación de Numpy para obtener más información sobre los métodos utilizados en esta actividad: 
# https://numpy.org/doc/stable/reference/index.html

# 1. Crear un array y obtener información sobre su forma y tamaño:
# Enunciado: Crea un array de 2 dimensiones utilizando el método np.array() con los siguientes
#   elementos: [1, 2, 3] y [4, 5, 6]. Luego, utiliza los métodos shape y size para obtener la 
#   forma y el tamaño del array, respectivamente. Imprime la forma y el tamaño por consola.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print (arr.shape)
print (arr.size)

# 2. Realizar operaciones matemáticas con un array:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5]. 
#   a) Utiliza la función np.square() para calcular el cuadrado de cada elemento del array. Imprime el resultado por consola.
#   b) Utiliza la función np.sqrt() para calcular la raíz cuadrada de cada elemento del array. Imprime el resultado por consola.
#   c) Utiliza la función np.sin() para calcular el seno de cada elemento del array. Imprime el resultado por consola.
#   d) Utiliza la función np.cos() para calcular el coseno de cada elemento del array. Imprime el resultado por consola.
#   e) Utiliza la función np.tan() para calcular la tangente de cada elemento del array. Imprime el resultado por consola.

import numpy as np
a = np.array([1, 2, 3, 4, 5])
a1 = np.square(a)
a2 = np.sqrt(a)
a3 = np.sin(a)
a4= np.cos(a)
a5 = np.tan(a)
print (a1)
print (a2)
print (a3)
print (a4)
print (a5)

# 3. Realizar operaciones matemáticas con dos arrays:
# Enunciado: Crea dos arrays utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5] y [6, 7, 8, 9, 10].
#   a) Utiliza la función np.add() para sumar los elementos de ambos arrays. Imprime el resultado por consola.
#   b) Utiliza la función np.subtract() para restar los elementos de ambos arrays. Imprime el resultado por consola.
#   c) Utiliza la función np.multiply() para multiplicar los elementos de ambos arrays. Imprime el resultado por consola.
#   d) Utiliza la función np.divide() para dividir los elementos de ambos arrays. Imprime el resultado por consola.
#   e) Utiliza la función np.power() para elevar los elementos del primer array a los elementos del segundo array. Imprime el resultado por consola.

import numpy as np
b = np.array([1, 2, 3, 4, 5])
c = np.array([6, 7, 8, 9, 10])
i2 = np.add(b, c)
i3 = np.subtract(b, c)
i4 = np.multiply(b, c)
i5 = np.divide(b, c)
i6 = np.power(b, c)
print (i2)
print (i3)
print (i4)
print (i5)
print (i6)

# 4. Manipular los elementos de un array:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Utiliza el método np.reshape() para cambiar la forma del array a (5, 1). Imprime el resultado por consola.
#   b) Utiliza el método np.ravel() para cambiar la forma del array a (1, 5). Imprime el resultado por consola.
#   c) Utiliza el método np.transpose() para cambiar la forma del array a (5, 1). Imprime el resultado por consola.
#   d) Utiliza el método np.resize() para cambiar la forma del array a (3, 3). Imprime el resultado por consola.
#   e) Utiliza el método np.append() para agregar el elemento 6 al array. Imprime el resultado por consola.

import numpy as jj
q = jj.array([1, 2, 3, 4, 5])
a = jj.reshape(q, (5, 1))
a2 = jj.ravel(a)
a3 = jj.transpose(a)
a4 = jj.resize(q, (3, 3))
a5 = jj.append(q, 6)
print (a)
print (a2)
print (a3)
print (a4)
print (a5)



## ACTIVIDADES CON MATPLOTLIB ##
# Visite la documentación de Matplotlib para obtener más información sobre los métodos utilizados en esta actividad:
# https://matplotlib.org/stable/api/index.html

# 1. Crear un gráfico de líneas:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Crea un gráfico de líneas utilizando el método plt.plot().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de líneas".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

import matplotlib.pyplot as plt
import numpy as kk
x = kk.array([1, 2, 3, 4, 5])
plt.plot(x)
plt.title("grafico de lineas")
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()


# 2. Crear un gráfico de barras:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Crea un gráfico de barras utilizando el método plt.bar().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de barras".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

import matplotlib.pyplot as plt
import numpy as kk
x = kk.array([1, 2, 3, 4, 5])
plt.bar(x, x)
plt.title("grafico de barras")
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()

# 3. Crear un gráfico de dispersión con un array de dos dimensiones:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [[1, 2], [3, 4], [5, 6]].
#   a) Crea un gráfico de dispersión utilizando el método plt.scatter().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de dispersión 2D".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico

import matplotlib.pyplot as plt
import numpy as kk
x = kk.array([[1, 2, 3], [4, 5, 6]])
plt.scatter(x, x)
plt.title("grafico de dispersion 2d")
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()

# 4. Crear un gráfico de dispersión con un array de tres dimensiones:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [[1, 2, 3], [4, 5, 6]].
#   a) Crea un gráfico de dispersión utilizando el método plt.scatter().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de dispersión 3D".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

import matplotlib.pyplot as plt
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
plt.scatter(x, x)
plt.title("grafico de dispersion 3d")
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()

# 5. Crear un gráfico de barras con dos arrays:
# Enunciado: Crea dos arrays utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5] y [6, 7, 8, 9, 10].
#   a) Crea un gráfico de barras utilizando el método plt.bar().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de barras".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   f) Utiliza el método plt.legend() para agregar la leyenda "Leyenda".
#   g) Utiliza el método plt.xticks() para agregar las etiquetas del eje x "Eje x".
#   h) Utiliza el método plt.yticks() para agregar las etiquetas del eje y "Eje y".
#   i) Utiliza el método plt.grid() para agregar la grilla al gráfico.
#   j) Utiliza el método plt.show() para mostrar el gráfico.


import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
x = np.array([1, 2, 3, 4, 5])
c = np.array([6, 7, 8, 9, 10])
r = ("")
plt.bar(x, c)
plt.title("grafico de dispersion 3d")
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.plot(r, label = "leyenda")
plt.legend()
plt.xticks([5], ['eje x'])
plt.yticks([10], ['eje y'])
plt.show()