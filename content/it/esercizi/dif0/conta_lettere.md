+++
author = "Domiziano Scarcelli"
title = "0.8 - Conta lettere in stringa"
categories = [
    "Difficoltà 0",
]
tags = [
    "liste",
    "stringhe"
]
+++

Scrivere una funzione che, presa in input una stringa `stringa` (di sole lettere minuscole) ed una lettera `let`, ritorni il numero di volte che `let` appare dentro la `stringa`.

> È la stessa cosa che fa il metodo `stringa.count(lettera)`, però non utilizzarlo per arrivare alla soluzione.

### Esempio esecuzione

```python
conta_lettere("mamma", "m") #Ritorna 3
conta_lettere("pierpaolo", "p") #Ritorna 2
```
<details>
<summary>Mostra la soluzione</summary>

```python
# Mantiene l’ordine delle lettere nella lista
def conta_lettere(stringa, let):
    contatore = 0
    for lettera in stringa:
        if lettera == let:
            contatore += 1
    return contatore
```
Oppure, usando una list comprehension
```python
def conta_lettere(stringa, let):
		contatore = sum(1 for letterea in stringa if lettera == let)
    return contatore
```

</details>
