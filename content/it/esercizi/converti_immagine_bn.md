+++
author = "Domiziano Scarcelli"
title = "2.1 - Converti immagine in bianco e nero"
categories = [
    "Difficoltà 2",
]
tags = [
    "matrici",
    "immagini"
]
+++
Un immagine può essere modellata tramite una matrice i cui elementi sono tuple della forma $(r,g,b)$ che modellano i singoli pixel in cui, per ogni tupla (pixel) $r$ è la quantità di rosso, $g$ è la quantità di verde e $b$ è la quantità di blu. 

I valori $r,g,b$ possono assumere un valore che va da 0 a 255 compresi. Ad esempio la tupla $(0,0,0)$ è un pixel nero, $(255,255,255)$ è un pixel bianco, $(100,100,100)$ è un pixel grigio di intensità 100, $(100,0,0)$ è un pixel di un rosso chiaro.

Una tupla contenente lo stesso valore per $r,g,b$ assume il colore grigio. Più questo valore è vicino al 0, più il grigio è intenso (0 è nero) e più è vicino a 255, meno intenso è il grigio (255 è bianco).

Per trasformare un’immagine da colorata a bianco e nero, basta sostituire ogni pixel $(r,g,b)$ con la media dei tre valori. Ovvero per ogni pixel $(r,g,b)$ questo deve essere sostituito con il pixel $(\frac{r+g+b}{3}, \frac{r+g+b}{3}, \frac{r+g+b}{3})$.

Notare che il pixel deve essere un intero, quindi può essere arrontondato mediante la funzione `round(numero)`.

Si definisca una funzione che prende una matrice formata da tuple di questo tipo, che rappresenta un immagine, e ritorni un’altra matrice che rappresenta l’immagine in bianco e nero.

```python
img = [[(100,34,25), (12,34,23), (10,10,10)],
			[(240,255,0), (100,10,44), (10,10,10)],
			[(100,34,25), (12,34,23), (0,100,0)]]
bianco_e_nero(img)
#Ritorna la matrice
[[(53, 53, 53), (23, 23, 23), (10, 10, 10)], 
[(165, 165, 165), (51, 51, 51), (10, 10, 10)], 
[(53, 53, 53), (23, 23, 23), (33, 33, 33)]]
```

>Nota: in questo caso stiamo rappresentando ogni pixel nell'immagine in bianco e nero come una tupla (r,g,b) dove $r=g=b$. Per occupare meno memoria, solitamente si conserva solamente una componente di ogni pixel invece dell'intera tupla.

<details>
<summary>Mostra la soluzione</summary>

```python
def bianco_e_nero(img):
    risultato = []
    for riga in img:
        nuova_riga = []
        for elem in riga:
            r,g,b = elem
            media = round((r+g+b)/3)
            pixel_grigio = (media, media, media)
            nuova_riga.append(pixel_grigio)
        risultato.append(nuova_riga)
    return risultato
```

</details>
