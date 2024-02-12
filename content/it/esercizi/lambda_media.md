+++
author = "Domiziano Scarcelli"
title = "0.96 - Funzione lambda media"
categories = [
    "Difficoltà 0",
]
tags = [
    "lambda",
]
+++
Si scriva una funzione lambda che prenda in input una lista e ritorni la media dei valori

```python
#lambda media = ...
media([1,2,3]) #Ritorna 2 ((1+2+3)/3)
```
<details>
<summary>Mostra la soluzione</summary>

```python
media = lambda lista: sum(lista)/len(lista)
```

</details>
