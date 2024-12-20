# Calcolatore Voto Laurea

## Descrizione
Script python grafico, che permette un calcolo del voto di laurea previsto (sia Triennale che Magistrale) in base ai parametri descritti dal dipartimento DIETI dell' Università degli studi di Napoli "Federico II"

## Prerequisiti
- Python 3.x
- Tkinter

## Installazione ed avvio

### 
```bash
git clone https://github.com/Agda78/calcolo_voto_n46.git
cd calcolo_voto_n46
```
# Avvio dello script
```bash
python ./calcolo_voto_laurea.py
```
o
```bash
python3 ./calcolo_voto_laurea.py
```
# Assicurarsi di aver installato tkinter
Nel caso l'avvio diretto desse problemi, provare ad installare la libreria tkinter con il comando seguente
###
```bash
pip install tk
```
## Per piani di studi con cfu diversi dallo standard
Una volta scaricato lo script, aprirlo e modificare le variabili:
- num_cfu_triennale
- num_cfu_magistrale
In base al piano di studi intrapreso (numero di cfu totali conseguiti)
