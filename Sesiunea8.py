import turtle


#functii in python

#bloc de cod reutilizabil care executa o sarcina -> scopul este de a scrie codul mai clar si mai usor de intretinut

#sintaxa
# def nume_functie(parametrul1, parametrul2, ...):
#     #bloc de cod
#     return valoare

# def salut(nume):
#     print(f"Salut, {nume}")
#
# salut("Florin")

#Functii cu return

# def adunare(a,b):
#     return a+b
#
# rezultat = adunare(3,5)
# print(rezultat)

#Functii fara parametri sau return

# def afiseaza_mesaj():
#     print("functie fara parametri")
#
# afiseaza_mesaj()

#parametrii default/impliciti

# def salut(nume="user"):
#     print(f"Salut, {nume}")
# salut()
# salut("Florin")

#domenii de vizibilitate/ scope

#variabile :
#1. globale
#2. locale
#3. enclosing - functii nested
#4. built-in - functii/variabile predefinite

# x = 10#variabila globala
#
# def test():
#     x = 5 #variabila locala
#     print("Local: ", x)
#
# test()
# print("Global: ", x)

#modificare variabila globala dintr-o functie

# x = 10
#
# def modificat():
#     global x
#     x = 20
#
# print(x)
# modificat()
# print(x)

#scope enclosing (functii nested)

# def functie_exterioare():
#     mesaj = "Exterior"
#
#     def functie_interioara():
#         print(mesaj)
#     functie_interioara()
# functie_exterioare()

#functii lambda (functii anonime)

# suma  = lambda a, b: a+b
# print(suma(3,4))

#enclosing scope (nonlocal)

# def exterior():
#     x= 10
#     def interior():
#         nonlocal x
#         x += 1
#         print(x)
#     interior()
# exterior()

#LEGB - python cauta variabilele in urmatoarea ordine:
#1. local
#2. enclosing
#3. global
#4. built-in

#exemplu legb

# x= "global" # global scope
#
# def functie_exterioara():
#     x = "enclosing" #enclosing scope - vriabila definita in functia exterioara
#
#     def functie_interioara():
#         x = "local" #local scope
#         print("in functia interioara: ", x) #afiseaza variabila locala
#
#     functie_interioara()
#     print("In functia exterioara: ", x)
# functie_exterioara()
# print("In afara functiilor: ", x)

#Exercitii:
#o functie care gaseste cel mai mare numar

# def cel_mai_mare_nr(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b> c:
#         return b
#     else:
#         return c
# rezultat = cel_mai_mare_nr(13, 10, 21)
# print("Cel mai mare nr este: ", rezultat)

#o functie care verifica un nr par
# def este_par(numar):
#     return numar % 2 == 0
#
# print(" este 4 par?: ", este_par(4))
# print(" este 5 par?: ", este_par(5))

#numaratoare inversa

# def countdown(n):
#     while n >= 0:
#         print(n)
#         n -= 1
# countdown(10)
#

#instructiune RETURN - folosita in functia pyhton ca sa returneze o valoare ca rezultat al executiei
#return - opreste executia functiei
#return - spefica o valoare inapoi
# return none

#functie care returneaza o valoare
#
# def suma(a, b):
#     suma=a+b
#     return suma
# rezultat = suma(1,2)
# print(rezultat)

#return care opreste functia

# def functie():
#     print("Inainte de retunr")
#     return
#     print("dupa return")
# functie()

#fara return explicit - None

# def salut():
#     print("Salut")
# x= salut()
# print(x)

#return poate afisa valori multiple

# def test():
#     return 2,3
#
# x, y = test()
# print(x, y)

#modalitate                  #ce returneaza
#1. return valoare          1. intoare "valoarea"
#2. return                  2. None
#3. nicio instructiune      3. intoare None
#4. return x, y, z          4. intoarce tuplu (x, y, z)

#util ca sa separi logica functiei de restul codului

#desanare un patrat/dreptunghi

# def patrat():
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
# turtle.speed(1)
# patrat()
# turtle.done()

#EXERCITIU: CALCULATOR SALARIU

# def calculeaza_salariu_net(salariu_brut):
#     impozit = salariu_brut * 0.10
#     cas = salariu_brut * 0.25
#     salariu_net = salariu_brut - impozit - cas
#     return salariu_net
#
# def afiseaza_fluturas(salariu_brut):
#     impozit = salariu_brut * 0.10
#     cas = salariu_brut * 0.25
#     salariu_net = calculeaza_salariu_net(salariu_brut)
#
#     print("Fluturas salariu")
#     print("Salariu brut: ", salariu_brut)
#     print("Impozit 10%: ", impozit)
#     print("cas 25% : ", cas)
#     print("Salariu net: ", salariu_net)
#
# brut = float(input("Introdu salariul brut: "))
# afiseaza_fluturas(brut)

#primeste temperatura in grade celsius
#converteste in kelvin si fahrenheit
#afiseaza rezultatele
#counter pt cate conversii s-au facut - global cope
#variabila unitate pentru scope enclosing

numar_conversii = 0

def conversie_temperatura():
    #enclosing scope
    unitate = "celsius"

    celsius = float(input("Introdu temperatura in grade Celsius: "))

    def calculeaza():
        #local scope
        f = celsius * 9 / 5 + 32
        k = celsius + 273.15

        print(f"\n Temperatura introdusa: {celsius} {unitate}")
        print(f"Fahrenheit : {f}")
        print(f"Kelvin: {k}")

        global numar_conversii
        numar_conversii += 1

    calculeaza()
conversie_temperatura()
conversie_temperatura()

print(f"nr conversii efectuate: {numar_conversii}")