def make_incrementor(n):
    return lambda x: x + n

b = int(input('Base: '))
f = make_incrementor(b)
inicio_rango = int(input('Inicio: '))
fin_rango = int(input('Fin: '))
for i in range(inicio_rango, fin_rango):
    print(f(i))
