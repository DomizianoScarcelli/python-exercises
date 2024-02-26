+++
author = "Domiziano Scarcelli"
title = "0.018 - Trova parola con occorrenze singole maggiori"
categories = [ "Difficoltà 0",]
tags = [ "stringhe", "lambda",]
date = "2024-02-14"
+++
Si definisca una funzione che prende in input una lista di stringhe, e ritorna la stringa che ha il maggior numero di caratteri unici.

```python
lista = ['gatto', 'gattogattogattogatto', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unica']
parola_unica(lista) #Ritorna abcdefhijklmnop perchè ha più caratteri unici
```

<details>
<summary>Mostra la soluzione</summary>

```python
def parola_unica(lista_parole):
	# Ritorno la parola che ha la lunghezza maggiore una volta che è stata 
	# trasformata in insieme, ovvero i cui elementi doppioni sono stati
	# eliminati
	return lista_parole.max(key=lambda parola: len(set(parola))
```

</details>
