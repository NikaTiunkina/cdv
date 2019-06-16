#moduł math
#pi

import math
pi = math.pi
print(pi)

#pierwiastek
pierwiastek = math.sqrt(9)
print(pierwiastek)

#moduł random

import random
losuj = random.random()
print(f'Zmienna wylosowana: {losuj}')

losujZlisty = random.choice([1,2,3,4])


print(f'Wylosowana liczba z listy: {losujZlisty}'  )

########################

x = 5
if x == 5:
 print('x jest rowne 5')
 #x = str(x)
 #print ('wartosc x= ' +x)
 print('Wartosc x =', x)
else:
     print('x jest rowne 5')
     print('Wartosc x =', x)

#######################

y = True  #False

if y:
    print('prawda')
else:
   print('falsz')

#########################
# j = '1'
# j = '0'
j = '' #False
j = False
if bool(j):
    print('true')
else:
    print('false')
########################

k = input('Podaj wartosc dla zmiennej k: ')
k = float(k)

if bool(k):
    print('true')
else:
    print('false')
########################

if True:
        print('true')
else:
        print('false')

