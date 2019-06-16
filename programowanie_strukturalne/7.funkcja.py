7.1 funkcja

#przekaxywanie argumentów przez referencje

def show(name):
print(f'Przed modyfikacja :{name}')

name[0] = 'Beata'
name[1] = 'Barbara
name[2] = 'Bogdan'
print(f'Po modyfikacji :{name}')
print(f'Id po modyfikacji  :{id (name)}')

data = ['Anna', 'Agnieshka', 'Andrzej']
print(f'Przed wyłowaniem funkcji show: {data}')
print(f'Id objektu show {id(data)}')
print()
show (data)
print (f'Po wyłowaniu funkcji show {data}')


######### ałownik
print(f'Słownik:')
data1 = {0: 'Artur', 1:'Andrzej' }
print(f'id przed modyfikacja: {id(data1)}')
show (data1)

przekazywanie argumentu praez wartośc
print('\n\n')

def show(city):
print(f'Przed modyfikacja :{city}')

name[0] = 'Berlin'
name[1] = 'Londyn'
print(f'Po modyfikacji :{city}')
print(f'Id po modyfikacji  :{id (city)}')
 
miasto = ['Gniezno', 'Poznan']

print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'Id miasto show1 {id(miasto)}')
show1(list(miasto)
print(f'Po wywołaniu funkcji show1:{miasto}')



miasto1 = {
   0: 'Gniezno'
   1; 'Poznan'
}

print(f'Przed wywołaniem funkcji show1: {miasto1}')
print(f'Id miasto show1 {id(miasto1)}')
show1(list(miasto1)
print(f'Po wywołaniu funkcji show1:{miasto1}')
 

#######try except ############

def div(x,y):
     try:
    result x/y
      print(f'{x} / {y} = result')
     except ZeroDivisionError:
      print('\nError you are devided by zero')
div (2,0)

print(div(2,4))

