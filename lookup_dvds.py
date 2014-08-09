import MySQLdb, os

def SQLLookupDVD(searchby, searchtext):
    SQL = "SELECT * FROM DVD WHERE %s=%s" % (searchby, searchtext)
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        raw_input("Blad nacinisj [Enter..]")
        return
    os.system('cls')
    print ("Wyniki wyszukiwania:")
    print ("==============================")
    
    if not output:
        print ("Brak rekordow")

    for entry in output:
        print ("Tytul:             ", entry[0])
        print ("Rola glowna:       ", entry[1])
        print ("Rola drugoplanowa: ", entry[2])
        print ("Rok:               ", entry[3])
        print ("Gatunek:           ", entry[4])
        print ("==============================")
    raw_input("nacinij [Enter..]")
	
def LookupDVD():
    print('''' Kryteria wyszukiwania: Wprowadz cyfre [1:5]''')
    choice = raw_input("wpradz cyfre i nacinij [Enter..]")
    searchby = ""
    searchtext = ""
    if choice=='1':
        searchby = "DVD_TITLE"
        searchtext = raw_input("wproawdz tytul:")
        searchtext = "\"%s\""% (searchtext)
    elif choice=='2':
        searchby = "DVD_STAR_NAME"
        searchtext = raw_input("wprowadz nazwisko 1 :")
        searchtext = "\"%s\""% (searchtext)
    elif choice=='3':
        searchby = "DVD_COSTAR_NAME"
        searchtext = raw_input("wprowadz nazwisko 2 :")
        searchtext = "\"%s\""% (searchtext)
    elif choice=='4':
        searchby = "DVD_YEAR"
        searchtext = raw_input("wprowadz rok produkcji :")
        searchtext = "\"%s\""% (searchtext)
    elif choice=='5':
         searchby = "DVD_GENRE"
         searchtext = raw_input("wprowadz gatunek :")
         searchtext = "\"%s\""% (searchtext)
    else:
        print ("Bledny wybor")
        return
    SQLLookupDVD(searchby, searchtext)