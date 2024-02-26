+++
author = "Domiziano Scarcelli"
title = "1.027 - Ordina dizionario per somma di chiavi"
categories = [ "Difficoltà 1",]
tags = [ "dizionario", "ordinamento", "lambda",]
date = "2024-02-26T14:03:09+01:00"
+++
Si costruisca una funzione che, dato un dizionario le cui chiavi sono interi
e i valori altri dizionari (chiavi interi, valori interi), ritorna la lista
formata dalle chiavi del dizionario ordinate in maniera decrescente secondo
la somma dei valori delle chiavi dei dizionari interni. Se questa somma è
uguale, si prenda la chiave più grande.

Esempio:

    dizionario = {1: {1: 1, 2: 1, 3: 0},
                  2: {1: 2, 2: 1, 3: 2},
                  3: {1: 3, 2: 0, 3: 0},
                  4: {1: 4, 2: 1, 3: 10},
                  5: {1: 1, 2: 1, 3: 1},
                  6: {1: 6, 2: 7, 3: 8}

La funzione ritorna [6, 4, 2, 5,3, 1]

Il valore 6, il cui dizionario associato è {1: 6, 2: 7, 3: 8} ha somma 21,
mentre la chiave 4, il cui dizionario associato è {1: 4, 2: 1, 3: 10} ha somma 15, 
quindi la chiave 6 viene prima di 4
<details>
<summary>Mostra la soluzione</summary>

```python
def ordina_matrice_diz(matrice, diz):
    return sorted(matrice, key=lambda x: (diz[x[0]], -sum(x), x[-1]))
```

</details>

