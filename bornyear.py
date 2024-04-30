bornyear = input('Year of birth Pushkin A.S.: ')

if bornyear == '06.06.1799':
    print('correct')
else:
    print('incorrect')
    print('try again')
    again = input('last chance: ')
    if again == '06.06.1799':
        print('correct')

print('end')