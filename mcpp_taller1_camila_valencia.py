
# coding: utf-8

# # Taller 1 
# Métodos Computacionales para Políticas Públicas - URosario
# 
# **Entrega: viernes 12-ago-2016 11:59 PM**

# <div class="alert alert-success">
# **[Camila Valencia]** <br><br>
# [camila.valencia@urosario.edu.co]
# </div>

# ## Instrucciones:
# - Guarde una copia de este *Jupyter Notebook* en su computador, idealmente en una carpeta destinada al material del curso.
# - Modifique el nombre del archivo del *notebook*, agregando al final un guión inferior y su nombre y apellido, separados estos últimos por otro guión inferior. Por ejemplo, mi *notebook* se llamaría: mcpp_taller1_santiago_matallana
# - Marque el *notebook* con su nombre y e-mail en el bloque verde arriba. Reemplace el texto "[Su nombre acá]" con su nombre y apellido. Similar para su e-mail.
# - Desarrolle la totalidad del taller sobre este *notebook*, insertando las celdas que sea necesario debajo de cada pregunta. Haga buen uso de las celdas para código y de las celdas tipo *markdown* según el caso.
# - Recuerde salvar periódicamente sus avances.
# - Cuando termine el taller:
#     1. Descárguelo en PDF. Esto puede implicar instalar LaTex en su computador. Resuélvalo por su cuenta, por favor. Recuerde: Google es su amigo.
#     2. Suba los dos archivos (.pdf y .ipynb) a su repositorio en GitHub antes de la fecha y hora límites.
# 
# (Todos los ejercicios tienen el mismo valor.)

# ---

# ## 1. Zelle, sección 1.10 (p. 17):
# - "Multiple Choice", Ejercicios # 1-10.
# - "Programming Exercises", Ejercicio # 1.

# Multiple Choice: 
# 1.b
# 2.d
# 3.d
# 4.a
# 5.b
# 6.b
# 7.b
# 8.b
# 9.a
# 10.d
# 

# In[6]:

#Programming Exercises 1
print("Hello, world!")
print("Hello", "world!")
print(3)
print(3.0)
print(2+3)
print(2.0+3.0)
print("2"+"3")
print("2+3=",2+3)
print(2*3)
print(2**3)
print(2/3)


# En *computer science* son comunes los ejercicios denominados "pensar como un computador". Con estos usted evalúa si está comprendiendo el material, siempre y cuando no utilice un computador para correr el código del enunciado. Siempre que vea un ejercicio marcado con la etiqueta "pensar como un computador", use papel y lápiz o incluso una calculadora si es necesario para descifrar la respuesta, pero nunca ejecute el código en computador.

# ## 2. [Pensar como un computador] ¿Cuál es el valor de *w* después de ejecutar el siguiente código?
x = 7
y = 5.0
z = 10.0
w = x % 2 + y / z + z + y / (z + z)
# w=11.75 el computador hace primero las multiplicaciones sobre las sumas a menos de que se encuentren en un paquete

# ## 3. [Pensar como un computador] ¿Cuál es el valor de *c* después de ejecutar el siguiente código?
c = True
d = False
c = c and d
c = not c or d
# c = True
# Por que en la tercera linea la funcion and entre un verdadero y falso de falso, luego el not de c es verdadero y el or entre verdadero y falso es verdadero

# ## 4. Ejecute el siguiente código y responda: ¿Por qué es falsa la tercera línea, mientras que las primeras dos son verdaderas?

# In[3]:

1 == 1
"1" == "1"
1 == "1"


# Es falsa porque la tercera linea es una igualdad entre dos formatos diferentes, uno es string y otro es numero. Las dos primeras lineas son verdaderas por que los 1 estan en el mismo formato.

# ## 5. Escriba un programa que le pida al usuario ingresar su nombre y que arroje un texto saludando de vuelta al usuario, así: "Hola, &lt;nombre>. ¡Veo que aprendes Python rápidamente! ¡Felicitaciones!".

# In[1]:

print("Ingrese su nombre")
name= input()
print('Hola '+name+' ¡Veo que aprendes Python rápidamente!¡Felicitaciones!')


# In[ ]:



