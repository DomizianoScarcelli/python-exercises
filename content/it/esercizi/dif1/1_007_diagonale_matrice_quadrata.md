+++
author = "Domiziano Scarcelli"
title = "1.007 - Calcola diagonale matrice quadrata"
categories = [
    "Difficoltà 1",
]
tags = [
    "liste",
    "matrici",
]
+++

Si definisca una funzione che prende in input una **matrice quadrata** (lista di liste tutte della stessa dimensione e dove base = altezza) e che torni la somma della diagonale principale.

Ricorda che un elemento con coordinate $(x,y)$ è sulla diagonale principale se $x = y$.

```python
matrice = [[1,2,3], 
			[4,5,6], 
			[7,8,9]] 
#Questa scrittura è solo per rendere la matrice più leggibile
somma_diagonale(matrice) #ritorna 1+5+9 = 15
```

<details>
<summary>Mostra la soluzione</summary>

```python
def calc_diagonale(matrice):
    count = 0
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            if x == y:
                count += matrice[y][x]
    return count
```

</details>
