+++
author = "Domiziano Scarcelli"
title = "Lista dei primi n numeri"
categories = [
    "Difficoltà 0",
]
tags = [
    "for-loops",
    "liste"
]
+++

Ritornare lista contenente i primi n numeri
<!--more-->

Scrivere una funzione che prende in input un numero `n`, e ritorna una lista i cui elementi sono i numeri che vanno da `1` ad `n` compresi.

Esempio:

```python
costruisci_lista(6) #Ritorna [1,2,3,4,5,6]
costruisci_lista(10) #Ritorna [1,2,3,4,5,6,7,8,9,10]
```
<details>
<summary>Mostra la soluzione</summary>

```python
def costruisci_lista(n):
	lista = []
	for i in range(n):
		lista.append(i+1)
	return lista

#Soluzione alternativa
def costruisci_lista(n):
	lista = []
	for i in range(1, n+1):
		lista.append(i)
	return lista
```

</details>
