import os

#La comanda os.listdir ens llegeix tots els arxius que estan a la carpeta html
fitxers = os.listdir('html/')
for nomFitxer in fitxers:
    #nomFitxer conté el nom de l'arxiu que està en el directori html 
    #s'obre per lectura
    fitxer = open('html/'+nomFitxer,"r")
    #Heu de posar la condició si està ben format o no 
    if ():
        print("L'arxiu ",nomFitxer," està ben format")
    else:
        print("L'arxiu ",nomFitxer," no està ben format")
