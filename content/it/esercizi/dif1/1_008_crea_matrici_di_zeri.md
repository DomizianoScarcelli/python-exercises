+++
author = "Domiziano Scarcelli"
title = "1.008 - Crea matrici di zeri"
categories = [ "Difficoltà 1",]
tags = [ "liste", "matrici",]
date = "2024-02-13T20:39:12+01:00"
+++

Si definisca una funzione che prende in input due valori `base` ed `altezza` e che costruisca una matrice di dimensioni base x altezza, i cui valori sono tutti 0. 

```python
matrice_zeri(5, 3)
#Ritorna la matrice
[[0,0,0,0,0],
[0,0,0,0,0]
[0,0,0,0,0]]
```

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def matrice_zeri(base, altezza):
    lista_finale = []
    for _ in range(altezza):
        riga = []
        for _ in range(base):
            riga.append(0)
        lista_finale.append(riga)
    return lista_finale

#Soluzione alternativa in una sola riga
def matrice_zeri_due(base, altezza):
    return [[0 for _ in range(base)] for _ in range(altezza)]
```

</details>
