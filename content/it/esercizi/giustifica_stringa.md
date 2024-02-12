+++
author = "Domiziano Scarcelli"
title = "0.5 - Giustifica stringa"
categories = [
    "Difficoltà 0",
]
tags = [
    "operazioni-aritmetiche",
    "stringhe"
]
+++

Scrivere una funzione che presa in input una stringa, la stampi a schermo in modo che l’ultima lettera di tale stringa cada nella colonna 70 del display.

<details>
<summary>Mostra la soluzione</summary>

```python
def giustif_destra(stringa):
  x = len(stringa)
  print(" " * (70 - x) + stringa)
	return

# Si può anche scrivere
def giustif_destra(stringa):
  print(" " * (70 - len(stringa)) + stringa)
	return
```

</details>
