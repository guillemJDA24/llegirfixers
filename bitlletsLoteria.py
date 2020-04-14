import random
fitxer = open("numerospremiats.txt","w")
for numero in range(0,10000):
    premiat = random.randint(10000,100000)
    fitxer.write(str(premiat)+"\n")
fitxer.close()
