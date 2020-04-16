#Definiu la variable que ens guardarà l'estadística per noms.
fitxer = open("noms.txt",'r')
#Pista clau ha de ser el nom i valor els cops que apareix. 
diccionari={}
for n in fitxer:
  if n in diccionari:
    diccionari[n]=diccionari[n]+1
  else:
    diccionari[n]=1
print(diccionari)
  
#Heu de llegir el fitxer noms.

#Aneu llegint  línia a lína que correspon a un nom.
#Sumeu cap cop que apareix un nom al seu valor.

#Finalment pinteu tots els noms i amb els cops que s'ha posat el darrer any.
#Pintar només la variable. Els diccionaris ja surten ordenats alfabèticament.
#diccionari[clau]=valor

