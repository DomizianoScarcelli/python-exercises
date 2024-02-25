+++
author = "Domiziano Scarcelli"
title = "2.006 - Ordina stringa per mappatura"
categories = [
    "Difficoltà 2",
]
tags = [
    "stringhe",
    "ordinamento",
    "dizionari"
]
+++

La funzione prende in input una stringa formata dai caratteri ed una mappatura (dizionario) da caratteri ad interi.
Si deve ritornare una copia della stringa ordinata in maniera crescente secondo il valore associato ad ogni carattere.
Nota bene: se il carattere non è presente nella mappatura, allora questo deve essere considerato come 0.

Esempio:

```python
mappatura = {'a': 5, 'b': 2, 'c': 3, 'd': 4}
sorted_strings('abcdefg', mappatura)
# ritorna 'efgbcda'
```

<details>
<summary>Mostra la soluzione</summary>

```python
def sorted_strings(s, mappatura):
    return ''.join(sorted(s, key=lambda x: mappatura[x] if x in mappatura else 0))
```

</details>

