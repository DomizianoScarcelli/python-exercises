+++
author = "Domiziano Scarcelli"
title = "1.019 - Stringa sarcastica"
categories = [ "Difficoltà 1",]
tags = [ "stringhe",]
date = "2024-02-14T11:09:03+01:00"
+++

Si definisca una funzione che prende in input una stringa e ritorna la sua versione scritta in maniera “sarcastica”, ovvero in cui le lettere sono scritte una in minuscolo ed una in maiuscolo, partendo da quella minuscola.

Nota: Attento agli spazi, che non dovrebbero influenzare l’andamento minuscolo → MAIUSCOLO → minuscolo → MAIUSCOLO

```python
stringa_sarcastica("ciaoo") #Ritorna cIaOo
stringa_sarcastica("come sei bravo") #Ritorna "cOmE sEi BrAvO" (Gli spazi non vengono contati)
```

<details>
<summary>Mostra la soluzione</summary>

```python
def stringa_sarcastica(stringa):
    risultato = ""
    contatore = 0
    for lettera in stringa:
        if contatore % 2 == 0:
            risultato += lettera.lower()
        else:
            risultato += lettera.upper()
        if lettera != " ":
            contatore += 1
    return risultato
```
</details>
