"""
La PILA o STACK, en inglés, es uno de los tipos de datos más usados
en programación. Es importante conocer su funcionamiento e implementación.
En Python se utiliza el tipo de dato lista y sus funciones para utilizarlo como
una pila:
Básicamente, es un conjunto de datos al que se accede desde su última entrada
tanto para eliminar esta última entrada, con pop(), como para añadir un nuevo
dato a continuación con append().
Es así de simple.

pop() toma el valor del último elemento de la pila y lo elimina.
"""

# Defino una lista cualquiera como mi pila.
stack = [3,4,5]
print('Primera muestra de la pila:\n', stack)

# append(elemento) añade un elemento al final de la pila "stack".
stack.append(6)

print('La pila después de añadir un elemento con append:\n', stack)

# pop() quita el último elemento de la pila
# En una pila, el último elemento es también el último que se añadió.
stack.pop()

print ('La pila después de quitar el último elemento con pop:\n', stack)

# Puedo ver cuál es el último elemento de la pila con print(stack[-1])
print (f'El último elemento de la pila ahora es: {stack[-1]}')
