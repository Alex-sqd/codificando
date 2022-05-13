produccion = int(input('Producción: '))  # Producción de vehículos de la jornada
primero = int(input('Primero: '))  # Número del primer vehículo de la jornada
vuelta = int(input('Vuelta: '))  # Número en que da la vuelta o cero si no da vuelta

def ultimo(a):
    return lambda b, c: ((a - (c - b))-1)

u = ultimo(produccion)
print (u(primero, vuelta))

"""
Funciona, pero no lo entiendo :(
Cuando lo escribí conseguí que funcionara y ahora no entiendo cómo es que funciona.

¿De donde obtiene b y c si a la función sólo le paso el valor a?

A ultimo se le asigna el valor de salida de ultimo(produccion)...
pero el valor de primero y vuelta se le pasa al comando print, no a la función.
