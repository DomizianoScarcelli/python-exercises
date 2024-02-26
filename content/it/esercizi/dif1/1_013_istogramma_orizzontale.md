+++
author = "Domiziano Scarcelli"
title = "1.013 - Istogramma Orizzontale"
categories = [ "Difficoltà 1",]
tags = [ "for-loops", "stringhe",]
date = "2024-02-13"
+++

Si definisca una funzione che, presa una lista di interi positivi, ritorni una stringa che rappresenta un istogramma orizzontale in cui sulla riga i-esima ci sono tanti caratteri “#” quanto il valore dell’i-esimo elemento nella lista.

```python
lista = [1,2,5,4,2]
print(istogramma_orizzontale(lista))
#Stampa il seguente valore:

#
##
#####
####
##
```

<details>
<summary>Mostra la soluzione</summary>

```python
def istogramma_orizzontale(lista):
    risultato = ""
    for elemento in lista:
        risultato += "#" * elemento + "\n"
    return risultato
```

</details>

