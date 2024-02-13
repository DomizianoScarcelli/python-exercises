+++
author = "Domiziano Scarcelli"
title = "0.009 - Verifica dimensione insieme"
categories = [
    "Difficoltà 0",
]
tags = [
    "insiemi"
]
+++

Scrivere una funzione che prenda in input un insieme `ins` ed un numero `num` e che ritorni `True` se la dimensione dell’insieme `ins` è maggiore o uguale al numero `num`, e che ritorni `False` altrimenti.

### Esempio esecuzione

```python
verifica_dimensione({1,5,9,4,6}, 4) #Ritorna True
verifica_dimensione({1,6}, 3) #Ritorna False
```

```
def verifica_dimensione(ins, num):
    return len(ins) >= num
```
<details>
<summary>Mostra la soluzione</summary>

```python
# Mantiene l’ordine delle lettere nella lista
def verifica_dimensione(ins, num):
    return len(ins) >= num
```

</details>
