+++
author = "Domiziano Scarcelli"
title = "2.010 - Ordina matrice dizionario"
categories = [ "Difficoltà 2",]
tags = [ "stringhe",]
date = "2024-02-26T13:46:33+01:00"
+++
Dato in input una matrice rappresentata come una lista di liste di interi
(matrice), ed un dizionario (diz) le cui chiavi e valori sono interi, si ritorni
una copia della lista ordinata secondo il seguente criterio:

- La riga il cui primo elemento è n è più grande della riga il cui primo
elemento è m se il valore associato alla chiave n nel dizionario è più
grande  del valore associato alla chiave m.
- In caso i valori siano uguali, le due righe vengono comparate a seconda della media degli elementi che hanno all'interno.
- Se anche la media è uguale, allora le due righe vengono ordinate a seconda dell'elemento che è nell'ultima posizione.

Nota: dai per scontato che la chiave n e la chiave m esistono sempre nel dizionario.

Esempio:
    matrice = [
        [12, 7, 20, 3, 15, 8],
        [1, 9, 11, 18, 0, 10],
        [6, 14, 2, 19, 13, 4],
        [16, 5, 17, 15, 8, 7],
        [11, 20, 4, 9, 2, 15]
    ]

    diz = {12: 10, 7: 5, 20: 7, 3: 3, 15: 8, 8: 3, 1: 1, 9: 5, 11: 9, 18: 4, 0:
    10, 10: 7, 6: 6, 14: 0, 2: 9, 19: 2, 13: 8, 4: 5, 16: 5, 5: 3, 17: 3}


La matrice ordinata è 

    [[1, 9, 11, 18, 0, 10],
    [16, 5, 17, 15, 8, 7],
    [6, 14, 2, 19, 13, 4],
    [11, 20, 4, 9, 2, 15],
    [12, 7, 20, 3, 15, 8]] 

<details>
<summary>Mostra la soluzione</summary>

```python
def ordina_matrice_diz(matrice, diz):
    return sorted(matrice, key=lambda x: (diz[x[0]], -sum(x), x[-1]))
```

</details>

