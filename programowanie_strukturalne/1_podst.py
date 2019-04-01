print("CDV")
print(10)


#komentarz

'''
komentarz
w
wielu
liniach
'''

#potegowanie
potega = 2 ** 10
print (potega)

#pobieranie danych z klawiatuey

imie = input()
#+ to konkatenacja
print ("Twoje imie podane z klawiatury :" + imie)

nazwisko = input ("Podaj nazwisko: ")
print("Twoje mazwisko podane z klawiatury", nazwisko)

#Twoje imię: [zmienna imie], twoje nazwisko [zmoienna imie]

print("Twoje imie: " + imie, ", twoje nazwisko: " + nazwisko )

'''
Użytkownik podaje z klawiatury swój wiek,
wyświetli dane w formacie: Twój wiek: [wiek] lat


 print("Podaj swoj wiek: ", end="")
  wiek= input()

  print (type(wiek)) #str
  print("Twoj wiek: " + wiek +" lat")

  wiek1= 20

  print (type(wiek1))
  wiek1= str(wiek1)
    print("Twoj wiek: " + wiek1 +" lat")
'''

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]

print(pierwszyZnak)

dlugosc = len(nazwisko)
print("Długość:", dlugosc )

ostatniZnak = nazwisko[len(nazwisko) - 1]
print("Ostatni znak: ", ostatniZnak )

ostatniZnak = nazwisko[-1]
print("Ostatni Znak:", ostatniZnak )

#konwersja

x= "5"
print(type(x)) #str
x= int(x)
print(type(x)) #int

y="10"
print(type(y))
#y= y / 2
#print(type(y)) #float

#print(y) #5.0

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl
