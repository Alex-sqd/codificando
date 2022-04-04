""" Para implementar una cola se usa la función deque de la librería collections.
En una cola se añade un elemento al principio de la cola
y se quita del final de la cola"""

# Primero hay que importar la función de la librería.
# "deque" es un tipo de dato que permite introducir y quitar
# elementos de cualquiera de sus extremos. Es una versión ampliada de una lista.
from collections import deque

# Creamos una lista de elementos de tipo "deque"
womenNames = deque(['Ana', 'Rocío', 'Lucía'])
print('El contenido de nuestra lista es: ', womenNames)

# Añadimos un elemento a la lista con append.
# append añade el elemto a la derecha, al final de la lista.
womenNames.append('María')
print('Después de añadir un elemento nuevo, la lista queda así:\n', womenNames)

# Y quitamos otro elemento al inicio de la lista con popleft().
# No se especifican argumentos a popleft(). Paréntesis siempre vacíos.
womenNames.popleft()
print('Después de quitar un elemento del principio de la lista queda así:\n', womenNames)



