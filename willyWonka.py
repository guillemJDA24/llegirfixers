import random

golden = False
for i in range(1,11):
    fitxer = open("xocolataFabrica/xocolata"+str(i)+".txt","w+")
    goldenTicket = random.randint(0,10)
    if (goldenTicket == 2 and not golden):
        fitxer.write("Golden ticket")
        golden = True
    else:
        fitxer.write("Ummm xocolata")
    fitxer.close()

if (not golden):
    fitxer = open("xocolataFabrica/xocolata"+str(random.randint(1,11))+".txt","w")
    fitxer.write("Golden ticket")
    fitxer.close()

print("Benvinguts a la fàbrica de xocolata de Willy Wonca")
print("Podràs visitar la  nostra meravellosa fàbrica.")
print("Si a l'obrir una tauleta de xocolata et surt el Golden Ticket")
print("Només hi ha un paquet amb el Golden ticket entre els 10")

paquet = input("Quin paquet vols dels deu possibles? Entra un número entre 1 i 10")

while (not(paquet.isnumeric()) or int(paquet) < 1 or int(paquet) > 10):
    paquet = input("Quin paquet vols dels deu possibles? Entra un número entre 1 i 10")

# Heu de llegir el fitxer que han triat i mostrar-li el contingut del fitxer
fitxer = open("xocolataFabrica/xocolata"+str(paquet)+".txt","r")
print(fitxer.read())
