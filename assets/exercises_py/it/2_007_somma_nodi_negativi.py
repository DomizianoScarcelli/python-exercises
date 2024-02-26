class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.children = []

    def add_chidlren(self, *nodi):
        for nodo in nodi:
            self.children.append(nodo)

    def __repr__(self):
        return f"{self.id}"


#Ignora il codice sottostante, è solo per costruire l'albero
def costruisci_albero_esercizio():
    radice = Nodo(5)
    nodo_2 = Nodo(-10)
    nodo_3 = Nodo(2)
    nodo_4 = Nodo(-3)
    nodo_5 = Nodo(11)
    nodo_6 = Nodo(4)
    nodo_7 = Nodo(2)
    nodo_8 = Nodo(-1)
    nodo_9 = Nodo(-4)
    nodo_10 = Nodo(7)
    nodo_11 = Nodo(3)
    nodo_12 = Nodo(1)

    radice.add_chidlren(nodo_2, nodo_3, nodo_4)
    nodo_2.add_chidlren(nodo_5)
    nodo_3.add_chidlren(nodo_6, nodo_7, nodo_8, nodo_9, nodo_10)
    nodo_7.add_chidlren(nodo_11, nodo_12)

    return radice


def somma_nodi(tree, somma=0):
    """
    Si implementi una funzione somma_valori, che somma tutti i valori dei nodi
    all'interno dell'albero, solo se tale valore Ã¨ positivo.

    Esempio:

    L'abero costruito da costruisci_albero_esercizio() Ã¨ il seguente:
              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |   |  |  |  |         
          4   2 -1 -4  7        
            __|__              
           |     |            
           3     1           
    La funzione deve restituire: 5 + 2 + 11 + 4 + 2 + 7 + 3 + 1 = 35
    """
    #TODO: Implementa qui la tua funzione
    pass


if __name__ == "__main__":
    radice = costruisci_albero_esercizio()
    risultato = somma_nodi(radice)
    somma_corretta = 35
    assert risultato == somma_corretta, f"""
    Somma errata:
    La somma da te generata: {risultato}
    La somma corretta: {somma_corretta}
    """
    print(
        f"La somma dei nodi non negativi è {risultato}, il risultato è corretto")