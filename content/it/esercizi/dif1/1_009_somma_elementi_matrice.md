+++
author = "Domiziano Scarcelli"
title = "1.009 - Somma elementi matrice"
categories = [ "Difficoltà 1",]
tags = [ "liste", "matrici", "for-loops",]
date = "2024-02-13T20:39:12+01:00"
+++

Si definisca una funzione che prende in input una matrice `matrice` e che ritorna la somma di tutti gli elementi all’interno di `matrice`.

```python
matrice = [[1,2,3],
			[1,0,0],
			[2,5,3]]
somma_lista_liste(matrice) #Ritorna 17
```

<details>
<summary>Mostra la soluzione</summary>

```python
def somma_matrice(matrice):
	count = 0
	for riga in matrice:
		for elem in riga:
			count += elem
	return count
```

</details>
