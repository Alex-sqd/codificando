""" 
En una cola se añade un elemento al final de la cola
y se quita del principio de la cola

Primero hay que importar el tipo deque de la librería collections.
"deque" es un tipo de dato que permite introducir y quitar
elementos de cualquiera de sus extremos. Es una versión ampliada de una lista.
"""

from collections import deque

# Creamos una lista de elementos de tipo "deque"
women_names = deque(['Ana', 'Rocío', 'Lucía'])
print('El contenido de nuestra lista es: ', women_names)

# Añadimos un elemento a la lista con append.
# append añade el elemto a la derecha, al final de la lista.
women_names.append('María')
print('Después de añadir un elemento nuevo, la lista queda así:\n', women_names)

# Y quitamos otro elemento al inicio de la lista con popleft().
# No se especifican argumentos a popleft(). Paréntesis siempre vacíos.
women_names.popleft()
print('Después de quitar un elemento del principio de la lista queda así:\n', women_names)



