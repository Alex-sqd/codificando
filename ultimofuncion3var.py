""" Utilizar variables con valores predefinidos me permite
utilizar varias variables en la misma función. 
Sin valores predefinidos sólo permite dos variables
y para esta función me interesa utilizar tres ;)"""

def ultimo(primero, produccion=419, vuelta=0):
    u = ((produccion-(vuelta-primero))-1)
    return u

continuar = 's'
while continuar == 's':
    produccion = int(input('La producción de hoy es: '))
    primero = int(input('El primer vehículo es el número: '))
    vueltaOk = False # Inicializo la variable para usarla en el bucle while
    """ Este bucle while me aseguro de que el número en que da la vuelta
    sea mayor que el número del primero"""
    while vueltaOk == False:
        vuelta = int(input('¿Hay vuelta? Indica en qué número: (Si no hay vuelta escribe 0)'))
        if vuelta > primero or vuelta == 0:
            vueltaOk = True
    print (ultimo(primero,produccion,vuelta))
    continuar = input('Continuar ("s" o cualquier tecla para finalizar)')

