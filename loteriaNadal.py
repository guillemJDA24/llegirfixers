import random
liniesPremiades = []

for n in range(0,5):
    linia = random.randint(0,10001)
    liniesPremiades.append(linia)

#Heu de llegir el fitxer numerosPremiats

# Mostrar número a número 
# I dir si és 1er premi, 2on premi, 3er premi o "Tornen diners".
# 1er premi si el número de línia esà en la primera posició de la llista liniesPremiades
# 2on premi si el número de línia està  en la segona o tercera posició de la llista liniesPremiades
# 3er premi si el número de línia està  en la quarta o cinquena posició de la llista liniesPremiades
# Tornen diners si el número de línia no està en la llista.

