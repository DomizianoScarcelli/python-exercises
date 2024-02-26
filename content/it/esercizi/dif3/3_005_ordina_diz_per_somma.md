+++
author = "Domiziano Scarcelli"
title = "3.005 - Ordina dizionario per somma"
categories = [ "Difficoltà 3",]
tags = [ "dizionari", "lambda", "ordinamento",]
date = "2024-02-25T21:01:47+01:00"
+++

La funzione prende in input un dizionario le cui chiavi sono interi ed i valori sono liste di dizionari (chiavi: interi, valori: liste di interi). Ritorna gli elementi (items) del dizionario ordinati in maniera crescente secondo tale criterio:

Un elemento è più grande di un altro se la somma del prodotto delle chiavi per il massimo valore delle liste di interi è maggiore.

L'ordine è in maniera decrescente.

Esempio:

```python

dizionario = {1:{4:[1,10,24],2:[4,9,12]},2:{3:[7,8,9],4:[10,11,12]}}
sort_dict(dizionario)

# Ritorna [(1, {4: [1, 10, 24], 2: [4, 9, 12]}), (2, {3: [7, 8, 9], 4: [10, 11, 12]})]
```

 Nota che il primo elemento è più grande del secondo perchè 4*24+2*12 > 3*9+4*12)

<details>
<summary>Mostra la soluzione</summary>

```python
def sort_dict(dizionario):
    return sorted(dizionario.items(), key=lambda x: sum([key * max(value) for key, value in x[1].items()]), reverse=True)
```

</details>

