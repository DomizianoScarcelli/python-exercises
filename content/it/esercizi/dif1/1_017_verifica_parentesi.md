+++
author = "Domiziano Scarcelli"
title = "1.017 - Verifica Parentesi"
categories = [ "Difficoltà 1",]
tags = [ "stringhe", "liste",]
date = "2024-02-13"
+++
Scrivere una funzione che prende in input una lista formata da parentesi aperte e chiuse, e ritorna True solo se le parentesi sono inserite in maniera corretta, False altrimenti.

In maniera corretta significa che ogni parentesi aperta deve essere chiusa correttamente. Non può esistere una parentesi aperta che non viene chiusa, e non può esistere una parentesi che viene chiusa senza essere aperta.

```python
esempio_1 = "(())()((())())"
esempio_2 = ")(())()((())())"
esempio_3 = "(())()((())()))"

parentesi_corrette(esempio_1) #True
parentesi_corrette(esempio_2) #False
parentesi_corrette(esempio_3) #False
```

<details>
<summary>Mostra la soluzione</summary>

```python
def verifica_parentesi(parentesi):
    contatore = 0
    for carattere in parentesi:
        if carattere == "(":
            contatore += 1
        if carattere == ")":
            contatore -= 1
        if contatore == -1:
            return False
		return contatore == 0
```


</details>
