continuar = 's'
while continuar != 'n':
    try:
        dividendo = int(input('Numerador: '))        
        divisor = int(input('Divisor: '))
        cociente = dividendo // divisor
        resto = dividendo % divisor
        print ('Cociente: ', cociente)
        print ('Resto: ', resto)
        continuar = input('¿Desea continuar? (n para finalizar) ')
    except ZeroDivisionError:
        print ('Error de división por cero')
        break
    except:
        print ('Descansa e inténtalo en otro momento')
        break

