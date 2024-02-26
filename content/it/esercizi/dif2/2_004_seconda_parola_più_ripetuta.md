+++
author = "Domiziano Scarcelli"
title = "2.004 - Seconda parola più ripetuta"
categories = [ "Difficoltà 2",]
tags = [ "liste", "stringhe",]
date = "2024-02-25"
+++

Si scriva una funzione che prende una stringa in input che rappresenta un testo, e si ritorni la seconda parola più ripetuta all’interno di questo testo, ovvero non la parola che appare più volte, ma quella al “secondo posto” sul podio.

>Nota: non dare per scontato che tutte le parole siano in minuscolo. Pensa anche a rimuovere la punteggiatura comune, come il punto, la virgola, il punto e virgola, il punto esclamativo, interrogativo ed i due punti.

```python
testo = "Questi occhiali mi fanno vedere male, vedere è importante, vedere con gli occhiali"
seconda_ripetuta(testo) #Ritorna "occhiali", che viene ripetuta 2 volte. La più ripetuta è "vedere".
```

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def seconda_ripetuta(string):
    parsed_string = "".join(l for l in string if (l.isalpha() or l == " ")).lower().split()
    word_count = {}
    for word in parsed_string:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return sorted(word_count, key=word_count.get, reverse=True)[1]
```
</details>

