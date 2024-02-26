+++
author = "Domiziano Scarcelli"
title = "2.003 - Somma liste innestate"
categories = [ "Difficoltà 2",]
tags = [ "liste", "ricorsione",]
date = "2024-02-14T11:09:03+01:00"
+++
TODO: rifinisci testo

Si vuole progettare una funzione che prende in input una lista di liste innestate fino ad un certo livello, in cui all’interno sono presenti dei numeri (di cui è ignoto il livello di innestamento a priori). Si vuole tornare la somma di tutti questi numeri.

<details>
<summary>Mostra la soluzione</summary>

```python
def somma_lista(lista, risultato=0):
    # Caso base
    if len(lista) == 0:
        return risultato # Ritorna il risultato in caso non c'è più nulla da esplorare
    
    elemento = lista[0]

    # Passo ricorsivo
    if type(elemento) is list:
        risultato = esplora_lista(elemento, risultato) # Esplora la lista innestataa
    else:
        risultato += elemento # Aggiunge elemento al risultato solo se non è una lista
    return somma_lista(lista[1:], risultato) # Continua la somma nel resto della lista

```

</details>

