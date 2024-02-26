+++
author = "Domiziano Scarcelli"
title = "2.002 - Da istogramma orizzontale a lista"
categories = [ "Difficoltà 2",]
tags = [ "for-loops", "stringhe", "liste",]
date = "2024-02-13T20:45:38+01:00"
+++

Si definisca una funzione che effettua l’inverso della funzione vista all’esercizio 3, ovvero prende in input una stringha che rappresenta un istogramma verticale, e ritorna la lista che modella tale istogramma.

Nota: i tre apici `"""` servono per poter scrivere una stringa su più righe.

```python
istogramma =
"""
  #  
  ## 
  ## 
 ####
#####
"""

istogramma_a_lista(istogramma) #Ritorna la lista [1,2,5,4,2]

```

<details>
<summary>Mostra la soluzione</summary>

```python
def lista_da_ist_verticale(istogramma):
    """
    Prende in input un'istogramma verticale e ritorna la lista che lo genera
    """
    righe_ist = istogramma.splitlines()
    result = [0 for _ in range(len(righe_ist))]
    for riga in righe_ist:
        for indice, elem in enumerate(riga):
            if elem == "#":
                result[indice] += 1
    return result
```

</details>

