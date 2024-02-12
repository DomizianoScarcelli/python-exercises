+++
author = "Domiziano Scarcelli"
title = "Primi N numeri primi"
categories = [
    "Difficoltà 1",
]
tags = [
    "for-loops",
    "liste"
]
+++

Si definisca una funzione che genera una lista lunga N contenente i primi N numeri primi.

Ricorda che un numero è primo solo se è divisibile per nessun numero apparte se stesso ed 1.

Consiglio: devi usare un if,  considera la condizione contraria per valutare se un numero è primo o meno:

- Un numero **NON** è primo se esiste almeno un numero divisore diverso da 1 e da se stesso. Il possibile divisore è comunque all’interno dell’intervallo [1, numero_considerato] e non oltre.

Esempi: 

- 7 è primo perchè non esiste nessun numero da 1 a 7 che lo divide (a parte 1 e 7)
- 4 non è primo perchè esiste un numero da 1 a 4 che lo divide, e questo è 2.

> N.B. 1 è un caso speciale e non considerarlo in quanto non è un numero primo.

### Esempio esecuzione

```python
primi_n_primi(3) #Ritorna [2,3,5]
primi_n_primi(5) #Ritorna [2,3,5,7,11]
```

<details>
<summary>Mostra la soluzione</summary>


Soluzione con una funzione di utilità che viene utilizzata come condizione:
```python
def primo(n):
    """
    Ritorna True se n è primo, False altrimenti
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def num_primi(n):
    """
    Ritorna la lista dei primi n numeri primi 
    (usa la funzione primo(n) per capire se un numero è primo o meno)
    """
    lista = []
    numero_corrente = 2
    while len(lista) < n:
        if primo(numero_corrente):
            lista.append(numero_corrente)
        numero_corrente += 1
    return lista
```

Soluzione con un "break" e il controllo direttamente all'interno del for
```python
def num_primi_unificato(n):
		"""
		Ritorna la lista dei primi n numeri primi 
		"""
    lista = []
    numero_corrente = 2
    while len(lista) < n:
        for i in range(2, numero_corrente): #Guardo tutti i numeri che vanno da 2 a num_corrente - 1
            if numero_corrente % i == 0: #Se trovo un numero 'i' che lo divide, allora num_corrente non`e primo
                break #Interrompo il ciclo for
        else: #Questo else si riferisce al for, e viene eseguito solo per quelle iterazioni che non raggiungono la clausola "break" (numeri primi)
            lista.append(numero_corrente)  
        numero_corrente += 1
    return lista
```

</details>

> Notare che in questo esempio l’else fa riferimento al “for”, e viene eseguito solamente per quelle iterazioni in cui non viene raggiunta la clausola “break”, 
