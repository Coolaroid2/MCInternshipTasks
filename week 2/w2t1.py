#Weight Converter
print('--------Weight Converter--------')
while True:
    choice = input('\nEnter a choice (1 for kilograms to pounds, 2 for pounds to kilograms): ')
    try:
        if int(choice) == 1:
            x = int(input('Enter number of kilograms to convert: '))
            print(f'\n{x} kilograms is equal to {x*2.2} pounds')
            break
        elif int(choice) == 2:
            x = int(input('Enter number of pounds to convert: '))
            print(f'\n{x} pounds is equal to {x/2.2} kilograms')
            break
        else:
            print('\nPlease enter a valid choice (1 for kilograms to pounds, 2 for pounds to kilograms)')
    except:
        print('\nPlease enter a valid choice (1 for kilograms to pounds, 2 for pounds to kilograms)')