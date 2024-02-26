+++
author = "Domiziano Scarcelli"
title = "1_023 - Numeri Divisibili"
categories = [ "Difficoltà 1",]
tags = [ "for-loops",]
date = "2024-02-25T21:01:47+01:00"
+++

Si definisca una funzione che prenda in input una lista di numeri interi `lista_numeri` e un numero intero `divisore`, e ritorni una lista di tuple, dove ogni tupla è composta da due elementi: il primo è un numero di `lista_numeri` e il secondo è `True` se quel numero è divisibile per `divisore`, `False` altrimenti.

```python
lista_numeri = [3, 6, 8, 12, 16, 21]
tupla_divisibili(lista_numeri, 3) #Ritorna [(3, True), (6, True), (8, False), (12, True), (16, False), (21, True)]
tupla_divisibili(lista_numeri, 4) #Ritorna [(3, False), (6, False), (8, True), (12, True), (16, True), (21, False)]
```
<details>
<summary>Mostra la soluzione</summary>

```python
def tupla_divisibili(lista_numeri, numero):
    result = []
    for num in lista_numeri:
        is_divisible = num % numero == 0
        result.append((num, is_divisible))
    return result

def tupla_divisibili_v2(lista_numeri, numero):
    return [(num, num % numero == 0) for num in lista_numeri]
```

</details>

