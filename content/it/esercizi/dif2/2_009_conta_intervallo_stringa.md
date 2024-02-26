+++
author = "Domiziano Scarcelli"
title = "2.009 - Conta intervallo stringa"
categories = [ "Difficoltà 2",]
tags = [ "stringhe",]
date = "2024-02-26"
+++

Si definisca una funzione che prende in input una stringa di caratteri, due
interi i e j e una sottostringa substr.

La funzione deve ritornare il numero di volte che substr è contenuto nella stringa di caratteri tra i e j (inclusi), meno il numero di volte che substr
è contenuto nelle altre posizioni (non nel range i -> j).

Esempio:

    stringa = "ciao mario ciao alberto ciao marco come stai ciao"
                            ^                 ^
                            i                 j
    i = 10
    j = 30
    substr = "ciao"

La funzione ritorna 0 perchè "mar" è contenuto 2 volte tra i e j, e 2 volte fuori da i e j. 

<details>
<summary>Mostra la soluzione</summary>

```python
def conta_intervallo_stringa(stringa, i, j, substr):
    str_range = stringa[i:j]
    count = str_range.count(substr)
    str_out_range = stringa[:i] + stringa[j:]
    count -= str_out_range.count(substr)
    return count
```

</details>

