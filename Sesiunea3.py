#recapitulare
#variabila = loc din memorie in care stocam o valoare
# exemplu
# nume ="Ana"  #stocheaza un string
# varsta = 20  #stocheaza un numar intreg
# inaltime = 1.60  #stocheaza un numar zecimal
# semnul "=" egal atribuie o valoare unei variabile
# print() -> afiseaza informatii pe ecran

# print(nume)
# print(varsta)

# cu print = afisam text, valori numerice, variabile, verificam daca programul e corect
# print("Malina")
# print(25)
# print(varsta)
# print(nume, varsta)
# print(nume, 15)
#python pune automat spatiu intre variabile atunci cand sunt separate prin virgula
#print("Numele meu este:", nume)

#mai multe moduri de afisare cu print
#varianta 1 : cu virgula in print()

# nume="Malina"
# varsta= 22
# print("Numele este:", nume)
# print("Varsta este:", varsta)

#varianta 2: cu + intre stringuri
# prenume = "Ion"
# nume_familie = "Popescu"
# print (prenume + " " + nume_familie)
# + = concatenare de stringuri
# cand folosim + ambele parti trebuie sa fie stringuri

# oras ="Botosani"
# print ("Locuiesc in " + oras)

# varsta = 29 # -> daca voiam sa fie direct un string atunci o puneam intre " "
# print ("Am " + varsta + " ani") -> va fi eroare -> poti concatena doar stringuri, varsta este int

# print("Am " + str(varsta) + " ani") # -> am transformat variabila in str

#varianta 3: cu f-string / cu acolade {}
# nume = "Malina"
# varsta = 21
#
# print(f"Numele meu este {nume} si am {varsta} ani") #-> folosesc functia f"", in interior pot scrie text, folosesc {} pentru variabile
#
# print(f"nume {nume}" )
# f inainte de string spune a in interior vom pune variabile
#variabilele se scriu intre {}

#varianta 4: metoda format()
# nume = "Malina"
# varsta = 20
#
# print ("Ma numesc {} si am {} ani".format(nume,varsta))

#Exercitiul 1 - creaza o variabila nume si afiseaza
# nume ="Denisa"
# print(nume)
# print(f"Numele meu este {nume}")

#Exercitiul 2 - creaza 2 variabile - nume si oras si apoi afiseaza-le pe aceeasi linie
# nume = "Malina"
# oras = "Botosani"
#
# print(f"Numele meu este {nume} si sunt din {oras}")
# print ("Numele meu este ", nume, "si sunt din", oras)
# print(nume, oras)
#
# text = " a"
# print(len(text)) # -> functia length (lungime) - printezi lungimea textului/sirului

#Tipuri de date in Python:
#un tip de date arata ce fel de valoare avem intr-o variabila
# un nume este text, o varsta este un intreg, o inaltime este un numar zecimal float, o valoare de tip da/nu poate fi true/false
#fiecare tip de date are comportament diferit

#1. str = string= text
#stringul reprezinta textul
#exemple:
# nume= "Ana"
# oras= "Cluj"
# mesaj = "Salut"
# a= "Pyhton"
# B= 'CURS'
# #observatie - cifrele intre ghilimele vor fi considerate text-string, de exemplu "123" reprezinta textul 123, nu numarul 123
# #triple quotes - pentru stringuri care contin mai multe randuri
# text = """ Acesta este un text
# care contine mai multe randuri
# si se scrie intre triple quotes"""
# #print(text)
# """Acesta este un comentariu
# pe mai multe randuri """
# print(type(text))
#
#
# text = f""" Acesta este un text {nume}
# care contine mai multe randuri
# si se scrie intre triple quotes"""
# print(text)
#
# #diferenta dintre " " si """  """ -> cu ghilimele normale scriu pe un singur rand, cu cele triple pot scrie pe mai multe linii
# #\n - treci pe linia urmatoare
# print ( "Salut \n Buna ziua") #textul va fi scris pe o singura linie de cod dar la afisare va fi pe mai multe linii

#2. int = integer= numar intreg
# varsta = 25
# an= 2026
# nr_persoane = 15
#
# #3. float = numar zecimal
# inaltime = 1.60
# pret = 19.99
# temperatura = 15.5
# #in python zecimalele se scriu cu punct, nu cu virgula
# print(15.5)
# print(15,4) #virgula pune un spatiu
# print(15, 5+2)

# 4. bool = boolean = adevarat sau fals
#acest tip de date are doar 2 valori - True(Adevarat) sau False(Fals)
# invata_Python = True
# este_ziua_mea = False

# variabila= None #-> variabila goala








