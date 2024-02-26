+++
author = "Domiziano Scarcelli"
title = "1.026 - Ordina insiemi per intersezione"
categories = [
    "Difficoltà 1",
]
tags = [
    "ordinamento",
    "lambda",
    "insiemi"
]
+++

La funzione prende in input una lista di insiemi ed un insieme. Ritorna la lista di insiemi ordinata in maniera crescente secondo il numero di elementi in comune con l'insieme in input.
Nota bene: non devi modificare la lista di insiemi in input, ma devi tornare una nuova lista ordinata.

Esempio:

```python
other_set = {4,2,6}
set_list = [{1,2,3,4},{1,3,4,5},{4,5,6,7}]
sort_by_intersection(other_set, set_list)

#Ritorna [{1, 3, 4, 5}, {1, 2, 3, 4}, {4, 5, 6, 7}]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def sort_by_intersection(other_set, set_list):
    return sorted(set_list, key=lambda x: len(x.intersection(other_set)))
```

</details>

