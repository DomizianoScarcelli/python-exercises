+++
author = "Domiziano Scarcelli"
title = "0.6 - Somma primi n numeri"
categories = [
    "Difficoltà 0",
]
tags = [
    "for-loops",
    "liste"
]
+++

Calcolare la somma dei primi `n` numeri, dove `n` è l'input della funzione. 

N.B. Non usare la formula $sum(n) = \frac{n(n+1)}{2}$, ma usare un ciclo for per arrivare al risultato.
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
