# Controllo data

#### Problema
Dati in ingresso tre numeri interi d,m,y che vorrebbero indicare una data,
verificare se tale giorno esista effettivamente nel calendario,
pagando in particolare attenzione alla regola che fissa quali anni siano bisestili secondo il calendario gregoriano (divisibili per 400 oppure per 4 ma non per 100).

## Esempi di date (d,m,y) non ammissibili:
- (1,1,0) no, perchè deve valere che y > 0;
- (-1,1,2000) no, perchè deve valere che d > 0;
- (1,15,2000) no, perchè deve valere che m <= 12;
- (31,11,1748) no, perchè novembre ha solo 30 giorni;
- (29,2,1900) no, perchè il 1900 non è un anno bisestile;

## Valore di return 
- restituire 1 se la data esiste
- 0 in tutti gli altri casi
