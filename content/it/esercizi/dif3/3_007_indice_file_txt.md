+++
author = "Domiziano Scarcelli"
title = "3.007 - Indice file txt"
categories = [ "Difficoltà 3",]
tags = [ "dizionari", "ricorsione",]
date = "2024-02-26T12:21:52+01:00"
+++
[Scarica qui i file necessari per risolvere l'esercizio](/exercises_py/it/3_007_indice_file_txt.zip)

Si implementi una funzione rappresenta_directory(directory) che dato il percorso assoluto di una directory,
ritorna un dizionario in cui:
- Le chiavi del dizionario sono i nomi dei file con estensione .txt
- Il valore associato ad ogni chiave è il contenuto di tale file

Esempio per la directory_esercizio_68 ritorna il seguente dizionario:

    {
        'amwgi.txt': 'This is a sample file.',
        'hhdix.txt': 'This is a sample file.',
        'kuhmp.txt': 'This is a sample file.',
        'lciny.txt': 'This is a sample file.'
    }

Funzioni del modulo os utili:
- os.listdir(path): ritorna la lista di tutti i nomi dei file e delle directory all'interno di path (nota bene: torna solo i nomi, non i percorsi assoluti)
- os.path.isdir(path): ritorna True se path è una directory
- os.path.join(path1, path2, ...): ritorna la concatenazione di path1, path2, ...

Altri consigli:
- Per stampare il dizionario in maniera più leggibile, si può utilizzare la funzione pprint del modulo pprint (già importato). Esempio: pprint(dizionario)

<details>
<summary>Mostra la soluzione</summary>

```python
def indice_file_txt(dir_path, dizionario=dict()):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            indice_file_txt(file_path, dizionario)
        else:
            if file.endswith(".txt"):
                with open(file_path, "r") as f:
                    dizionario[file] = f.read()
    return dizionario
```

</details>

