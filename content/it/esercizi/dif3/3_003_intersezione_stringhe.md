+++
author = "Domiziano Scarcelli"
title = "3.003 - Intersezione tra stringhe"
categories = [ "Difficoltà 3",]
tags = [ "stringhe", "for-loops",]
date = "2024-02-14T11:09:03+01:00"
+++

Si definisca una funzione che prende in input due stringhe e ritorni la stringa formata dai caratteri che nella posizione $j$ appaiono in entrambe le stringhe.

L’intersezione in questo caso deve rispettare l’ordine dei caratteri.

```python
intersezione_stringhe("mario", "mamma") #Ritorna "ma"
intersezione_stringhe("giovanna", "giovanni") #Ritorna "giovann"
intersezione_stringhe("muletto", "variopinto") #Ritorna ""
intersezione_stringhe("male", "benevolo") # Ritorna "e"
```

Illustrazione per farti capire meglio il problema da risolvere: 

```python
mario
mamma
ma

giovanna
giovanni
giovann

muletto
variopinto

male
benevolo
   e
```

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def intersezione_stringhe(stringa1, stringa2):
    stringa_finale = ""
    for i in range(min(len(stringa1), len(stringa2))):
        if stringa1[i] == stringa2[i]:
            stringa_finale += stringa1[i]
    return stringa_finale
```
</details>
