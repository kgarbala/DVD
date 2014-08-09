# DVD.PY
# PROGRAM DO ZARZADZANIA BAZA DANYCH KOLEKCJI FILMOW
# POWSTAL NA PODSTAWIE PROJEKTU JAMES'A O. KNOWLTON'A
# W KSIAZCE "PYTHON PROJEKTY DO WYKORZYSTANIA". 
# Python: 2.7
# MySQL 5.6.19 Community Server (GPL)
# Platoforma: Windows
# KRZYSZTOF GARBALA

import os
import add_dvd, lookup_dvds, modify_dvd, delete_dvd, csvreport_dvd

def menu():
    global choice
    #os.system('cls')
    print(''' Baza Filmow:
    1. dodaj
    2. przeszukaj
    3. modyfikuj
    4. usun
    5. eksportuj csvreport_dvd
    6. Koniec
    ''')
    choice = input("Wybierz opcje:")
    return choice
choice = ''

while choice!=6:
    choice=menu()
    os.system('cls')
    if choice==1:         
        add_dvd.AddDVD()
        os.system('cls')
    elif choice==2:
        os.system('cls')
        lookup_dvds.LookupDVD()
    elif choice==3:
        os.system('cls')
        modify_dvd.ModifyDVD()
    elif choice==4:
        os.system('cls')
        delete_dvd.DeleteDVD()
    elif choice==5:
        os.system('cls')
        csvreport_dvd.writeCSV()        
    else:
        if choice !=6:
            os.system('cls')
