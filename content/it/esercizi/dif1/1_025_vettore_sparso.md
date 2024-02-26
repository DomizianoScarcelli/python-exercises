+++
author = "Domiziano Scarcelli"
title = "1.025 - Vettore Sparso"
categories = [ "Difficoltà 1",]
tags = [ "dizionari", "stringhe",]
date = "2024-02-25T21:01:47+01:00"
+++

Si scriva una funzione che, data una lista di numeri, ritorni un dizionario le cui chiavi sono gli indici degli elementi diversi da 0, e i cui valori sono gli elementi a tali indici.

Esempio:

```python
vettore = [0,0,0,1,0,0,2,0,0,0,0,5,0,0,0,3]

to_sparse(vettore) 
#output: {3: 1, 6: 2, 11: 5, 15: 3}
```

<details>
<summary>Mostra la soluzione</summary>

```python
def to_sparse(vettore):
    dizionario = {}
    for index, elem in enumerate(vettore):
        if elem != 0:
            dizionario[index] = elem
    return dizionario

def to_sparse_v2(vettore):
    return {index: elem for (index, elem) in enumerate(vettore) if elem != 0}
```

</details>

