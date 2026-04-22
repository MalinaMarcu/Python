#Conditionale - if/elif/else
#o conditie este o expresie care poate fi adevarata sau falsa
#pe baza ei putem decide daca anumite blocuri de cod se pot executa

#if conditie:
    #codul se executa daca conditia este True
#elif alta conditie:
    #codul se executa daca prima conditie nu a fost adevarata dar aceasta este
#else:
    #codul se executa daca niciuna dintre conditiile anterioare nu a fost adevarata/indeplinita

#EXEMPLE:

# varsta = 18
#
# if varsta >=18:
#     print("Ai voie sa votezi")
# else:
#     print("Esti prea tanar sa votezi")

#python foloseste indentare deci nu folosim acolade

#operatori logici : <, >, =<, >=, == , !=
#1. AND -> ambele conditii trebuie sa fie True / Adevarate
#2. OR -> cel putin una din conditii trebuie sa fie True
#3. NOT -> inverseaza valoarea

#1. Egal cu - ==
# x= 5
#
# if x == 5:
#     print("x este egal cu 5")

#2. Diferit de - !=

# if x != 10:
#     print("x NU este egal cu 10")

#3. Mai mare decat - >

# temperatura = 30

# if temperatura > 25:
#     print("afara sunt mai mult decat 25 de grade ")
#
# #4. Mai mic decat - <
#
# elevi = 15
# if elevi < 20:
#     print("clasa ese mai mica de 20 de elevi")

#5. Mai mare sau egal - >=

# varsta = 18
# if varsta >= 18:
#     print("ai voie sa votezi")
#
# #6. Mai mic sau egal =<
# pret = 99
# if pret <= 99:
#     print("pretul este mic")

#1. AND
# varsta = 20
# nationalitate = "roman"
#
# if varsta > 18 and nationalitate == "roman":
#     print("poti vota")
# else:
#     print("nu poti vota")

#2. OR
# zi = "sambata"
#
# if zi == "sambata" or zi =="duminica":
#     print("este weekend")

#3. NOT

# ploua = False
# if not ploua:
#     print("vremea este frumoasa" )

#if not -> aceasta este o verificare de tip falsy -> python interpreteaza valoarea lui "x" in contextul de adevar sau fals
#if x -> acesta verifica daca x este adevarat truthy
#if not x -> verifica daca x este fals
#valori considerate falsy in python -> none, False,0 (oricenumar 0), ''/"" -> sir gol, [] -> lista goala, {} -> dictionar gol, set() -> set gol, () -> tuplu gol - colectii de date

#EXEMPLE

# x = 0 # -> adica este false
# print(bool(x))
# print(not x)
#
# if not x:
#     print("este zero")
#
# x = ''
# if not x:
#     print ("string gol")
#
# x= [1,2,3]
# if not x:
#     print("Lista este goala")

#Alte modalitati de a scrie if
#1. if pe o singura linie
# x=3
# if x % 2 == 0: print("numar par")
# if x % 2 != 0: print("numar impar")

#2. if ternar (pe o singura linie si iti inlocuieste if/else)
# x= 7
# rezultat = "Par" if x % 2 == 0 else "impar"
# print(rezultat)


# if x % 2 == 0:
#     rezultat = "par"
# else:
#     rezultat = "impar"
# print(rezultat)

#3. if cu in (verificare apartenenta)
# litera = 'a'
# if litera in 'aeiou':
#     print("este vocala")

#4. if cu bool() (conditie implicita)
# nume = "maria"
# print(type(nume))
# print(bool(nume))
# nume2 =""
# print(type(nume2))
# print(bool(nume2))
#
# if nume: #-> string ul este implicit adevarat, doar cel declarat gol este false
#     print(" ai introdus un nume")

#5. if comparativ cu mai multe valori
# x = 7
# if 5 <  x <  10:
#     print("x este intre 5 si 10")

#6. nested if - if in interiorul altui if - folosit pentru mai multe niveluri de verificare

# varsta = int(input("introdu varsta ta: "))
#
# if varsta >= 18:
#     print ("esti adult")
#
#     if varsta >= 65:
#         print("esti pensionar")
#     else:
#         print("esti  apt de munca")
# else:
#     print("esti minor")

#EXERCITII

#1. citeste un numar de la tastatura si afiseaza daca este par sau impar

# numar = int(input("Introdu numarul: "))
# if numar % 2 == 0:
#     print("numar par")
# else:
#     print("numar impar")

#2. afiseaza daca un numar introdus este pozitiv sau negativ sau 0
# numar = int(input("Introdu numarul: "))
# if numar > 0:
#     print("Numarul este pozitiv")
# elif numar < 0 :
#     print ("Numarul este negativ")
# else:
#     print("Numarul este 0")

#3. verifica daca un numar introdus de la tastatura este intre 1 si 100 inclusiv
#numar = int(input("Introdu numarul: "))
#
# if numar >= 1 and numar <= 100:
#     print ("numarul se afla in intervalul 1 - 100")
# else:
#     print ("numarul nu se afla intre 1-100")

#4. daca temperatura este sub 0 - afiseaza ger , intre 0 si 15 - afiseaza frig 16-25 - afiseaza placut , peste 25 cald

temperatura = int(input("Introdu temperatura: "))

if temperatura < 0:
    print("ger")
elif temperatura >= 0 and temperatura <=15:
    print("frig")
elif temperatura >=16 and temperatura <=25:
    print("placut")
elif temperatura > 25:
    print("cald")