# ACTIVIDAD 1: EJERCICIOS DE PROGRAMACIÓN BÁSICA EN PYTHON
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES
# 1. Imprimir "¡Hola, mundo!" en la consola usando print().

print("hola mundo")

# 2. Pedir al usuario que ingrese su nombre usando input() e imprimir un saludo en consola usando print().

nombre=input("ingresa tu nombre:")
print("\n hola "+ nombre)

# 3. Sumar dos números ingresados por el usuario mediante input() y luego mostrar el resultado en consola usando print().
 
a=int(input("ingresar un numero entero:"))
b=int(input("\n ingrese otro numero entero:"))
print("\n ingresste:", a , "y", b)

# 4. Calcular el área de un triángulo a partir de la base y la altura ingresadas por el usuario mediante input() y luego mostrar el resultado en consola.

g=int(input(" ingresar la base del triangulo:"))
j=int(input("\n ingresar la altura del triangulo:"))
print("el area del triangulo es: ", (g*j)/2)

# 5. Calcular el promedio de tres números ingresados por el usuario mediante input() y luego mostrar el resultado en consola.

e=int(input("ingrese un numero entero:"))
r=int(input("ingresar otro numero entero:"))
t=int(input("ingrese un ultimo numero entero:"))
print("su promedio es", (e+r+t)/3)

# 6. Crear una lista con los siguientes números enteros: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] y mostrar por pantalla el resultado de sumar todos los números de la lista.

practica=[2, 4, 6, 8, 10 , 12, 14, 16, 18, 20]
print("la suma de su lista es:")
print(sum(practica))

# 7. Crear una función que reciba un número entero como parámetro y retorne el resultado de multiplicarlo por 2. Imprimir el resultado de invocarla pasándole como argumento un 5.

def practicab(a, b):
       return a*b
respuesta=practicab(5, 2)
print(respuesta)

# 8. Crear una función que reciba una cadena de texto como parámetro y retorne la cantidad de caracteres que tiene.

def practicac(h):
    h=input("ingrese un texto cualquiera(escriba lo que quiera):")
    contar=len(h)
    print(contar)
practicac("")
    
# 9. Crear una función que reciba una lista de números enteros como parámetro y retorne el número más grande de la lista.

def intento34(u=[39, 40, 19, 1, 86, 7]):
    lista2=u[0]
    for r in range(0, len(u)):
     if u[r] > lista2:
        lista2=u[r]
    return lista2
auxiliar=intento34()
print(auxiliar)
  
# 10. Crear una función que reciba una lista de cadenas de texto como parámetro y retorne la cantidad de cadenas que tienen más de 5 caracteres.

def argentinaprograma( w, m, f):
  caracteres=len(w)
  acciliar=0
  auciliar=0
  arciliar=0
  if caracteres> 5:
      auciliar=1
  cart=len(m)
  if cart > 5:
      acciliar=1
  cartf=len(f)
  if cartf > 5:
      arciliar=1
  suma=acciliar+auciliar+arciliar
  return suma
mostrar=argentinaprograma("la patagonia argentina, lindo lugar", "puerto esperansa", "hola mundo")
print(mostrar)