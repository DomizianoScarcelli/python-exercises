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

Si implementi una funzione somma_valori, che somma tutti i valori dei nodi
    all'interno dell'albero, solo se tale valore Ã¨ positivo.

    Esempio:

    L'abero costruito da costruisci_albero_esercizio() Ã¨ il seguente:
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
def sorted_strings(s, mappatura):
    return ''.join(sorted(s, key=lambda x: mappatura[x] if x in mappatura else 0))
```

</details>

