+++
author = "Alessio Lucciola"
title = "1.011 - Somma delle righe di una lista di liste"
categories = [
    "Difficoltà 1",
]
tags = [
    "liste-di-liste",
]
+++
Si definisca una funzione che prende in input una lista di liste, e che ritorna una lista in cui l’elemento i-esimo è la somma degli elementi sulla i-esima riga

```python
lista_liste = [[1,2,3,1,3,4],
							[1],
							[2, 3]]
lista_somma_righe(lista_liste) #Ritorna la lista [14,1,5]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def lista_somma_righe(lista_liste):
    somma_finale = []
    for riga in lista_liste:
        somma_finale.append(sum(riga))
    return somma_finale
```

</details>
