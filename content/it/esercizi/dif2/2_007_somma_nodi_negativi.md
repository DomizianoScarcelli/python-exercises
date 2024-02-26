+++
author = "Domiziano Scarcelli"
title = "2.007 - Somma nodi negativi"
categories = [
    "Difficoltà 2",
]
tags = [
    "alberi",
    "ricorsione",
]
+++

[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/2_007_somma_nodi_negativi.zip)

Si implementi una funzione somma_valori, che somma tutti i valori dei nodi
all'interno dell'albero, solo se tale valore è positivo.

Esempio:

L'abero costruito da costruisci_albero_esercizio() è il seguente:

              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |   |  |  |  |         
          4   2 -1 -4  7        
            __|__              
           |     |            
           3     1           

La funzione deve restituire: 5 + 2 + 11 + 4 + 2 + 7 + 3 + 1 = 35

<details>
<summary>Mostra la soluzione</summary>

```python
def somma_nodi(tree, somma=0):
    if tree.valore > 0:
        somma += tree.valore
    for child in tree.children:
        somma += somma_nodi(child)
    return somma
```

</details>

