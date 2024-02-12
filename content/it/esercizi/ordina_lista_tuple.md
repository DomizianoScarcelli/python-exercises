+++
author = "Domiziano Scarcelli"
title = "1.96 - Ordina lista di tuple"
categories = [
    "Difficoltà 1",
]
tags = [
    "lambda",
    "ordinamento"
]

+++
Si scriva una funzione lambda da usare come chiave di ordinamento per ordinare una lista di tuple rispetto al secondo valore.

Nota: in questo caso la tua funzione lambda prende come input `elemento`, dove `elemento` è una tupla.

```python
lista_tuple = [(1,2), (5,1), (7,3), (1,1)]
lista_tuple.sort(key=#La tua funzione lambda)
print(lista_tuple) #[(1,1), (5,1), (1,2), (7,3)]
```

<details>
<summary>Mostra la soluzione</summary>

```python
lista_tuple.sort(key=lambda tupla: tupla[1]) #Ordina in base al secondo valore
```
</details>
