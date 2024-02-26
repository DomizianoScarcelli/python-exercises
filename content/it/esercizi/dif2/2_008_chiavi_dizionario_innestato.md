+++
author = "Domiziano Scarcelli"
title = "2.008 - Chiavi dizionario innestato"
categories = [
    "Difficoltà 2",
]
tags = [
    "dizionari",
    "ricorsione",
]
+++

[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/2_008_chiavi_dizionario_innestato.zip)

Si implementi la funzione chiavi_dizionario(dizionario) che ritorna l'insieme
delle chiavi del dizionario.

Per il dizionario dato in input, la funzione deve ritornare l'insieme:

    {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'}

Consiglio: per capire se un elemento è un intero, si può usare la funzione
isinstance(elemento, int) che ritorna True se elemento è un intero, False
altrimenti.

Allo stesso modo, per capire se un elemento è un dizionario, si può usare la
funzione isinstance(elemento, dict) che ritorna True se elemento è un dizionario,
False altrimenti.

<details>
<summary>Mostra la soluzione</summary>

```python
def chiavi_dizionari(dizionario, chiavi=set()):
    for chiave in dizionario:
        chiavi.add(chiave)
        if isinstance(dizionario[chiave], dict):
            chiavi_dizionari(dizionario[chiave], chiavi)
    return chiavi
```

</details>

