+++
author = "Domiziano Scarcelli"
title = "1.93 - Decora Stringa"
categories = [
    "Difficoltà 1",
]
tags = [
    "stringhe",
]
+++

Si scriva una funzione `decora_stringa` che, presa in input una stringa su una sola riga (nel senso che non sono presenti caratteri di accapo `\n`) ritorni la stringa “decorata” dal carattere “#” così come si vede nell’esempio.

Da notare che le righe superiore ed inferiore sono formate solo dal carattere “#”, mentre la riga centrale ha il carattere “#”, poi uno spazio, poi la stringa, poi uno spazio e poi di nuovo il carattere “#”

```python
testo = "Mario mangia il pane"
print(decora_stringa(testo))
#Stampa il seguente testo:

########################
# Mario mangia il pane #
########################
```

<details>
<summary>Mostra la soluzione</summary>

```python
def decora_stringa(stringa):
    """ Data una stringa in input su una sola riga, si vuole ritornare tale stringa
        circondata da caratteri #"""
    riga_caratteri = "#" * (len(stringa) + 2)
    centro = f"#{stringa}#"
    stringa_finale = f"{riga_caratteri}\n{centro}\n{riga_caratteri}"
    return stringa_finale
```

</details>
