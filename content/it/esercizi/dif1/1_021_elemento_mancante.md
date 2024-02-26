+++
author = "Domiziano Scarcelli"
title = "1.021 - Elemento Mancante"
categories = [ "Difficoltà 1",]
tags = [ "for-loops", "liste",]
date = "2024-02-25T21:01:47+01:00"
+++

Si scriva una funzione che presa una lista di $n$ elementi in successione, con uno o più numeri mancanti all’interno, ritorni una lista contenente i valori dei numeri mancanti, ordinati in maniera crescente.

Esempio:

```python
lista_1 = [1,2,3,4,6,7,8,9,10]
elemento_mancante(lista_1) #ritorna [5]

lista_2 = [6,8,10,11,13,14,15]
elemento_mancante(lista_2) #ritorna [7,9,12]

lista_3 = [10,11,12,13,14]
elemento_mancante(lista_3) #ritorna []
```

Nota: la successione non parte necessariamente da 1. 

<details>
<summary>Mostra la soluzione</summary>

```python
def elemento_mancante(lista):
    start = lista[0]
    end = lista[-1]
    lista_completa = list(range(start, end+1))
    mancanti = [x for x in lista_completa if x not in lista] 
    return sorted(mancanti)
```

</details>

