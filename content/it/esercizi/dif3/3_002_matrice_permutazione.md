+++
author = "Domiziano Scarcelli"
title = "3.002 - Matrice di Permutazione"
categories = [ "Difficoltà 3",]
tags = [ "matrici", "liste", "for-loops",]
date = "2024-02-14T11:09:03+01:00"
+++

Si definisca una funzione che prende in input una lista lunga $n$ uguale alla `lista_permutazione` vista nell’esercizio 3, ovvero i cui elementi sono definiti nel range $[0, n-1]$ e che appaiono una sola volta in tale lista.

La funzione deve ritornare una matrice quadrata $n \times n$ in cui la lista sulla riga $i$ è formata da tutti $0$ tranne per un $1$ nella colonna $j$ dove $j = \text{lista\_permutazione}[i]$.

Wikipedia: [Matrice di permutazione](https://it.wikipedia.org/wiki/Matrice_di_permutazione)

Esempio:

$\text{lista} = [1,3,0,2,4]$

Ritorna la matrice:

$$
\text{matrice} =
\begin{pmatrix}
0 & 1 & 0&  0&  0 \\
0 & 0 & 0&  1&  0 \\
1 & 0 & 0&  0&  0 \\
0 & 0 & 1&  0&  0 \\
0 & 0 & 0&  0&  1 \\
\end{pmatrix} 
$$

Come vedi, nella riga all’indice $0$ è presente l’$1$ nell’indice $1$, perchè $\text{lista}[0] = 1$

<details>
<summary>Mostra la soluzione</summary>

```python
#Solutione: Alessio Lucciola
def permutation_matrix(list):
    final_matrix = []
    list_len = len(list)
    for el in list:
        row = [0]*list_len
        row[el] = 1
        final_matrix.append(row)
    return final_matrix
```

</details>
