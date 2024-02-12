+++
author = "Domiziano Scarcelli"
title = "Lista di lettere"
categories = [
    "Difficoltà 0",
]
tags = [
    "liste",
    "stringhe"
]
+++

Si scriva una funzione che prende in input una stringa `stringa` formata da soli caratteri minuscoli (non ci sono lettere maiuscole) e che ritorni una lista contenente le lettere, in modo che nella lista non ci siano ripetizioni. L’ordine all’interno della lista non è importante. 

> NOTA BENE: Puoi iterare sopra una stringa nello stesso modo in cui iteri sugli elementi di una lista.

Ecco un esempio
```python

stringa = "mario"
for lettera in stringa:
	print(lettera) #Lettera varrà prima “m” poi “a” poi “r” ecc. per tutte le lettere della stringa
```

Esempio di esecuzione:
```python
stringa_senza_rip("mamma") #Ritorna ["m", "a"] in qualsiasi ordine
stringa_senza_rip("paolo") #Ritorna ["p", "a", "o", "l"] in qualsiasi ordine 
```

In sostanza, iterare su una stringa con il costrutto `for l in stringa` ti permette di iterare sulle lettere della stringa.

<details>
<summary>Mostra la soluzione</summary>

```python
# Mantiene l’ordine delle lettere nella lista
def stringa_senza_rip(stringa):
    lista = []
    for lettera in stringa:
        if lettera not in lista:
            lista.append(lettera)
    return lista
```

```python
# L’ordine delle lettere nella lista finale è casuale
def stringa_senza_rip(stringa):
    return set(stringa)
```
</details>
