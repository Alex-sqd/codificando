produccion = int(input('Producción: '))  # Producción de vehículos de la jornada
primero = int(input('Primero: '))  # Número del primer vehículo de la jornada
vuelta = int(input('Vuelta: '))  # Número en que da la vuelta o cero si no da vuelta

def u(a):
    return lambda b, c: ((a - (c - b))-1)

u_m1 = u(produccion)   # 
print (u_m1(primero, vuelta))
