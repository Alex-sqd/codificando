counter = 10
index = 1
sum = 0

while index <= counter:
    try:
        number = int(input('Enter a number: '))
        sum = sum + number
        index = index + 1
    except:
        print('Please enter an integer')
        break

print('Sum of numbers = ', sum)
