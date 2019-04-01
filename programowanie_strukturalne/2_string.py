tekst = "Anna, paweł, JulIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print (type(lista)) #list

imie1 = lista[0]
print(imie1) #Anna

imieDuza = imie1.upper()
print(imieDuza) #ANNA

imieMale = imie1.lower()
print(imieMale) #anna

#sprawdzanie zawartosci

nazwisko = ""
print(nazwisko.isalpha()) #false

print ("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true or false

tekst1 = "\nJulia\n"
tekst2 = "Nowak"
print(tekst1 + tekst2)

tekst1 = tekst1.rstrip()
print(tekst1 + tekst2)
print(tekst1 + " " + tekst2)


#wyswietlenie lancucha znakow

#wszystkie znaki Pytona

text = "%s %s " % ("PHP", "Python" )
print(text)

#nowsze wersje pythona

text = "{1}, Java i {0} ".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

rok=2019
miesiac= "kwiecień"
dzien = 1
print("\nData:", end="")
print(dzien, miesiac, rok)
