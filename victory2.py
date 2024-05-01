correct = 0
incorrect = 0

bornyear1 = input('Year of birth Einstein A.: ')
if bornyear1 == '1879':
    correct +=1

else:
    incorrect +=1

bornyear2 = input('Year of birth Mozart W.A.: ')
if bornyear2 == '1756':
    correct +=1
else:
    incorrect +=1

bornyear3 = input('Year of birth Shakespeare W.: ')
if bornyear3 == '1564':
    correct +=1
else:
    incorrect +=1

bornyear4 = input('Year of birth Curie M.: ')
if bornyear4 == '1867':
    correct +=1
else:
    incorrect +=1

bornyear5 = input('Year of birth Gandhi M.: ')
if bornyear5 == '1869':
     correct +=1
else:
     incorrect +=1

print('правильные ответы: ', correct)
print('неправильные ответы: ', incorrect)

famous = 5

prc_correct = (correct/5)*100
prc_incorrect = (incorrect/5)*100

print('процент правильных ответов: ', prc_correct)
print('процент неправильных ответов: ', prc_incorrect)