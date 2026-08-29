def exercise ():
    total = 0

    while (True):
        try:
            no = int(input('Enter Number (Even Number to continue, Odd number to break): '))

            if no % 2 > 0:
                break
            
            total += no
        
        except ValueError:
            print('Try Enter number again')


    print('')
    print('Total Sum: ', total)
