#!/usr/bin/env python
# coding: utf-8

# ## Notas numpy

# In[1]:


#La forma estándar de importar NumPy
import numpy as np


# In[2]:


lista1 = [12,43,52,78] 

#Convertir una lista en un arreglo unidimensional
arreglo1d = np.array(lista1)

arreglo1d


# In[3]:


lista2 = [24,43,54,65]

lista2d = [lista1,lista2]

#Arreglo multidimensional 2d
arreglo2d = np.array(lista2d)

arreglo2d


# In[4]:


#Información básica


# In[5]:


#Dimensiones del arreglo.
arreglo2d.shape


# In[6]:


#Tipo del arreglo
arreglo2d.dtype


# In[7]:


#Cantidad de elementos del arreglo
arreglo2d.size


# In[8]:


np.arange(10)


# ###Creación de un arreglo

# In[9]:


#Desde una lista y dando el tipo 
lista_complejos = [[1,2,3],[4,5,6]]

arreglo_complejo = np.array(lista_complejos, dtype=complex)

arreglo_complejo


# In[10]:


#Desde un rango de números conocidos

arreglo_rango_pares = np.arange(0,30,2)


# In[11]:


#Arrelo de ceros

arreglo_ceros = np.zeros(9)
arreglo_ceros


# In[12]:


#Arreglo de unos

arreglo_unos = np.ones(9)
arreglo_unos


# In[13]:


#Arreglo ojo

arreglo_ojo = np.eye(3)
arreglo_ojo


# In[15]:


#Arreglo con números aleatorios
array_random_uniforme = np.random.rand(5) #uniforma con valores [0,1]
array_random_uniforme


# In[16]:


array_random_randn = np.random.randn(5) #Gaussian
array_random_randn 


# In[25]:


np.random.seed(1234) #Con semilla
array_random_randn = np.random.randn(5) #Gaussian
array_random_randn


# In[29]:


# np.empty Desplegar la ayuda

#Crear un arreglo vacio

np.empty([3,3])


# ## Visualización Básica

# In[58]:


#Habilitar la plots en la hoja
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

import matplotlib as mpl


# In[39]:


#Array 1D
#Line plot

#Definir arreglo  abscisa(x) y ordenada(y) 

x = np.arange(0,30,2)
y = np.arange(1,31,2)

plt.plot(x,y, '*')

plt.show()


# In[43]:


image = np.random.rand(20,30)
plt.imshow(image, cmap=plt.cm.hot)   


# In[59]:


mpl.cm.get_cmap


# In[66]:


image2 = np.random.rand(20,30)
image2 = np.cos(image)

colors = 4
plt.imshow(image2, cmap=plt.cm.Greens)   

image2.size


# ##  Indexing and slicing
# ##  manipular elementos dentro de un arreglo

# In[68]:


arr1 = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
arr1


# In[72]:


arr1[:,2] # colomna 3


# In[74]:


arr1[0,3:5] # columna 0, elementos 3,4


# In[75]:


arr1[3,:] #fila 4


# In[76]:


arr1[4:,4:] # Ultimas 5 interseccion filas y columas

