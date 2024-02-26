+++
author = "Domiziano Scarcelli"
title = "1.024 - Combinazione Stringhe"
categories = [
    "Difficoltà 1",
]
tags = [
    "stringhe",
]
+++

Si scriva una funzione che prende in input tre liste di lunghezza maggiore di 0, con all’interno delle stringhe, e si ritorni una lista di stringhe, ognuna delle quale rappresenta una combinazione dei tre elementi (uno per ogni lista in input). La lista finale deve tornare tutte le possibili combinazioni di questi elementi.

Esempio:

```python
lista_1 = ["Il", "Un", "Nessun"]
lista_2 = ["re", "cavallo", "uomo"]
lista_3 = ["corre", "gioca", "dorme"]

output:
[
	"Il re corre",
	"Il re gioca",
	"Il re dorme",
	"Il cavallo corre", 
	"Il cavallo gioca",
	...
	"Nessun uomo dorme"
]
```

Ricorda che il numero totale di combinazione è il prodotto della lunghezza delle tre liste.

<details>
<summary>Mostra la soluzione</summary>

```python
def combinazione_stringhe(lista1, lista2, lista3):
    result = []
    for elem_1 in lista1:
        for elem_2 in lista2:
            for elem_3 in lista3:
                combinazione = f"{elem_1} {elem_2} {elem_3}"
                result.append(combinazione)
    return result
```

</details>

