+++
author = "Domiziano Scarcelli"
title = "0.011 - Pulisci dizionario"
categories = [
    "Difficoltà 0",
]
tags = [
    "dizionari",
]
+++
Si scriva una funzione che prende in input un dizionario `diz` che associa ad ogni intero una lista e modifica il dizionario in-place (sul posto, ovvero senza ritornare nulla, ma il dizionario in input deve essere modificato) in cui le chiavi a cui è associata una lista vuota vengono eliminate.

```python
diz = {
	1: [],
	2: [1,2,3],
	3: [3],
	4: [],
	5: [5,6,7]
}

pulisci_dizionario(diz) #Ritorna None
print(diz)
#Il dizionario diz ora è modificato, ed è
{
	2: [1,2,3],
	3: [3],
	5: [5,6,7]
}
```

<details>
<summary>Mostra la soluzione</summary>

```python
def pulisci_dizionario(diz):
	for key in diz.copy():
		if diz[key] == []:
			diz.pop(key)
	return
```

</details>
