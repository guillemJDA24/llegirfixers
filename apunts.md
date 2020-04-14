# Treballant en fitxers

## Introducció

Ja portem dos trimestres programant, aprenent algorismes i instruccions. I sobretot executant i provant programes un rera l'altre. I:

- S'han d'introduir 25 números. El programa no em xuta i quin pal posaar i posar els 25 números.
- Hem acabat d'introduir les dades dels pokemons o les receptes, s'acaba la classe. A l'endemà... torna a introduir les dades.

Les dades fins ara han estat volàtils, les guardavem en variables (diversos tipus de dades de més simples a complexes) i aquestes estaven a la memòria RAM. Per tant a l'acaba execució es perdien.

Primera solució, perquè tinguem persistència de dades
les guardem al disc dur. **I el disc dur guarda les dades en fitxers i capretes (directoris)**

En aquest tema aprendrem com des de programació treballar amb el sistema d'arxius d'un ordinador.

Aprendrem:

- Llegir fitxers
- Crear fitxers
- Escriure fitxers
- Llegir les característiques d'un arxiu (mida, nom, darrera modificació...)
- Crear, eliminar i moure carpetes

Inicialment serà amb arxius de text. Aquells que es poden treballar des d'un editor de text simple (edit, notepad, sublime, thonny ...etc) que guarden caràcters però després treballarem amb arxius binaris com: imatges o audios.

## Llegint d'un fitxer

A l'hora de llegir un fitxer haurem de fer dues coses:

- el nom del fitxer indicant la ruta a com accedir.
- el nombre de caràcters a llegir

Els exemples de a continuació ho farem amb l'arxiu informacio.txt que conté:

```bash=
Jaume Molins Pi
Pepa Marquesa Vilanova
Jorge Martínez López
Marta Mireu Vila
Fernanda Pal Pila
Aitor Tilla Patatas
Laura Nio Caro
``` 
### Definint variable fitxer

Per poder llegir d'un fitxer des del Python usem la funció open. Aquesta rep dos paràmetres:
- el nom (ruta per accedir a l'arxiu)
- el mode
  - que és **r** ja que només volem llegir per ara.

```python3=
fitxer = open("informacio.txt",r)
```

En aquest cas la varibale fitxer ens permet treballar l'arxiu de nom informacio.txt que està guardat en la mateixa carpeta (directori) que el nostre programa en Python. La **r** ens restringeix només a lectura.

### Llegir tot el fitxer

```python3=
fitxer = open("informacio.txt",r)
contingut = fitxer.read()
```

La funció read del fitxer ens permet llegir el seu interior i ens ho retorna en un String.

### Llegir nombre de caràcters concrets

```python3=
fitxer = open("informacio.txt",r)
contingut = fitxer.read(10)
print(contingut)
```

La funció read del fitxer ens permet llegir el seu interior i en aquest cas ens retorna en un String els primers 10 caràcters. L'execució mostra:

```bash=
Jaume Moli
```

### Llegir una línia

```python3=
fitxer = open("informacio.txt",r)
contingut = fitxer.readline()
```

L'execució ens mostra:
```bash=
Jaume Molins Pi
```

La funció readline ens retorna una línia del fitxer. La línia on estigui la variable en aquell moment. Per tant ara si tornessim a executar la instrucció fitxer.readline() ens llegiria la segona. Sortiria:

```bash=
Pepa Marquesa Vilanova
```


### Llegir línia a línia

```python3
fitxer = open("informacio.txt",r)
for linia in fitxer:
    print(linia)
```

Aquí es fa de la mateixa manera que quan llegim element a element d'una llista.

Vegeu en aquest video una execució de les diferents maneres de llegir un arxiu des de Python.

[![asciicast](https://asciinema.org/a/Pmsi3ASwFW6lmNnZmBAtiYCqn.svg)](https://asciinema.org/a/Pmsi3ASwFW6lmNnZmBAtiYCqn)

Visiteu el video a [https://asciinema.org/a/Pmsi3ASwFW6lmNnZmBAtiYCqn](https://asciinema.org/a/Pmsi3ASwFW6lmNnZmBAtiYCqn)
