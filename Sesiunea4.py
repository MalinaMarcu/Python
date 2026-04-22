# x = "25"
# y = int(x)
# print(y + 5)
#
# print("10" + "5") #105 - lipeste textul
#
# x="19.99"
# decimal = float(x)
# print(x)
# print(type(x))
# print(type(decimal))

#operatori aritmetici
#simboluri folosite pentru calcule matematice
# + -> adunare
# - -> scadere
# * -> inmultire
# / -> impartire
# ** -> ridicarea la putere
# // -> catul impartirii - impartirea intreaga
# % -> restul impartirii

# print(7 // 2)
# print ( 7/ 2)
# print ( 7 %  2)

#Adunare

# a = 10
# b = 5
# suma = a + b
# print(suma)
#
# #Scadere
#
# diferenta = a - b
# print(diferenta)
#
# #Inmultire
#
# produs = a * b
# print(produs)
#
# #Impartirea
#
# cat = a / b
# print(cat)
# print(int(cat))

#:.2f -> se foloseste ca sa afisam un numar zecimaal cu exact 2 cifre dupa virgula - > f - float si . 2 -> 2 zecimale poti folosi si 1f sau 10 f sau cat doresc si iti va afisa cate zecimale doresti

# rezultat = 10/3
# print(rezultat)
# print(f"{rezultat:.2f}")
# print(f"{rezultat:.4f}")
# Important! :.2f nu schimba valoarea, doar modul de afisare

#Impartirea intreaga

# print(10//3) # -> va afisa 3, doar partea intreaga

#Restul impartirii
# print (10%3)

#daca restul este 0 stim sigur ca numaarul este divizibil cu 2
#util pentru a verifica daca un numar este par sau impar

#puterea

# print ( 2**3 )
# print (5**2)
#
# #Ordinea operatiilor
# #In python se respecta ordinea matematica a operatiilor
#
# print(2 + 3 * 4)
# print ( (2+3) * 4) # parantezele schimba ordinea efectuarii operatiilor  exact ca la matematica a
#
# #in matematica = inseamna egalitate, in programare = inseamna atribuire
#
# x = 10 # x primeste valoarea 10, pune valoarea 10 in variabila x

#Functia input() ->cum citim date de la utilizator

#input() este o functie care permite utilizatorului sa scrie ceva de la tastatura

# nume = input("Cum te numesti?")
# print(nume)

# 1. programul afiseaza mesajul "cum te numesti"
# 2. utilizatorul scrie ceva
# 3. valoarea introdusa este salvata in variabila nume
#input() -> returneaza intotdeauna text

# varsta = input("Cati ani ai?\n ")
# print(varsta)
# print(type(varsta))
#
#
# varsta1 = int(input("Cati ani ai?\n "))
# print(varsta1)
# print(type(varsta1))
#
#
# inaltime = float(input("Ce inaltime ai? \n"))
# print(inaltime)
# print(type(inaltime))


# numar1 =input("Primul numar: ")
# numar2 =input("Al doilea numar: ")
# print (numar1 + numar2)
#
# numar1 =int(input("Primul numar: "))
# numar2 =int(input("Al doilea numar: "))
# print (numar1 + numar2)

# exemple de operatii aritmetice

# a=10
# b=3
#
# print("Adunare: ", a+b)
# print("Scadere: ", a-b)
# print("Inmultire: ",a*b)
# print("Impartire: ", a/b)
# print("Impartire intreaga: ", a//b)
# print("Restul impartirii: ", a%b)
# print("Puterea: ", a**b)

#greseli frecvente
# nume = Ana - ghilimele cand declari text
# inaltime = 1,75 - la variabilele de tip float folosim . nu ,
#cand unesti text cu un numar fara conversiwe
#varsta = 20
#print(" am " + varsta + " ani") = trebuie sa convertim variabila - str(varsta)
# input() returneaza intotdeauna text
#se confunda / cu //
# / -> rezultat decimal
# // -> doar partea intreaga

# exercitii:

#1. Citeste de la tastatura numele utilizatorului si afiseaza un mesaj

# nume = input("Introdu numele: ")
# print(f"Bun venit la curs {nume}")

#2. citeste de la tastatura doua numere intregi si afiseaza suma lor

# a= int(input("Primul numar: "))
# b= int(input("Al doilea numar: "))
# print ("Suma: ", a+b)

#3. citeste de la tastatura doua numere intregi si afiseaza suma, scaderea, inmultirea si impartirea

# a= int(input("Primul numar: "))
# b= int(input("Al doilea numar: "))
# print ("Suma: ", a+b)
# print ("Diferenta: ", a-b)
# print ("Inmultirea: ", a*b)
# print ("impartirea: ", a/b)
# print ("Impartirea intreaga: ", a//b)
# print ("Restul este: ", a%b)
# print( "Puterea este: ", a**b)

#4. citeste varsta de la tastatura si afiseaza peste 5 ani vei avea varsta de :

# varsta = int(input("Introduceti varsta: " ))
# x = 5 + varsta
# print(f"Peste 5 ani vei avea varsta de {x} ani")

#5. citeste un pret si o cantitate si calculeaza costul final

# pret = float(input("Pretul: "))
# cantitate = int (input("Cantitatea pentru care vreau sa calculez pretul: "))
# cost = pret * cantitate
# print (f"Costul total este: {cost}")
# print (f"Costul total este: {cost:.1f}")