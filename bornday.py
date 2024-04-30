bornyear = input('Year of birth Pushkin A.S.: ')

if bornyear == '1799':
    print('print his birhday')
    bornday = input('Day of born Pushkin A.S.: ')
    if bornday == '06.06':
        print('correct')
    else:
        print('incorrect')
else:
    print('incorrect')
    print('try again')
    again = input('last chance: ')
    if again == '1799':
        print('print his birhday')
        bornday = input('Day of born Pushkin A.S.: ')
        if bornday == '06.06':
            print('correct')
        else:
            print('incorrect')
print('end')