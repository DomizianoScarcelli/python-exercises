+++
author = "Domiziano Scarcelli"
title = "1.020 - Lista di permutazione"
categories = [ "Difficoltà 1",]
tags = [ "for-loops", "liste",]
date = "2024-02-14T11:09:03+01:00"
+++

Si definisca una funzione che prende due liste della stessa lunghezza in input, `lista` e `lista_permutazione`, e ritorni una nuova lista in maniera tale che ogni elemento nell’indice $i$ venga inserito nell’indice che si trova nella posizione $i$ nella `lista_permutazione`.

Nota: dai per scontato che la `lista_permutazione` sia ben formata, vuol dire che al suo interno devono essere presenti solo i numeri che indicano gli indici possibili di `lista`, e ogni indice deve apparire una ed una sola volta.

Extra: cosa succederebbe se in `lista_permutazione` ci fossero numeri che non rappresentano gli indici di `lista`?

```python
lista = [1,2,3,4,5]
lista_permutazione = [0, 3, 2, 1, 4]

permuta_lista(lista, lista_permutazione) #Ritorna [1,4,3,2,5]
permuta_lista(lista, [4,3,2,1,0]) # Ritorna [5,4,3,2,1]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def permuta_lista(lista, lista_permutazione):
    lista_risultato = [0 for _ in range(len(lista))]
    for indice, elemento in enumerate(lista):
        indice_nuovo = lista_permutazione[indice]
        lista_risultato[indice_nuovo] = elemento
    return lista_risultato
```

</details>

