+++
author = "Domiziano Scarcelli"
title = "0.003 - Aggiungi stringa a lista"
categories = [ "Difficoltà 0",]
tags = [ "liste", "stringhe",]
date = "2024-02-13T20:45:38+01:00"
+++

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
