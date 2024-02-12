+++
author = "Domiziano Scarcelli"
title = "1.97 - Ordina elementi dizionario"
categories = [
    "Difficoltà 1",
]
tags = [
    "lambda",
    "ordinamento"
]

+++
Si deve ordinare un dizionario che associa stringhe a liste.

Si vuole ritornare la lista formata dalle tuple (chiave, valore) ordinata in modo crescente secondo la lunghezza del valore (ovvero della lista associata alla chiave).

La lista di tuple si può ottenere tramite `list(diz.items())`.

Si scriva una funzione lambda da usare come chiave di ordinamento in maniera da risolvere il problema.

```python
dizionario = 
{
	"mario": [1,2,3],
	"paolo": [7,3,2,5,4],
	"giulio": [3]
}

lista_tuple = list(dizionario.items())
lista_tuple.sort(key=#La tua funzione lambda)
print(lista_tuple)
#[("paolo",[7,3,2,5,4]), ("mario", [1,2,3]), ("giulio", [3])]
```

<details>
<summary>Mostra la soluzione</summary>

```python
def ordina_elementi(dizionario):
	items = list(dizionario.items())
	items.sort(key=lambda tupla: len(tupla[1]))
	return items

# Items sarà ordinato secondo la lunghezza del secondo elemento della tupla
# Ovvero il valore associato ad ogni chiave del dizionario
```
</details>
