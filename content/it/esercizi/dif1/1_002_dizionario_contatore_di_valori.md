+++
author = "Domiziano Scarcelli"
title = "1.002 - Dizionario contatore di valori"
categories = [ "Difficoltà 1",]
tags = [ "dizionari", "stringhe",]
date = "2024-02-13"
+++
Si definisca una funzione che prende in input un dizionario `diz` che associa un intero ad un altro intero (sia le chiavi che i valori sono tutti interi) e ritorna un altro dizionario in cui le chiavi sono i valori presenti in `diz` ed il valore associato è le volte che tale valore appare in `diz`.

```python
diz = {
	1: 0,
	2: 1,
	3: 0,
	4: 26,
	34: 18,
	21: 26
}
diz_conta_valori(diz)
# Ritorna il seguente dizionario
{
	0: 2, #Il valore 0 è presente 2 volte come valore all'interno di diz
	1: 1,
	26: 2,
	18: 1
}
```

<details>
<summary>Mostra la soluzione</summary>

```python
def diz_conta_valori(diz):
	cont = {}
	for value in diz.values():
		if value not in cont:
			cont[value] = 1
		else:
			cont[value] += 1
	return cont
```

</details>
