import MySQLdb 

def SQLAddDVD(Title, Star, Costar, Year, Genre):
    SQL = 'INSERT INTO dvd values("%s","%s","%s","%s","%s")' %\
    (Title, Star, Costar, Year, Genre)
    try: 
        db = MySQLdb.connect('localhost', 'root', 'niepowiem', 'dvdcollection')
        c = db.cursor()
        c.execute(SQL)
        db.commit()
        c.close()
        raw_input("Rekord zostal dopisany.[ENTER..]")
    except:
        raw_input("Blad.[ENTER..]")
   
def AddDVD():
    Title = raw_input("Wprowadz tytul:")
    Star = raw_input("Wprowadz Star:")
    Costar = raw_input("Wprowadz CoStar:")
    Year = raw_input("Wprowadz Year:")
    Genre = raw_input("Wprowadz Genre:")
    SQLAddDVD(Title, Star, Costar, Year, Genre)
