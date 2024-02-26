+++
author = "Domiziano Scarcelli"
title = "1.003 - Dizionario contatore di parola a partire da un testo"
categories = [ "Difficoltà 1",]
tags = [ "dizionari", "stringhe",]
date = "2024-02-13T20:39:12+01:00"
+++
Si definisca una funzione che, presa in input una stringa che rappresenta un testo (che non contiene punteggiatura, ma che può contenere parole con maiuscole), ritorni un dizionario che associ ad ogni parola le volte che questa è presente all’interno del testo.

Puoi usare la funzione `diz_conta_parole` definita nella lezione precedente.

Nota che per passare da una stringa contenente un testo alla lista di parole puoi usare il metodo `stringa.split(” “)`. Per maggiore info su questo metodo fai riferimento alla pagina [Funzioni e Metodi utili](https://www.notion.so/Funzioni-e-Metodi-utili-239c8c5f760d4d95aa9e0f636a94a6cb?pvs=21). 

```python
testo = "Mario compra la pasta cucina la pasta compra il pollo mangia la Pasta col Pollo"
diz_conta_parole_da_testo(testo)
# Ritorna il dizionario contenente quante volte ogni parola è presente all'interno del testo,
# Ricorda che Pollo e pollo devono essere contate come la stessa parola. 
```

<details>
<summary>Mostra la soluzione</summary>

```python
#Soluzione: Alessio Lucciola
def diz_conta_parole_da_testo(testo):
    testo = testo.lower().split(" ")
    diz_finale = {}
    for p in testo:
        diz_finale[p] = diz_finale.get(p, 0) + 1 # Se la parola non è presente nel dizionario, aggiungila con valore 0 e incrementa subito di 1. Altrimenti incrementa solo il contatore di 1.
    return diz_finale

# Versione alterntiva
def diz_conta_parole_da_testo_due(testo):
    testo = testo.lower().split(" ")
    diz_finale = {}
    for p in testo:
        if p in diz_finale:
            diz_finale[p] += 1
        else:
            diz_finale[p] = 1
    return diz_finale
```
</details>
