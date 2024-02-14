+++
author = "Domiziano Scarcelli"
title = "2.005 - Lista intercalcata"
categories = [
    "Difficoltà 2",
]
tags = [
    "liste",
]
+++

Si scriva una funzione che prenda in input due liste e ritorni una nuova lista ottenuta intercalando gli elementi delle due liste. 

Per intercalcare si intende che si prende prima un elemento della lista 1 e poi uno della lista 2, alternando così finchè gli elementi non terminano. Le liste in input sono di uguale lunghezza.

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_intercalata(lista1, lista2) # Ritorna [1, 4, 2, 5, 3, 6]
```

Extra: Modifica l’algoritmo in maniera tale che se una lista è maggiore dell’altra, allora gli elementi restanti della lista più lunga vengono semplicemente messi alla fine della lista intercalcata.

```python
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [4, 5, 6]

lista_intercalata(lista1, lista2) # Ritorna [1, 4, 2, 5, 3, 6, 4, 5, 6, 7, 8]
```

<details>
<summary>Mostra la soluzione</summary>
>TODO: da fare

</details>

