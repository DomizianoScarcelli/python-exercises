+++
author = "Domiziano Scarcelli"
title = "1.006 - Chiave con valore di lunghezza maggiore"
categories = [
    "Difficoltà 1",
]
tags = [
    "liste",
    "dizionari"
]
+++

Si definisca una funzione che prende in input un dizionario `diz` che associa ad ogni intero un insieme, e ritorna la chiave che ha l’insieme di lunghezza maggiore. Si assuma che esista una sola chiave con valore di lunghezza maggiore rispetto alle altre chiavi.

```python
diz = {
	1: {1,2,3,4},
	10: {3,4},
	19: {},
	3: {1,2,3,4,5,6,7,8,9},
	4: {4,55,6,43}
}
chiave_valore_maggiore(diz) #Ritorna 3, visto che è la chiave con il valore con lunghezza maggiore
```
<details>
<summary>Mostra la soluzione</summary>

```python
def chiave_valore_maggiore(diz):
	max = 0
	chosen_key = None
	for key, value in diz.items():
		if len(value) > max:
			max = len(value)
			chosen_key = key
	return chosen_key
```

</details>
