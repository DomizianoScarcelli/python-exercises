+++
author = "Domiziano Scarcelli"
title = "Stampa rettangolo"
categories = [
    "Difficoltà 1",
]
tags = [
    "insiemi",
    "for-loops"
]
+++

Si scriva un codice che riceva come input due interi `base` e `altezza` e disegni (tramite il metodo print) sullo schermo un rettangolo di dimensioni base x altezza usando il carattere `*`.

**Consiglio**: stampare una riga (in senso orizzontale) del rettangolo alla volta. (Ogni volta che si chiama `print`, questo torna automaticamente accapo)

### Esempio di esecuzione

```python
rettangolo(10, 5)
#Stampa a schermo:
#**********
#*        *
#*        *
#*        *
#**********

#Ovviamente senza il carattere "#", utilizzato qua solo per inserire il commento
```

<details>
<summary>Mostra la soluzione</summary>

```python
def stampa_rettangolo(base, altezza):
    for i in range(altezza):
        if i == 0 or i == altezza-1:
            print("*" * base)
        else:
            print("*" + " " * (base - 2) + "*")
    return
```

</details>
