inicio = int(input('Valor inicial: '))
fin = int(input('Valor final: '))
args = [inicio, fin]
lista = list(range(*args))
print (f'Lista inicial (valores inicial y final): {args}')
print (f'Lista desplegada desde los valores inicial al final: {lista}')
print ('Observa que el valor final no se alcanza')
print ('Para corregirlo podemos hacer una "trampa"...')
fin2 = fin + 1
args2 = [inicio, fin2]
lista2 = list(range(*args2))
print ('Sumo 1 al valor final y vuelvo a desplegar la lista y ahora sí alcanza el valor final: ', lista2)
