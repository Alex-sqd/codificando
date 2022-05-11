""" break permite saltar al siguiente valor de x, evitando else, sin finalizar el bucle.
    Si la condición de if no se cumple, no se ejecutan print ni break por lo que el programa continua  
    la sentencia else y finaliza"""

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # Si no se encuentra un multiplo
            print(n, 'is a prime number')
