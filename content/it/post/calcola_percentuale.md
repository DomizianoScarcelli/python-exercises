+++
author = "Domiziano Scarcelli"
title = "Calcola Percentuale"
date = "2019-03-11"
description = "Calcola la percentuale di un certo numero."
categories = [
    "",
]
tags = [
    "markdown",
    "text",
]
+++

Calcola la percentuale di un certo numero.
<!--more-->

Scrivere una funzione che prende in input due parametri: `numero` e `percentuale`. Percentuale deve essere un numero da 0 a 100 La funzione ritorna la `percentuale` di `numero`.


```python
percentuale(100,54) # Ritorna il 54% di 100 ovvero 53
percentuale(25, 31) # Ritorna 7.75
```
<details>
<summary>Mostra la soluzione</summary>

```python
def calcola_percentuale(numero, percentuale):
    return numero * (percentuale / 100)
```

</details>
