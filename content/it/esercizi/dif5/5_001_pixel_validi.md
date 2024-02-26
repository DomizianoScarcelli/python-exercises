+++
author = "Domiziano Scarcelli"
title = "5.001 - Conta pixel validi in immagine"
categories = [ "Difficoltà 5",]
tags = ["immagini",]
date = "2024-02-26T12:21:52+01:00"
+++
[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/5_001_pixel_validi.zip)

Si progetti una funzione che prende in input il percorso di un'immagine.

Un pixel "valido" è un pixel di un determinato colore i cui vicini hanno
TUTTI lo stesso colore. (Non considerare i pixel vicini in diagonale).
Un pixel di colore NERO (0,0,0) è sempre NON valido.

In particolare i pixel vicini sono quelli sopra, sotto, a destra e a
sinistra.  Se un pixel si trova sul bordo, si considerino solo i pixel
adiacenti che esistono. Questo vuol dire se un pixel si trova nell'angolo in
alto a sinistra, allora basta che abbia lo stesso colore del pixel a destra
e del pixel sotto per essere considerato valido.

Si crei un dizionario in cui le chiavi sono i colori (la tupla r,g,b) dei
pixel trovati sopra, e le chiavi una lista di coordinate del tipo (x,y) dei
pixel validi di tale colore.  Ritornare gli items del dizionario ordinati a
seconda della coordinata media dei pixel validi di un determinato colore, da
sinistra a destra e, in caso di parità, dall'alto in basso.  Esempio: se il
dizionario è {(10,1,12): [(10,0), (1,20)], (255,255,255): [(12,13), (1,9)]},

la funzione ritorna [((255,255,255), [(1,9), (12,13)]), ((10,1,12): [(10,0),
(1,20)]) perché il punto medio del colore (255,255,255) è (6.5, 11) e il punto medio
del colore (10,1,12) è (5.5, 10), quindi il secondo colore è più a sinistra
del primo.


- Salvare l'immagine colorando i pixel non validi di nero.

Nota: puoi caricare l'immagine con images.load(path) e salvarla con images.save(img, path).

<details>
<summary>Mostra la soluzione</summary>

```python
def pixel_validi(path_immagine, save_path):
    img = images.load(path_immagine)
    dizionario = {}
    valid_coords = []
    BLACK = (0, 0, 0)
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x] != BLACK:
                color = img[y][x]
                neighbours = get_neighbours(img, x, y)
                for neighbour in neighbours:
                    xn, yn = neighbour
                    if img[yn][xn] != color:
                        break
                else:
                    valid_coords.append((x, y))
                    valid_coords.extend(neighbours)
                    if color not in dizionario:
                        dizionario[color] = [(x, y)]
                    else:
                        dizionario[color].append((x, y))

    items_ord = sorted(dizionario.items(), key=lambda x: (sum(
        [i[0] for i in x[1]])/len(x[1]), sum([i[1] for i in x[1]])/len(x[1])))

    for y in range(len(img)):
        for x in range(len(img[0])):
            if (x, y) not in valid_coords:
                img[y][x] = (0, 0, 0)
    images.save(img, save_path)

    return items_ord
```

</details>

