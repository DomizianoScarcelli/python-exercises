+++
author = "Domiziano Scarcelli"
title = "0.019 - Rimpiazza carattere in stringa"
categories = [ "Difficoltà 0",]
tags = [ "stringhe",]
date = "2024-02-14"
+++
Si definisca una funzione che prende in input una lista di stringhe ed un carattere e si ritorni la lista di stringhe in cui tutte le occorrenze di quel carattere sono state rimpiazzate dal carattere `.`.

Prova a risolvere questo esercizio sia con l’uso di `string.replace()` sia rimpiazzando i caratteri manualmente.

Nota: dai per scontato che sia le stringhe sia il carattere siano minuscoli

```python
lista_stringhe = ["mario", "giulio", "giovanna", "matteo","onorio"]
rimpiazza_caratteri(lista_stringhe, "o") #Ritorna ["mari.", "giuli.", "gi.vanna", "matte.", ".nori."]
```

<details>
<summary>Mostra la soluzione</summary>
Utilizzando replace:

```python
def rimpiazza_caratteri_2(lista_stringhe, carattere):
    risultato = []
    for parola in lista_stringhe:
        parola_rimpiazzata = parola.replace(carattere, ".")
        risultato.append(parola_rimpiazzata)
    return risultato
```

Senza utilizzare replace:

```python
def rimpiazza_caratteri(lista_stringhe, carattere):
    risultato = []
    for parola in lista_stringhe:
        nuova_parola = ""
        for lettera in parola:
            if lettera != carattere:
                nuova_parola += lettera
            else:
                nuova_parola += "."
        risultato.append(nuova_parola)
    return risultato
```

</details>
