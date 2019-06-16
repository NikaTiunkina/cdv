programowanie = ['Python', 'C#', 'JS','PHP', 'Java']

print(programowanie)
print(type(programowanie))

pierwszy = programowanie [0]
print('Pierwszy język programowania: ' +pierwszy)

trzyElementy = programowanie[0:3]

print(trzyElementy)

ostatni = programowanie[-1]

print('Ostatni język programowania: ' +ostatni)

#Dodanie nowego elementu do listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#Zliczanie elementow w liscie
ile = programowanie.count('Python')
print(f'Python wystepuje {ile} razy')

#ilosc elementow w naszeq liscie
iloscElem = len(programowanie)
print('Ilosc elementow w liscie:', end='' )
print(iloscElem)

#polaczenie list
print(f'\n\n{programowanie}')
inneJezyki = ['c', 'c++']
print('Połączenie list')
programowanie.extend(inneJezyki)
print(programowanie)

#wyczyscczenie listy
nowa = programowanie
print(f'Nowa lista: {nowa}')
nowa.clear()
print(f'Nowa lista po wyczyscczeniu: {programowanie}')

programowanie = ['Python', 'C#', 'JS','PHP', 'Java']

print(programowanie)
print(type(programowanie))

pierwszy = programowanie [0]
print('Pierwszy język programowania: ' +pierwszy)

trzyElementy = programowanie[0:3]

print(trzyElementy)

ostatni = programowanie[-1]

print('Ostatni język programowania: ' +ostatni)

#Dodanie nowego elementu do listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#Zliczanie elementow w liscie
ile = programowanie.count('Python')
print(f'Python wystepuje {ile} razy')

#ilosc elementow w naszeq liscie
iloscElem = len(programowanie)
print('Ilosc elementow w liscie:', end='' )
print(iloscElem)

#polaczenie list
print(f'\n\n{programowanie}')
inneJezyki = ['c', 'c++']
print('Połączenie list')
programowanie.extend(inneJezyki)
print(programowanie)

#wyczyscczenie listy
nowa = programowanie
print(f'Nowa lista: {nowa}')
nowa.clear()
print(f'Nowa lista po wyczyscczeniu: {programowanie}')

