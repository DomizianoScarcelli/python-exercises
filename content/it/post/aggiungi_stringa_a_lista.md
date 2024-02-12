+++
author = "Domiziano Scarcelli"
title = "Aggiungi stringa a lista"
date = "2019-03-11"
description = "Aggiungi stringa a lista."
categories = [
    "",
]
tags = [
    "markdown",
    "text",
]
+++

Aggiungi stringa a lista.
<!--more-->

Scrivere una funzione che prende in input una lista `lista` ed una stringa `stringa` e ritorna la lista con in aggiunta alla fine tale stringa.

Esempio:

```python
aggiungi_stringa([1,5,7], "mario") #Ritorna la lista [1,5,7,"mario"]
aggiungi_stringa([5,4], "paolo") #Ritorna la lista [5,4, "paolo"]
```
<details>
<summary>Mostra la soluzione</summary>

```python
def aggiungi_stringa(lista, stringa):
	lista.append(stringa)
return lista
```

</details>
