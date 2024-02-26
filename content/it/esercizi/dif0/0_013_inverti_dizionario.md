+++
author = "Domiziano Scarcelli"
title = "0.013 - Inverti dizionario"
categories = [ "Difficoltà 0",]
tags = [ "dizionari",]
date = "2024-02-13T20:45:38+01:00"
+++

Si definisca una funzione che prende in input un dizionario che associa ad ogni stringa un intero, e ritorna il dizionario inverso, ovvero un altro dizionario in cui le chiavi ed i valori sono inverititi (le chiavi diventano i valori e i valori diventano le chiavi).

Si dia per scontato che non esistono due chiavi che hanno associato il medesimo valore. 

```python
diz = {
	"Mario Rossi": 3,
	"Giuseppe Bianchi": 10,
	"Pino Blu": 2
}
inverti_dizionario(diz)
#Ritorna il seguente dizionario
{
	3: "Mario Rossi",
	10: "Giuseppe Bianchi",
	2: "Pino Blu"
}

```
<details>
<summary>Mostra la soluzione</summary>

```python
def inverti_dizionario(diz):
	diz_invertito = {}
	for key, value in diz.items():
		diz_invertito[value] = key
	return diz_invertito
```

Oppure

```python
def inverti_dizionario(diz):
	return {value: key for key, value in diz.items()}
```

</details>
