+++
author = "Domiziano Scarcelli"
title = "0.016 - Funzione per stampare dizionario"
categories = [ "Difficoltà 0",]
tags = [ "dizionari",]
date = "2024-02-13T20:45:38+01:00"
+++
Si definisca una funzione che preso in input un dizionario qualsiasi (ricorda che le chiavi possono essere solo stringhe o interi per ora) e stampa riga per riga la chiave ed il valore associato a tale chiave all’interno del dizionario con la seguente forma `Chiave: chiaveDizionario, Valore: valoreAssociatoAllaChiave`. La funzione non ritorna nessun valore.

```python
diz = {
	"mario": "rossi",
	4: [2,3,4,5],
	"insieme": {1,2,3},
	2: "cani"
}
stampa_dizionario(diz)
#Stampa le seguenti righe

#Chiave: mario, Valore rossi
#Chiave: 4, Valore [2,3,4,5]
#Chiave: insieme, Valore {1,2,3}
#Chiave: 2, Valore: cani

```
<details>
<summary>Mostra la soluzione</summary>

```python
def stampa_dizionario(diz):
    for k, v in diz.items():
        print(f"Chiave: {k}, Valore {v}")
```

</details>
