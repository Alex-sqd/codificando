for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
    else:
        # Si no se encuentra un multiplo
        print(n, ' Es un número primo.')
