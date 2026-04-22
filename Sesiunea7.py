
import random

#am importat o librarie care imi genereaza numere - pot adauga ce librarie AM NEVOIE


#while - o instructiune care este o structura de control care executa un bloc de cod atata timp cat o conditie este adevarata

#Sintaxa
#while conditie:
    #bloc de cod executat daca conditia este True

#Exemplu:

# x=0
# while x<5:
#     print(x)
#     x+=1

#INFORMATII GENERALE:
#1. Conditia trebuie sa se schimbe ALTFEL STRUCTURA VA RULA LA INFINIT

# while True:                       #structura va fi tot timpul adevarata/ bucla nu se va opri
#     print("Ruleaza la infinit")


# x= 0
# while True:
#     print("aragaz")
#     x+=1
#     if x==30:
#         break

#Daca nu modifici variabilele din conditie vei crea o bucla infinita / loop infinit

#2. Comanda BREAK

# x= 0
# while True:
#     print("aragaz")
#     x+=1
#     if x==3:
#         break #cand x va fi 3, bucla se va opri, tot codul va afisa cuvantul de 3 ori

#3. Comanda CONTINUE

# x= 0
# while x<5:
#     x+=1 #incrementare  x-=1 ->decrementare
#     if x==3:
#         continue #cand va ajunge la 3, se va relua bucla, deci il va sari pe 3
#     print(x)

#4. else in while

# x=0
# while x<3:
#     print(x)
#     x += 1
# else:
#     print("while s-a terminat")

#se executa daca bucla se incheie in mod normal, fara break

#cazuri de utilizare

#1. Numarare

# x=10
# while x>0 :
#     print(x)
#     x -= 1

#2. Asteptare pana la o conditie

# conditie = ""
# while conditie != "exit":
#     conditie = input("Scrie 'exit' pentru a iesi: ")

#3. Validare input

# valoare= int(input("Introdu un numar pozitiv: "))
# while valoare  <= 0:
#     valoare = int(input("Numar invalid. Reincearca: "))

#while TRUE cu BREAK

# while True:
#     comanda= input("Comanda: ")
#     if comanda == 'stop':
#         break
#     print("Ai tastat: ",comanda)

#blocul try/ except
#folositi pentru gestionarea exceptiilor(pentru a prinde si trata erori care pot aparea in timpul rularii unui program) fara ca acesta sa se opreasca brusc

#Sintaxa

# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("Nu poti imparti la zero")

# try:
#     numar = int(input("Introdu un numar: "))
#     print("Numarul este: ", numar)
# except ValueError:
#     print("Nu ai introdus un numar valid")

#fara try/ except va genera eroare in momentul in care introduci un string, de exemplu, try si except te ajuta sa printezi un mesaj in loc de eroare
# numar = int(input("Introdu un numar: "))
# print("Numarul este: ", numar)

# try:
#     x = 1/0
# except: #va cumprinde toate erorile, e generic, nu este recomandat pt ca nu vei sesiza de unde e eroarea
#     print("a aparut o eroare")



#1. Generare de numere prime - un numar mai mare decat 1 care se divide cu 1 si el insusi - exemplu: 2,3,5,7, etc.    #0,1- nu sunt prime

# numar = 2 #numarul pe care il verifica
# while numar <= 20: #cat timp numarul curent este mai mic sau egal cu 20, repeta instructiunile
#     divizor = 2 #variabila cu care incercam sa impartim numarul
#     prim = True #am pus true la inceput pentru ca presupunem ca numarul este prim
#     while divizor < numar: #cat timp divizorul este mai mic decat numarul, verifica daca numarul se imparte exact la acel divizor
#         if numar % divizor == 0: #verifica daca se divide exact, Daca se indeplineste, inseamna ca numar se divide exact la divizor
#             prim = False #numarul nu mai este prim
#             break #oprim imediat bucla INTERIOARA
#         divizor += 1 #daca nu s-a impartit exact, trecem la urmatorul divizor
#     if prim: #daca variabila prim este inca True, inseamna ca nu am gasit niciun divizor
#         print(numar)
#     numar += 1 #dupa verificare trecem la urmatorul numar


#Ghiceste numarul:
#VARIANTA FARA MODULUL RANDOM:
# numar_secret = 7
# ghicire = None
#
# while ghicire != numar_secret:
#     ghicire = int(input("Ghiceste numarul: "))
# print("Ai ghicit")

#VARIANTA CU MODULUL RANDOM:

# numar_secret = random.randint(1, 3)
# ghicire = None
# while ghicire != numar_secret:
#     try:
#         ghicire = int(input("Ghiceste numarul(1 - 3): "))
#     except ValueError:
#         print("Introdu un numar valid: ")
#         continue
# print("Ai ghicit")

# numar_secret = random.randint(1, 3)
# ghicire = None
# while ghicire != numar_secret:
#     ghicire = int(input("Ghiceste numarul(1 - 3): "))
# print("Ai ghicit")

# numar_secret = random.randint(1, 30)
# ghicire = None
# incercari = 0
# incercari_maxime = 5
# while ghicire != numar_secret and incercari <= incercari_maxime: #fiind <= incercarile maxime vor fi incercari_maxime+1
#     try:
#         ghicire = int(input("Ghiceste numarul(1 - 30). Ai 6 incercari: "))
#         incercari += 1
#         if ghicire < numar_secret:
#             print("Numarul este mai mare")
#         elif ghicire > numar_secret:
#             print("Numarul este mai mic")
#     except ValueError:
#         print("Introdu un numar valid: ")
#         continue
# if ghicire == numar_secret:
#     print(f"Ai ghicit din {incercari} incercari")
# else:
#     print(f"Ai pierdut, numarul era: {numar_secret}")

#Exercitiu:
#simulator bancomat
#avem un sold initial de 1000 LEI. Vrem sa afisam un meniu:
#1. Vezi sold
#2. Depune bani
#3. Retrage bani
#4. iesire
#reguli:
#1. Meniul trebuie repetat pana cand userul alege iesirea
#2. la retragere nu ai voie sume mai mari decat soldul
#3. fara sume negative sau 0
#4. dupa fiecare operatie afisezi soldul nou

sold = 1000.0
aplicatia_ruleaza = False
pin_corect = "1234"
incercari_maxime = 3
autentificat = False

incercari = 0

while incercari < incercari_maxime:
    pin_introdus = input("Introdu PIN: ")

    if len(pin_introdus) != 4:
        print("PIN trebuie sa contina 4 cifre")
        incercari +=1
        incercari_ramase = incercari_maxime - incercari
        print(f"Incercari ramase: {incercari_ramase}")
        continue

    if pin_introdus == pin_corect:
        print("Autentificare OK")
        autentificat = True
        break
    else:
        incercari = incercari + 1
        incercari_ramase = incercari_maxime - incercari
        print("PIN incorect")
        print(f"Incercari ramase: {incercari_ramase}")

if autentificat == False:
    print("Card blocat. Prea multe incercari")

if autentificat == True:
    aplicatia_ruleaza = True
    while aplicatia_ruleaza:
        print("\n**** MENIU ****")
        print("1. Vezi sold")
        print("2. Depune bani")
        print("3. Retrage bani")
        print("4. Iesire")
        print("****************\n")

        optiune = input("Alege o optiune (1-4): ")

        if optiune == "1":
            print(f"Soldul curent este: {sold:.2f} LEI ")
        elif optiune == "2":
            suma_text = input("Introdu suma pe care vrei sa o depui: ")
            try:
                suma= float(suma_text)
                if suma <= 0:
                    print("Suma introdusa trebuie sa fie mai mare decat 0")
                else:
                    sold = suma + sold
                    print(f"Ai depus {suma:.2f} LEI")
                    print(f"Noul sold este {sold:.2f} LEI")
            except ValueError:
                print("Valoare invalida. Introdu un numar valid")
        elif optiune == "3":
            suma_text = input("Introdu suma pe care vrei sa o retragi: ")
            try:
                suma= float(suma_text)
                if suma <= 0:
                    print("Suma introdusa trebuie sa fie mai mare decat 0")
                elif suma > sold:
                    print("Fonduri insuficiente")
                else:
                    sold = sold - suma
                    print(f"Ai retras {suma:.2f} LEI")
                    print(f"Noul sold este {sold:.2f} LEI")
            except ValueError:
                print("Valoare invalida. Introdu un numar valid")
        elif optiune == "4":
            print("Iesire din meniu")
            break # sau aplicatia_ruleaza = False
        else:
            print("Optiune invalida")

