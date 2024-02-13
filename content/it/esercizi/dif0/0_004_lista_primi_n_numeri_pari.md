+++
author = "Domiziano Scarcelli"
title = "0.004 - Lista dei primi n numeri pari"
categories = [
    "Difficoltà 0",
]
tags = [
    "for-loops",
    "liste"
]
+++

Scrivere una funzione che prende in input un numero `n`, e ritorna una lista i cui elementi **pari** sono i numeri che vanno da `1` ad `n` compresi.

Esempio:

```python
costruisci_lista(6) #Ritorna [2,4,6]
costruisci_lista(10) #Ritorna [2,4,6,8,10]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def costruisci_lista(n):
	lista = []
	for i in range(n):
		if (i+1) % 2 == 0:
			lista.append(i+1)
	return lista

#Soluzione alternativa
def costruisci_lista(n):
	lista = []
	for i in range(1, n+1):
		if i % 2 == 0:
			lista.append(i)
	return lista
```

</details>
