import os

#La comanda os.listdir ens llegeix tots els arxius que estan a la carpeta curses
fitxers = os.listdir('curses/')
#per cada arxiu que està al directori curses
con=0
for nomFitxer in fitxers:
  
    #nomFitxer conté el nom de l'arxiu que està en el directori curses 
    #TODO heu de posar a la variable fitxer l'obertura per lectura del fitxer de nom nomFitxer.
    fitxer =open("curses/"+nomFitxer,"r")
    print(fitxers[con])
    #Heu de pintar les tres primeres posicions 
    print("Or: ",fitxer.readline())
    print("Plata: ",fitxer.readline())
    print("Bronze: ",fitxer.readline())
    con=con+1