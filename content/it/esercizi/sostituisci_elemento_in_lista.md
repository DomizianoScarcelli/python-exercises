+++
author = "Domiziano Scarcelli"
title = "Sostituisci elemento in lista"
categories = [
    "Difficoltà 0",
]
tags = [
    "liste"
]
+++

Scrivere una funzione che prenda in input tre parametri:

- Una lista `lst`
- Un numero `num`
- Una posizione `pos`

La funzione ritorna una nuova lista uguale a `lst`, ma in cui l’elemento in posizione `pos` è sostituito dal numero `num`.  

### Esempio esecuzione

**NOTA BENE:** Ricorda che puoi accedere ad un elemento all’indice `i` di una lista `lst` facendo `lst[i].`

Ricorda anche che gli indici delle liste partono da 0 ed arrivano fino a `len(lista)-1`.

Dai per scondato che `pos < len(lista)` altrimenti ti darebbe un errore.

```python
sostituisci_elem([1,6,9,6,4], 100, 2)
# La funzione ritorna la lista [1,6,100,4] che è uguale alla lista in input, 
# ma il numero in posizione 2 è stato modificato col numero 100.
sostituisci_elem([2,7,3,64,2], 50, 0) #Ritorna [50,7,3,64,2]
```


<details>
<summary>Mostra la soluzione</summary>

```python
def sostituisci_elem(lista, num, pos):
    lista_copia = lista.copy() # Altrimenti andrei a modificare la lista in input
    lista_copia[pos] = num
    return lista_copia
```

</details>
