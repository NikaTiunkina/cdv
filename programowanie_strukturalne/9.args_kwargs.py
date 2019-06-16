def wyswietl(num1, num2):
  print(f'liczba1:{num1}')
  print(f'liczba2:{num2}')
wyswietl(2,4)

########### *args

def wyswietlArgs(num1, *args) :

   print(f'\nPierwzsy element:{num1}')

for i in args:
    print(f'Następny element: {i}')

wyswietlArgs(2, 33, 21, 100)


###### kwargs ######

import os

os.system('cls')

def pracownik(**kwargs):

   # print(kwargs)
   for key, val in kwargs.items();
    print(f'Klucz: {key}, wartość; {val}')


pracownik1 = {
        'fName' : 'Janusz',
        'lName' : 'Nowak',
        'age' : 23,
        'city' : 'Poznan',
        'job': True
}
pracownik(**pracownik1)

 



a^2


def div(x,y):
     try:
    result x+y
    x**2
   
      print(f'{x} + {y} = result')
     result1 x+y

     (x+y)**2

     print(f'{x} + {y} = result1')

     result2 result/result1

      print(f'{result} / {result1} = result2')  

     except ZeroDivisionError:
      print('\nError you are devided by zero')
div (2,3)

