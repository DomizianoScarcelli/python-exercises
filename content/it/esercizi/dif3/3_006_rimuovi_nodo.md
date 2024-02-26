+++
author = "Domiziano Scarcelli"
title = "3.006 - Rimuovi nodo albero"
categories = [ "Difficoltà 3",]
tags = [ "alberi", "ricorsione",]
date = "2024-02-26T11:27:05+01:00"
+++
[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/3_006_rimuovi_nodo.zip)

Si implementi una funzione rimuovi_nodo(tree, valore) che prende in input
l'albero ed il valore di un nodo. Modifica l'albero in maniera distruttiva
in modo da rimuovere tutti i nodi che hanno il valore valore, rimuovendo
anche i rispettivi figli.

Esempio:

L'abero costruito da costruisci_albero_esercizio() è il seguente:

              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |   |  |  |  |         
          4   3 -1 -4  7        
            __|__              
           |     |            
           3     1           

La funzione rimuovi_nodo(tree, 2) modifica l'albero in maniera distruttiva
in modo da ottenere
```
              5                       
      ________|_____________         
     |                     |       
    -10                    -3      
     |                
     11   
```
Mentre La funzione rimuovi_nodo(tree, 3) modifica l'albero in maniera distruttiva
in modo da ottenere

              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |     |  |  |         
          4    -1 -4  7        

<details>
<summary>Mostra la soluzione</summary>

```python
def rimuovi_nodo(radice, valore):
    for child in radice.children:
        if child.valore == valore:
            radice.children.remove(child)
        else:
            rimuovi_nodo(child, valore)
```

</details>

