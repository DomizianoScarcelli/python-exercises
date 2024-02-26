+++
author = "Domiziano Scarcelli"
title = "2.006 - Ordina stringa per mappatura"
categories = [ "Difficoltà 2",]
tags = [ "stringhe", "ordinamento", "dizionari",]
date = "2024-02-25T21:01:47+01:00"
+++
[Scarica QUI i file necessari per risolvere l'esercizio.](/assets/exercises_py/it/2_007_somma_nodi_negativi.py)

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
def somma_nodi(tree, somma=0):
    if tree.valore > 0:
        somma += tree.valore
    for child in tree.children:
        somma += somma_nodi(child)
    return somma
```

</details>

