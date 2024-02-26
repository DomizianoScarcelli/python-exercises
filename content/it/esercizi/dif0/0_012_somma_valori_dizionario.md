+++
author = "Domiziano Scarcelli"
title = "0.012 - Somma valori di un dizionario"
categories = [ "Difficoltà 0",]
tags = [ "liste", "stringhe",]
date = "2024-02-13T20:45:38+01:00"
+++

Si definisca una funzione che prende in input un dizionario `diz` che associa ad ogni stringa un intero, e ritorna la somma totale dei valori presenti all’interno del dizionario.

```python
diz = {
	"Mario Rossi": 3,
	"Giuseppe Bianchi": 10,
	"Pino Blu": 2
}
somma_diz(diz) #Ritorna il valore 15
```
<details>
<summary>Mostra la soluzione</summary>

```python
def somma_diz(diz):
    return sum(diz.values())
```
</details>
