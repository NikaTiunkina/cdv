
###zmienne globalne i lokalne


#precyzja


x = "{0:.3f"}, format(5)
printf(x) #5.000


#napisz funkcle która jako argument przyjmuje wartość i zamienia dane po kursie zisejszym franka
wyswietl użytkownikowi ile  frankow kupi za podana kwote

def plnToChf(value)
 kursChf = 3.81849933
iloscChf = value // kursChf
print(f'Ilosc CHF: {iloscChf}')

plnToChf(500)


zmienna globalna

zmiennaGlobal = 10
print(f'Wartość zmiennej globalnej: {zmiennaGlobal}')
print(f'Id zmiennej globalnej: {id(zmiennaGlobal)}')


def spr():
global zmiennaGlobal
zmiennaGlobal = 20
print(f'\nWartość zmiennej globalnej wewnietrz funkcji: {zmiennaGlobal}')
print(f'\nId zmiennej globalnej wewnietrz funkcji: {id(zmiennaGlobal)}')

spr()
