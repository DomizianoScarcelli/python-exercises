+++
author = "Domiziano Scarcelli"
title = "4.001 - Rappresenta directory con dizionario"
categories = [ "Difficoltà 4",]
tags = [ "dizionari", "ricorsione",]
date = "2024-02-26"
+++
[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/4_001_rappresenta_directory.zip)

Si implementi una funzione rappresenta_directory(directory) che dato il percorso assoluto di una directory,k
rappresenta la sua struttura mediante un dizionario.

In particolare:
- la chiave del dizionario è il nome della directory
- i valori associati alle chiavi sono:
    - un dizionario per ogni sottodirectory
    - il contenuto del file per ogni file

Esempio per la directory_esercizio_68 ritorna il seguente dizionario:

    {
        "vtkgn": {
                "iojiq": {
                        "amwgi.txt": "This is a sample file.",
                        "eogzu": {
                                "hhdix.txt": "This is a sample file.",
                                "lciny.txt": "This is a sample file.",
                                "zpplp.md": "This is a sample file."
                        },
                        "folnb.csv": "This is a sample file.",
                        "xcvsu.csv": "This is a sample file."
                },
                "kuhmp.txt": "This is a sample file.",
                "nhtqg.csv": "This is a sample file.",
                "zvxis.csv": "This is a sample file."
        }

Consiglio: per evitare un dizionario infinito, ogni volta che fai la chiamata ricorsiva
rappresenta_directory(dir_path, dizionario), passa un dizionario vuoto dict() come argomento per il dizionario.

Funzioni del modulo os utili:
- os.listdir(path): ritorna la lista di tutti i nomi dei file e delle directory all'interno di path (nota bene: torna solo i nomi, non i percorsi assoluti)
- os.path.isdir(path): ritorna True se path è una directory
- os.path.join(path1, path2, ...): ritorna la concatenazione di path1, path2, ...

Altri consigli:
- Per stampare il dizionario in maniera più leggibile, si può utilizzare la funzione pprint del modulo pprint (già importato). Esempio: pprint(dizionario)

<details>
<summary>Mostra la soluzione</summary>

```python
def rappresenta_directory(dir_path, dizionario=dict()):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            dizionario[file] = rappresenta_directory(
                file_path, dict())
        else:
            with open(file_path, "r") as f:
                contenuto = f.read()
            dizionario[file] = contenuto
    return dizionario
```

</details>

