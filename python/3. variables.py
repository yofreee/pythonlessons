#Variables
#Las variables son contenedores para almacenar valores de datos

#Creación de variables
#Python no tiene ningún comando para declarar una variable, una variable se crea en el momento en que se le asigna un valor por primera vez:
x = 5
y = "Jhon"
print(x)
print(y)

#Las variables no necesitan ser declaradas con ningún tipo en particular, e incluso pueden cambiar de tipo de despúes de que se hayan establecido
x = 4 # x es de tipo int
y = "Jhon" # y es de tipo str
print(x)

#Fundición
#Si desea especificar el tipo de datos de una variable, esto se puede hacer con la conversión:
x = str(3) # x será "3"
y = int(3) # y será 3
z = float(3) #z será 3.0

#Obtener el tipo
#Para obtener el tipo de datos de una variable con la función type())
x = 5
y = "jhon"
print(type(x))
print(type(y))

# ¿Comillas simples o dobles?
#Las variables de cadena se pueden declarar mediante comillas simples o dobles:
x = "jhon"
# es lo mismo que
x = 'jhon'

# Distinguen entre mayúsculas y minúsculas
# Los nombres de las variables distinguen  entre mayúsculas y minúsculas
a = 4
A = "Sally"
# Esto creará dos variables distintas, por lo tanto A no sobreescribirá a la variable a

#Nombres de variables
# Una variable puede tener un nombre corto o un nombre más descriptivo (edad, nombre, total_volume)
    
    # Reglas para las variables de Python:
    # 1) Un nombre de variable debe comenzar con una letra
    # 2) Un nombre de variable no puede comenzar con un número
    # 3) Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos
    # 4) Los nombres de variables distinguen entre mayúsculas y minúsculas (edad, Edad y EDAD son tres variables diferentes)

    # Ejemplo de variables validas:
    myvar = "jhon"
    my_var = "jhon"
    _my_var = "jhon"
    myVar = "jhon"
    MYVAR = "jhon"
    myvar2 = "jhon"

    # Nombres de variables de varias palabras:
    # Los nombres de variables con más de una palabra pueden ser difíciles de leer, hay varias técnicas que se pueden utilizar para hacerlos más legibles:

    # 1) Camel Case
    # Cada palabra, excepto la primera, comienza con una letra mayúscula:
    myVariable = "jhon"

    # 2) Pascal Case
    # Cada palabra comienza con una letra mayúscula:
    MyVariableName = "jhon"

    # 3) Snake Case
    # Cada palabra está separada por un carácter de subrayado:
    my_variable_name = "jhon"


# Asignar varios valores
# Python permite asignar valores a múltiples variables en una línea:
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

# Asignar el mismo valor a varias variables en un línea:
x = y = z = "orange"
print(x)
print(y)
print(z)

# Desempaquetar una colección
# Si tiene una colección de valores en una lista. Python le permite extraer los valores en variables. Esto se llama desempaquetado
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Variables de salida
# La función print() Python la utiliza a menudo para generar variables
x = "Python es increible"
print(x)
# Para generar varias variables se puede utilizar el operador +
x = "Python "
y = "es "
z = "increible"
print(x + y + z)
#Observe el carácter de espacio despúes de "Python " y "es " , sin ellos el resultado sería "Pythonesincreible"

# Para los números el carácter + funciona como un operador matemático:
x = 5
y = 10
print(x + y)
# Aunque al intentar combinar una cadena y un número con el operador + Python le dará un error, la mejor manera de generar múltiples variables en la función print() es separarlas con comas, que incluso admiten diferentes tipos de datos:
x = 5
y = "jhon"
print(x, y)

#Variables globales
# Las variables que se crean fuera de una función se conocen como variables globales, las variables globales pueden ser utilizadas por todos, tanto dentro de las funciones como fuera

# Ej. Crear una variable fuerda de una función y utilizarla dentro de la función:
x = "increible"

def miFuncion():
    print("Python es " + x)

miFuncion()

# Si crea una variable con el mismo nombre dentro de una función, esta variable será local y solo se puede usar dentro de la función. La variable global con el mismo nombre permanecerá como estaba, global y con el valor original:

# Ej. Crear una variable dentro de una función, con el mismo nombre que la variable global
x = "increible"

def miFuncion():
    x = "fantastico"
    print("Python es " + x)     # Python es fantastico

miFuncion()
print("Python es " + x)      # Python es increible


# La palabra clave global
# Normalmente cuando se crea una variable dentro de una función, esa variable es local y solo se puede usar dentro de esa función, para crear una variable global dentro de una función, se puede utilizar la palabra clave global:

# Ej. si usa la palabra clave "global", la variable pertenece al ámbito global:
def miFuncion():
    global x
    x = "fantastico"

miFuncion()

print("Python es " + x)

# Cambiar una variable global dentro de una función
# Ej. Para cambiar el valor de una variable global dentro de una función , consulte la variable usando la palabra clave global:
x = "increible"

def miFuncion():
    global x
    x = "fantastico"

miFuncion()

print("Python es "+ x)      #Python es fantastico


















