+++
author = "Domiziano Scarcelli"
title = "1_022 - Ridimensiona Matrice"
categories = [ "Difficoltà 1",]
tags = [ "matrici",]
date = "2024-02-26T11:16:25+01:00"
+++

Si scriva una funzione che prende in input una matrice $n \times m$ ($n$ righe, $m$ colonne) e che ritorni una lista lunga $n \cdot m$ in cui tutte le righe della matrice sono state concatenate per formare una sola lista.

$$
\text{matrice} =
\begin{pmatrix}
1 & 2 & 3&  4&  5 \\
6 & 7 & 8&  9&  10 \\
11 & 12 & 13&  14&  15 \\
\end{pmatrix} \quad n = 3, m = 5
$$

```python
matrice = [[1,2,3,4,5],
					[6,7,8,9,10],
					[11,12,13,14,15]]

ridimensiona(matrice)
#Ritorna la lista: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def ridimensiona_matrice(matrice):
    result = []
    for riga in matrice:
        for elemento in riga:
            result.append(elemento)
    return result

#Soluzione più compatta
def ridimensiona_matrice_v2(matrice):
    return [elemento for riga in matrice for elemento in riga]
```

</details>

