+++
author = "Domiziano Scarcelli"
title = "1.010 - Media elementi lista di liste"
categories = [
    "Difficoltà 1",
]
tags = [
    "for-loops",
    "liste-di-liste"
]

+++
Si definisca una funzione che prende in input una lista di liste (non necessariamente una matrice) che contiene interi, e che ritorni la media del valore degli elementi all’interno.

```python
lista_liste = [[1,2,3,1,3,4],
							[1],
							[2, 3]]
media_lista_liste(lista_liste) #Ritorna 2.222 (20/9)
```

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def media_lista_liste(lista_liste):
    somma_valori = 0
    numero_elementi = 0
    for lista in lista_liste:
        numero_elementi += len(lista)
        somma_valori += sum(lista)
    return somma_valori/numero_elementi
```
</details>
