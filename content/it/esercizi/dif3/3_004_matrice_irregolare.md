+++
author = "Domiziano Scarcelli"
title = "3.004 - Da lista di liste a matrice"
categories = [
    "Difficoltà 3",
]
tags = [
    "stringhe",
    "for-loops"
]
+++

Si definisca una funzione che prende in input una lista di liste, quindi una “matrice irregolare” in cui **non** tutte le righe hanno la stessa lunghezza.

Si vuole ritornare una matrice regolare, di dimensioni $m \times n$ dove $m$ è il numero di righe della matrice irregolare in input, ed $n$ è la lunghezza della riga con lunghezza massima nella matrice irregolare.

Ogni riga che viene “riempita” perchè di lunghezza minore di $n$ deve essere riempita con degli $0$.

**Esempio**

$$
\text{matriceIrregolare} = 
\begin{pmatrix}
1 & 3 & 3 \\
1 & 3\\
1 & 3 & 3 & 9 & 2 \\
1 & 3 & 3 & 12 \\
\end{pmatrix}
$$

Deve ritornare la matrice:

$$
\text{matriceRegolare} = 
\begin{pmatrix}
1 & 3 & 3 & 0 & 0\\
1 & 3& 0 & 0 & 0\\
1 & 3 & 3 & 9 & 2 \\
1 & 3 & 3 & 12 & 0\\
\end{pmatrix}
$$

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def regolarize_matrix(matrix):
    longest_row = max(map(len, matrix))
    for index, row in enumerate(matrix):
        digits_to_add = longest_row - len(row)
        matrix[index].extend([0] * digits_to_add)
    return matrix
```
</details>
