for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
    else:
        # Loop fell through without finding a factor
        # Si no se encuentra un multiplo
        print(n, 'is a prime number')
