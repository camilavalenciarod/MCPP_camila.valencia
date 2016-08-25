
# coding: utf-8

# # Taller 3
# Métodos Computacionales para Políticas Públicas - URosario
# 
# **Entrega: viernes 26-ago-2016 11:59 PM**

# <div class="alert alert-success">
# **[Camila Valencia]** <br><br>
# [camilavalenciar@gmail.com]
# </div>

# ## Instrucciones:
# - Guarde una copia de este *Jupyter Notebook* en su computador, idealmente en una carpeta destinada al material del curso.
# - Modifique el nombre del archivo del *notebook*, agregando al final un guión inferior y su nombre y apellido, separados estos últimos por otro guión inferior. Por ejemplo, mi *notebook* se llamaría: mcpp_taller3_santiago_matallana
# - Marque el *notebook* con su nombre y e-mail en el bloque verde arriba. Reemplace el texto "[Su nombre acá]" con su nombre y apellido. Similar para su e-mail.
# - Desarrolle la totalidad del taller sobre este *notebook*, insertando las celdas que sea necesario debajo de cada pregunta. Haga buen uso de las celdas para código y de las celdas tipo *markdown* según el caso.
# - Recuerde salvar periódicamente sus avances.
# - Cuando termine el taller:
#     1. Descárguelo en PDF.
#     2. Suba los dos archivos (.pdf y .ipynb) a su repositorio en GitHub antes de la fecha y hora límites.
# 
# (El valor de cada ejercicio está en corchetes [ ] después del número de ejercicio.)

# ---

# Antes de iniciar, por favor descarge el archivo <font face="consolas" color="green">mcpp_taller3_listas_ejemplos.py</font> del repositorio, guárdelo en la misma carpeta en la que está trabajando este taller y ejecútelo con el siguiente comando:

# In[5]:

run mcpp_taller3_listas_ejemplos.py


# Este archivo contiene tres listas (<font face="consolas" color="green">l0</font>, <font face="consolas" color="green">l1</font> y <font face="consolas" color="green">l2</font>) que usará para las tareas de esta sección. Puede ver los valores de las listas simplemente escribiendo sus nombres y ejecutándolos en el Notebook. Inténtelo para verificar que <font face="consolas" color="green">mcpp_taller3_listas_ejemplos.py</font> quedó bien cargado. Debería ver:

# In [1]: l0
# Out[1]: []
# 
# In [2]: l1
# Out[2]: [1, 'abc', 5.7, [1, 3, 5]]
# 
# In [3]: l2
# Out[3]: [10, 11, 12, 13, 14, 15, 16]

# In[6]:

l0


# In[7]:

l1


# In[8]:

l2


# ## 1. [1]
# 
# Cree una lista que contenga los elementos <font face="consolas">7</font>, <font face="consolas">"xyz"</font> y <font face="consolas">2.7</font>.

# In[9]:

l4=[7,"xyz",2.7]


# In[10]:

l4


# ## 2. [1]
# 
# Halle la longitud de la lista <font face="consolas">l1</font>.

# In[11]:

len(l1)


# ## 3. [1]
# 
# Escriba expresiones para obtener el valor <font face="consolas">5.7</font> de la lista <font face="consolas">l1</font> y para obtener el valor <font face="consolas">5</font> a partir del tercer elemento de <font face="consolas">l1</font>.

# In[12]:

l1[2]


# In[13]:

l1[3][2]


# ## 4. [1]
# 
# Prediga qué ocurrirá si se evalúa la expresión <font face="consolas">l1[4]</font> y luego pruébelo.

# Prediciendo esto me va a generar un error ya que python empieza a contar en 0. Luego el primer elemento esta en la posicion 0, si le pido que me muestre el 4 posicion elemento me mostrara el 5to elemento. Como la lista solo tiene 4, me dira que hay un error porque no hay elemtos que mostrar

# In[1]:

l1[4]


# ## 5. [1]
# 
# Prediga qué ocurrirá si se evalúa la expresión <font face="consolas">l2[-1]</font> y luego pruébelo.

# Mostrara el ultimo elemento de l2, es decir 16

# In[15]:

l2[-1]


# ## 6. [1]
# 
# Escriba una expresión para cambiar el valor <font face="consolas">3</font> en el tercer elemento de <font face="consolas">l1</font> a <font face="consolas">15.0</font>.

# In[17]:

l1[3][1]=15.0
l1


# ## 7. [1]
# 
# Escriba una expresión para crear un "slice" que contenga del segundo al quinto elemento (inclusive) de la lista <font face="consolas">l2</font>.

# In[20]:

l2[1:5]


# ## 8. [1]
# 
# Escriba una expresión para crear un "slice" que contenga los primeros tres elementos de la lista <font face="consolas">l2</font>.

# In[21]:

l2[:3]


# ## 9. [1]
# 
# Escriba una expresión para crear un "slice" que contenga del segundo al último elemento de la lista <font face="consolas">l2</font>.

# In[23]:

l2[1:]


# ## 10. [1]
# 
# Escriba un código para añadir cuatro elementos a la lista <font face="consolas">l0</font> usando la operación <font face="consolas">append</font> y luego extraiga el tercer elemento (quítelo de la lista). ¿Cuántos "appends" debe hacer?

# In[ ]:

Ya que la lista es vacia tengo que hacer 4 appends


# In[26]:

import random
for i in range(4):
    l0.append(random.randint(0,55))
    print (l0)


# In[31]:

del l0[2]
l0


# ## 11. [1]
# 
# Cree una nueva lista <font face="consolas">nl</font> concatenando la nueva versión de <font face="consolas">l0</font> con <font face="consolas">l1</font>, y luego actualice un elemento cualquiera de <font face="consolas">nl</font>. ¿Cambia alguna de las listas <font face="consolas">l0</font> o <font face="consolas">l1</font> al ejecutar los anteriores comandos?

# In[34]:

n1=l0+l1
n1


# In[37]:

n1[2]=5555
n1


# In[38]:

l0


# In[39]:

l1


# Al hacer este cambio no se alteran ninguna de las dos listas l0 o l1 ya que se actualizo el elemento el la lista n1

# ## 12. [2]
# 
# Escriba un loop que compute una variable <font face="consolas">all_pos</font> cuyo valor sea <font face="consolas">True</font> si todos los elementos de la lista <font face="consolas">l3</font> son positivos y <font face="consolas">False</font> en otro caso.

# In[46]:

l3=[5,-8,33,-77,-9,55,3]


# In[47]:

all_pos = True 
for i in l3:
    if i<0:
        all_pos=False
        break
print(all_pos)
    


# ## 13. [2]
# 
# Escriba un código para crear una nueva lista que contenga solo los valores positivos de la lista <font face="consolas">l3</font>.

# In[50]:

pos=[]
for i in l3:
    if i>0:
        pos.append(i)
        
        
print (pos)


# ## 14. [2]
# 
# Escriba un código que use <font face="consolas">append</font> para crear una nueva lista <font face="consolas">nl</font> en la que el i-ésimo elemento de <font face="consolas">nl</font> tiene el valor <font face="consolas">True</font> si el i-ésimo elemento de <font face="consolas">l3</font> tiene un valor positivo y <font face="consolas">Falso</font> en otro caso.

# In[54]:

n1=[]

for i in l3:
    if i>0:
        n1.append(True)
    if i<0:
        n1.append(False)
print(n1)


# ## 15. [3]
# 
# Escriba un código que use <font face="consolas">range</font>, para crear una nueva lista <font face="consolas">nl</font> en la que el i-ésimo elemento de <font face="consolas">nl</font> es <font face="consolas">True</font> si el i-ésimo elemento de <font face="consolas">l3</font> es positivo y <font face="consolas">Falso</font> en otro caso.
# 
# **Pista:** Comience por crear una lista de longitud adecuada, con <font face="consolas">False</font> en cada índice.

# In[62]:

n1=[False]*len(l3)
n1
for i in range(len(l3)):
    if l3[i]>0:
        n1[i]=True
        
n1


# ## 16. [4]
# 
# En clase construimos una lista con 10000 números aleatorios entre 0 y 9, a partir del siguiente código:
import random

N = 10000  
random_numbers = []
for i in range(N):
    random_numbers.append(random.randint(0,9))
# Y creamos un "contador" que calcula la frecuencia de ocurrencia de cada número del 0 al 9, así:
count = []
for x in range(0,10):
    count.append(random_numbers.count(x))
# Cree un "contador" que haga lo mismo, pero sin hacer uso del método "count". (De hecho, sin usar método alguno.)

# **Pistas:**
# 
# - Esto puede lograrse con un loop muy sencillo. Si su código es complejo, piense el problema de nuevo.
# - Es muy útil iniciar con una lista "vacía" de 10 elementos. Es decir, una lista con 10 ceros.

# In[9]:

import random

N = 10000  
random_numbers = []
for i in range(N):
    random_numbers.append(random.randint(0,9))
    
contar=[0]*10
numeros=[0,1,2,3,4,5,6,7,8,9]
for n in random_numbers:
    for i in numeros:
        if i==n:
            contar[n]=contar[n]+1

print(contar)


# In[15]:

count = []
for x in range(0,10):
    count.append(random_numbers.count(x))
print(count)

