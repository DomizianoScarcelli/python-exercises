+++
author = "Domiziano Scarcelli"
title = "1.018 - Filtra parole secondo prefisso"
categories = [ "Difficoltà 1",]
tags = [ "liste", "stringhe",]
date = "2024-02-13"
+++

Si scriva una funzione che prende in input una stringa `prefisso` ed una lista di stringhe `lista_parole`, e ritorni una lista contenente le parole in `lista_parole` che iniziano con `prefisso`.

```python
lista_parole = ["mario", "mamma", "pane", "gatto", "topo", "torino"]
parole_prefisso("ma", lista_parole) #Ritorna ["mario", "mamma")
parole_prefisso("pan", lista_parole) #Ritorna ["pane"]
parole_prefisso("t", lista_parole) #Ritorna ["topo", "torino]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def prefisso_nome(prefisso, lista_parole):
    lista_nomi = []
    for parola in lista_parole:
        if parola[0:len(prefisso)] == prefisso:
            lista_nomi.append(parola)
    return lista_nomi
```
</details>
