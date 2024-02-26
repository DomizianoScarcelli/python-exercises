+++
author = "Domiziano Scarcelli"
title = "3.001 - Istogramma Verticale"
categories = [ "Difficoltà 3",]
tags = [ "for-loops", "stringhe",]
date = "2024-02-13"
+++

Si definisca una funzione che fa lo stesso lavoro della funzione precedente, però ritorna l’istogramma verticale, nel senso che le barre si sviluppano in vericale e non in orizzontale.

```python
lista = [1,2,5,4,2]
print(istogramma_verticale(lista))
#Stampa il seguente valore:

  #  
  ## 
  ## 
 ####
#####
```

<details>
<summary>Mostra la soluzione</summary>

```python
def istogramma_verticale(lista):
    """Data una lista di interi, stampare la lista rappresentata da istogramma verticale."""
    max_elemento = max(lista)
    risultato = ""
    for step in range(max_elemento):
        altezza = max_elemento - step
        riga = ""
        for elemento in lista:
            if elemento >= altezza:
                riga += "#"
            else:
                riga += " "
        risultato += riga + "\n"
    return risultato
```

</details>
