---
name: hdd-presentazioni
description: Prepara presentazioni per interventi pubblici di Hotel Digital Distribution (HDD) con il sistema grafico comune del gruppo - una pagina HTML che scorre, slide a tutto schermo, colori e caratteri HDD, animazioni, QR finale. Usala quando qualcuno del gruppo HDD chiede slide, una presentazione, un intervento, un talk o un workshop, anche se non nomina HDD o la skill.
---

# Presentazioni HDD

Ogni presentazione del gruppo HDD è una pagina HTML che scorre: una sezione per schermata, a tutto schermo, con frecce, spazio e contatore in basso a destra. La grafica è sempre la stessa per tutti. Cambiano i contenuti.

Il punto di partenza è `modello/modello.html`. Contiene il sistema grafico completo (colori, caratteri, componenti, animazioni) e quindici slide di esempio con testi segnaposto, una per componente.

## Come si lavora

1. **Capire l'intervento.** Chi c'è in sala (albergatori, ville e appartamenti, agenzie…), quanto dura, cosa deve portarsi a casa la gente. Se mancano, chiedilo prima di scrivere.
2. **Scrivere la scaletta prima delle slide.** Una schermata per idea. Per un'ora bastano 35–40 schermate. Dividi in capitoli e apri ogni capitolo con un divisorio.
3. **Copiare il modello** in una cartella nuova, tenere solo i blocchi che servono e cambiare i testi. Non toccare il CSS né il motore in fondo: se serve un componente nuovo, aggiungilo usando i colori e le classi che ci sono.
4. **Costruire il file finale** con lo script (vedi sotto) e controllarlo.
5. **Consegnare** la pagina online (in Claude, come Artifact) e il file `--offline` da scaricare per il giorno dell'evento.

## Le regole della grafica

- **Sfondi alternati.** `slide` (chiaro), `slide rosa`, `slide scura`, `slide blu`. Mai due slide di fila con lo stesso sfondo, tranne due foto a tutto schermo.
- **`data-tono`** vale `chiaro` per chiaro e rosa, `scuro` per scura e blu. Serve al contatore e alla testata.
- **Titolo + seguito.** Ogni slide ha un titolo breve e, dentro, `<span class="seguito">` con la seconda frase in corsivo. Il seguito porta la conseguenza o il punto di vista.
- **Testo corto.** Due o tre righe a slide al massimo. Il resto si dice a voce.
- **Percorso in alto (facoltativo).** Se l'intervento segue una storia a tappe, la testata mostra fino a cinque passi. Compare solo sulle slide con `data-passo` da 1 a 5, non sulle altre.
- **Animazioni.** Si attivano con `data-anim` (`titolo`, `sali`, `righe`, `passi`, `parole`) e ripartono ogni volta che si torna su una slide. Il grafico 3D (`con-3d`) e la foto che si accende (`foto-viva`) vanno usati una volta sola per intervento, nel punto che conta.
- **Proiettore.** Il layout si adatta da solo. Il file finale va controllato almeno a 1280×720 e 1920×1080: nessuna slide deve uscire dallo schermo.

## I componenti del modello

| Componente | Quando usarlo |
|---|---|
| Copertina | Prima slide: evento, titolo, relatore. Le barre del logo HDD si muovono. |
| Divisorio (`titolo grande`) | Apertura di ogni capitolo. |
| Schermo ricostruito (`schermo data-vivo`) | Far vedere una chat AI, una ricerca, una pagina. La domanda si scrive da sola, una risposta si accende. |
| Numeri grandi (`prova`, `data-conta`) | Uno o due risultati misurati. |
| Frase da ricordare (`parole`) + `filo` | Il concetto chiave, più il ragionamento in tre passaggi. |
| Barre orizzontali (`barre-fonti`) | Quote e percentuali, leggibili da lontano. |
| Tabella di confronto (`tabella`) | Due situazioni messe a fianco, per esempio portale e sito. |
| Tre colonne + spunte (`tre`, `spunte`) | Un metodo in tre punti, con le garanzie sotto. |
| Prima e dopo (`confronta-foto`) | Due catture dello stesso sito. La linea scorre da sola, poi si trascina. |
| Cinque azioni (`cinque`) | Cose pratiche da fare dopo l'intervento. |
| A tutta foto (`con-foto foto-viva`) | Il momento emotivo. Foto almeno 1600 px di larghezza. |
| Dati in 3D (`con-3d`) | Il momento in cui parli di dati: punti sparsi che diventano un grafico. |
| Riepilogo + frase finale (`riepilogo`, `finale`) | Prima della chiusura: i punti dell'intervento, poi tre righe che arrivano una alla volta. |
| Invito con QR (`data-qr`) | Cosa fare dopo. L'indirizzo con i parametri UTM dell'evento sta in `data-qr`. |
| Grazie (`chiusura`) | Ultima slide. |

## Come si scrivono i testi

- **Italiano parlato, frasi brevi, «tu» a chi è in sala.** Esempi presi dal lavoro vero.
- **Niente formule da testo generato:** titoli a domanda retorica, «non X ma Y», elenchi a tre solo per ritmo, trattini lunghi, «soluzioni», «su misura», «concreto».
- **Niente gergo da addetti ai lavori:** OTA, canale, booking engine, deep link. Si dice portali, sito, sistema di prenotazione.
- **Esempi credibili per un albergatore.** Se l'esempio fa dire «ma chi non lo farebbe?», va cambiato. Meglio una cosa che molti hanno e pochi scrivono sul sito.
- **Personaggio.** Se usi un ospite inventato per fare da filo, presentalo all'inizio. Quando torna più avanti, ricorda in una riga chi è e dove eravamo rimasti, così la sala non si perde.

## Dati e correttezza

- **Ogni numero ha fonte e data**, nella didascalia sotto.
- **Misurato e stimato restano separati.** Una stima si dichiara come stima.
- **Schermate.** Quelle rifatte portano l'etichetta `<span class="ric">Ricostruzione</span>`, le catture vere `<span class="ric">Vero</span>`.
- **Clienti.** Niente nomi o numeri di un cliente senza il suo consenso. In alternativa si usa «struttura non nominata».
- **Prezzi.** Non si mostrano prezzi diversi tra sito e portali: l'argomento lo spiega HDD a voce. Per parlare di convenienza si mostra quanto resta alla struttura, a parità di prezzo.

## Logo e materiali HDD

- Il logo completo (barre + «HOTEL digital distribution») è già nel modello, in copertina e nella slide finale, come SVG che usa i caratteri della pagina. Per altri usi ci sono `modello/img/logo-hdd-su-chiaro.svg` e `logo-hdd-su-scuro.svg`.
- Le barre colorate del logo (`logo-barre`) sono il segno grafico ricorrente: non cambiarne colori e proporzioni.
- Altri materiali (foto dei lavori, immagini del blog, immagine di condivisione) si prendono dal sito ufficiale https://hoteldigitaldistribution.it, cartella `/assets/img/`, salvandoli in `img/` accanto alla presentazione. Prima di usare la foto di una struttura cliente, chiedi al relatore se c'è il consenso.

## Costruire il file finale

```
python3 -I scripts/costruisci.py mia.html finale.html            # immagini e font dentro il file
python3 -I scripts/costruisci.py mia.html finale.html --offline  # in più le librerie: funziona senza internet
```

- Le immagini si citano con `src="img/nome.jpg"`, relative al file di partenza, e finiscono dentro il file.
- I caratteri ufficiali HDD sono Switzer (testo), Newsreader corsivo (seguiti) e Hanken Grotesk (logo). Lo script li mette sempre dentro il file. Switzer non è nella skill: la prima volta lo script lo scarica da Fontshare in `fonts/`. Se non riesce perché manca internet, dillo al relatore. Non sostituire i caratteri con altri.
- Le librerie (GSAP, Lenis, three.js, qrcode-generator) si caricano da internet. Le copie in `librerie/` servono a `--offline`.

## Prima di consegnare

- Scorri tutte le slide avanti e indietro: le animazioni devono ripartire e nessun testo deve restare vuoto.
- Controlla a 1280×720 e 1920×1080 che niente esca dallo schermo.
- Leggi i titoli in fila: devono raccontare l'intervento da soli.
- Prova il QR con un telefono.
- Dai al relatore anche il file `--offline` e digli di provarlo una volta sul computer dell'evento, a schermo intero (F11, oppure Ctrl+Cmd+F su Mac).
