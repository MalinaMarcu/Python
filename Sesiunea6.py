# and -> inseamna adevarat doar daca toate conditiile sunt adevarate
# or -> inseamna adevarat doar daca un dintre conditii e adevarata
# not -> inverseaza valoarea
#
# ploua = False
# print(not ploua)

# Instructiunea FOR

#pentru a printa un mesaj de 5 ori:

# for i in range(5):
#     print("Salut")

# Instructiunea FOR este folosita atunci cand vrei sa repeti o actiune pentru fiecare element dintr-o colectie sau un anumit numar de pasi

# FOR -> ia pe rand fiecare valoare
#executa acelasi bloc de cod pentru fiecare valoare
#Utilitati:
#afisam mai multe valori
#parcurgem o lista
#procesam literele dintr-un text
#calcule
#repetam instructiuni de un numar fix de ori
#Sintaxa generala:

# for variabila in colectie
#     instructiune_1
#     instructiune_2
#     instructiune_3

#for -> aici incepe bucla
# variabila -> ia pe rand valorile
#in -> din/in
#colectie -> locul de unde luam valorile
#instructiunile din interior care trebuie sa fie indentate

# for i in range(5):
#     print(i)

#range(5) nu inseamna de la 1 pana la 5
#porneste de la 0
#se opreste inainte de 5

# for i in range(1, 10, 2): -> va genera de la 1 pana la 9 (n-1), din 2 in 2
#     print(i)

#ce este range()
#genereaza o secventa de numere

#3 variante
#range(stop) - range(5)
#range(start, stop) - range (0,5)
#range(start, stop, pas) - range(0,5,2)
#produce o serie de numere pe care bucla for le foloseste unul cate unul
#ii spunem de cate ori vrem sa se repete cate ceva (si) intre ce numere vrem sa mergem

#range(stop)

# for i in range(5):
#     print(i)

#range(start, stop) -> punctul de stop mereu cu 1 mai putin n-1

# for i in range(2,6):
#     print(i)

#range (start, stop, pas)

# for i in range(0, 10, 2):
#     print(i)

#ps negativ
# for i in range(10, 0, -1):
#     print(i)

#rolul variabilei din for
#i este o variabila care primeste pe rand valorile  -> pot declara orice variabila, nu neaparat i

#aceasta variabila este creata pentru bucla FOR
#isi schimba valoarea automat
#poate fi folosita in diferite operatii (calcule, conditii, afisari, etc)

#exemplu - calcul

# for i in range(5):
#     print(i+10)


# for i in range(3):
#     x = i+2
#     print(x)

#FOR nu este folosit doar pentru afisat valori
#se foloseste sa execute orice instructiune de mai multe ori

# for i in range(3):
#     print(i)
#     print("Salut")

#FOR si variabil deja existente - pot folosi o variabila deja declarata in interiorul buclei

# a= 10 #a ramane 10
#
# for i in range(3):
#     print(a+i)

#FOR si conditii IF
#putem folosi conditii if in interiorul buclei pentru a verifica o conditie la fiecare pas
#Exemplu:

# for i in range(6):
#     if i % 2 ==0:
#         print(i)

# bucla merge prin valorile 0, 1, 2, 3, 4, 5
#pentru fiecare valoare verifica daca este para
#doar valorile pare sunt afisate

#cum se citeste in pseudocod
#1. pentru fiecare numar i de la 0 pana la 5:
#2. daca i este par
#3. atunci afiseaza i

#prin for controlam repetarea iar prin i controlam decizia
# for i in range(5):
#     if i < 3:
#         print(f"{i} - valoare mica")
#     else:
#         print(f"{i} - valoare mare")

#FOR cu operatori de comparatie

# for i in range(5):
#     if i == 3:
#         print("am gasit 3")

#FOR si operatori logici

# for i in range(10):
#     if i >= 2 and i <= 6:
#         print(i)

#Recapitulare

#1. range(5) -> inseamna de la 0 pana la stop-1 deci pana la 4
#2. indentarea -> toate instructiunile pe care vrem sa le executam cu FOR trebuie sa fie indentate (cu un TAB in interiorul FOR ului)
#3. rolul variabilei i -> nu ramane mereu aceeasi: se schimba la fiecare pas: i este un nume dat de noi, putem defini orice valoare
# alte operatii pe care le poti folosi BREAK / CONTINUE

#1. BREAK - opreste complet bucla
#in momentul in care Python intalneste BREAK, iese din FOR si nu mai continua deloc cu rstul iteratiilor
#Exemplu:

# for numar in range(1,6): #range(1,6) -> produce 1,2,3,4,5
#     if numar == 3: # la 1 -> se afiseaza; la 2 -> se afiseaza; la 3 -> se executa break
#         break #-> bucla se opreste
#     print(numar)

#2. CONTINUE - nu opreste bucla, doar sare peste iteratia curenta si trece la urmatoarea

# for numar in range(1,6): # produce 1,2,3,4,5
#     if numar == 3: #la 1 -> se afiseaza; la 2-> se afiseaza; la 3-> se executa continue, nu va afisa 3, dar bucla va continua si vor fi afisate valorile 1,2,4,5
#         continue
#     print(numar)

#Exemplu:
#
# for litera in "python ":
#     if litera == "h":
#         break
#     print(litera)

# for litera in "python ":
#     if litera == "h":
#         continue
#     print(litera)

#EXERCITII

# sa se calculeze suma tuturor numerelor pare de la 1 la 20 inclusiv
#
# suma = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         suma = suma + i # pot folosi si suma += i
# print(suma)

#2. sa se parcurga numerele de la 1 la 30  inclusiv si sa se afiseze cate numere sunt: mai mari decat 10 si pare

# counter = 0
# for i in range(1,31):
#     if i > 10 and i %2 ==0:
#         counter = counter + 1
# print(counter)

#3. sa se calculeze suma numerelor de la 1 la 100 care sunt divizibile si cu 3 si cu 5

# suma =0
# for i in range(1,101):
#     if i % 3 ==0 and i % 5 == 0:
#         suma += i
# print(suma)

#4. sa se parcurga numerele de la 1 la 10 pentru fiecare numar se calculeaza: rezultat = i *3 -2 sa se afla cea mai mare valoare obtinuta

# maxim = 0
# for i in range(1,11):
#
#     rezultat = i *3 -2
#     if rezultat > maxim:
#         maxim = rezultat
# print(maxim)

#5. se da un text : pentru fiecare vocala incrementam cu 2, iar pentru fiecare consoana cu 1.. la final afiseaza totalul punctelor


# text ="python"
# puncte = 0
#
# for litera in text:
#     if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
#         puncte = puncte + 2
#     else:
#         puncte = puncte + 1
# print (puncte)

