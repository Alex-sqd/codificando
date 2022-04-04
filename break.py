for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    """ break permite saltar al siguiente valor de x, evitando else, sin finalizar el bucle.
    Si no se utiliza break en este punto, se ejecuta else tras el bloque if, ejecutandose asi ambas ramas"""
    else:
        # Loop fell through without finding a factor
        # Si no se encuentra un multiplo
        print(n, 'is a prime number')
