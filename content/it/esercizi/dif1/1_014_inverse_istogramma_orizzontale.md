+++
author = "Domiziano Scarcelli"
title = "1.014 - Da istogramma orizzontale a lista"
categories = [
    "Difficoltà 1",
]
tags = [
    "for-loops",
    "stringhe",
    "liste"
]
+++

Si definisca una funzione che effettua l’inverso della funzione vista all’esercizio 2, ovvero prende in input una stringa che rappresenta un istogramma orizzontale, e ritorna la lista che modella tale istogramma.

Nota: i tre apici `"""` servono per poter scrivere una stringa su più righe.

```python
istogramma =
"""
#
##
#####
####
##
"""

istogramma_a_lista(istogramma) #Ritorna la lista [1,2,5,4,2]

```

<details>
<summary>Mostra la soluzione</summary>

```python
def lista_da_ist_orizzontale(istogramma):
    """
    Prende in input un'istogramma orizzontale e ritorna la lista che lo genera
    """
    lista_finale = []
    righe_ist = istogramma.split("\n")
    for riga in righe_ist:
        if len(riga) != 0:
            lista_finale.append(len(riga))
    return lista_finale
```

</details>

