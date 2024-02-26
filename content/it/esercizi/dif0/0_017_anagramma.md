+++
author = "Domiziano Scarcelli"
title = "0.017 - Verifica Anagramma"
categories = [ "Difficoltà 0",]
tags = [ "stringhe",]
date = "2024-02-13T20:45:38+01:00"
+++
Scrivere una funzione che prende in input due stringhe e ritorna True se sono due anagrammi, False altrimenti.

```python
is_anagramma("mario", "rioma") #True
is_anagramma("mario", "paolo") #False
```

<details>
<summary>Mostra la soluzione</summary>

```python
def is_anagramma(parola1, parola2):
	return sorted(parola1) == sorted(parola2)
```

</details>
