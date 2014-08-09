import MySQLdb, os

def SQLDeleteDVD(dvdToDelete):
    try:
        SQL_DELETE = "DELETE DVD FROM DVD WHERE DVD_TITLE = \
        \"%s\"" % dvdToDelete
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_DELETE)
        db.commit()
        c.close()
        db.close()
        raw_input("Rekord zostal usuniety")         
    except:
        print("wystapil problem z usunieciem rekordu z bazy")
        raw_input("Nacisnij [Enter..]")
        return 

def DeleteDVD():
    os.system('cls')
    dvdToDelete = raw_input("\nWprowadz tytul do usuniecia: ")
    SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \
    \"%s\"" % dvdToDelete
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_LOOKUP)
        searchResult = c.fetchall()
        if searchResult[0]==():
            raise
    except:
        print("Wystapil problem z dostepem do rekordu w bazie")
        raw_input("Nacisnij [Enter..]")
        return
    print("Usuwany rekord:")
    print ("1: Tytul\t", searchResult[0][0])
    print ("2: Star\t", searchResult[0][1])
    print ("3: Costar\t", searchResult[0][2])
    print ("4: Rok\t", searchResult[0][3])
    print ("5: Gatunek\t", searchResult[0][4])
    print("czy na pewno chcesz usunac?\nT/t = tak, inny znak = nie")
    choice = raw_input("\t")
    if choice=="T" or choice=="t":
       SQLDeleteDVD(dvdToDelete)
    else:
        c.close()
        db.close()
        raw_input("Rekord nie zostal usuniety, nacisnij [Enter..]")
