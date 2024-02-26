+++
author = "Domiziano Scarcelli"
title = "0.015 - Funzione lambda media"
categories = [ "Difficoltà 0",]
tags = [ "lambda",]
date = "2024-02-13T20:45:38+01:00"
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
