# Calcolatore Voto Laurea
## Opzione Web

### Online
Sì può accedere al calcolatore mediante il link:
```link
https://agda78.github.io/Calcolo_Voto_Laurea/
```
Oppure cliccando [qui](https://agda78.github.io/Calcolo_Voto_Laurea/)

### Offline
Basta clonare la repo con il comando:
```bash
git clone https://github.com/Agda78/Calcolo_Voto_Laurea.git
```

Poi è possibile aprire la pagina html `index.html` che permetterà di accedere al calcolatore in modo offline mediante l'interfaccia web.

[!NOTE]
>Nel caso in cui si dovesse modificare il numero di CFU per via di un piano di studi differente, allora premere sulla rotellina in alto a sinistra per poter modificare il numero di CFU utilizzato all'interno del calcolo


## Opzione Python
Nella cartella python è possibile trovare il file calcolo_voto_laurea che si sta cercando e si può proseguire con le linee guida seguenti

### Descrizione
Script python grafico, che permette un calcolo del voto di laurea previsto (sia Triennale che Magistrale) in base ai parametri descritti dal dipartimento DIETI dell' Università degli studi di Napoli "Federico II"

### Prerequisiti
- Python 3.x
- Tkinter

### Installazione ed avvio

### 
```bash
git clone https://github.com/Agda78/Calcolo_Voto_Laurea.git
cd Calcolo_Voto_Laurea
```
## Avvio dello script
```bash
python ./python/calcolo_voto_laurea.py
```
o
```bash
python3 ./python/calcolo_voto_laurea.py
```
### Assicurarsi di aver installato tkinter
Nel caso l'avvio diretto desse problemi, provare ad installare la libreria tkinter con il comando seguente

###
```bash
pip install tk
```
### Per piani di studi con cfu diversi dallo standard
Una volta scaricato lo script, aprirlo e modificare le variabili:
- num_cfu_triennale
- num_cfu_magistrale


In base al piano di studi intrapreso (numero di cfu totali conseguiti)
