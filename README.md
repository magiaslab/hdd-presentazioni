# Presentazioni HDD

Skill per Claude che prepara le presentazioni del gruppo Hotel Digital Distribution, tutte con la stessa grafica.

Si chiede a Claude, per esempio, «prepara le slide HDD per il mio intervento su…»: Claude parte dal modello, usa colori, caratteri e componenti comuni, e consegna una pagina che scorre a tutto schermo, più un file che funziona anche senza internet.

## Cosa c'è dentro

- `SKILL.md`: le istruzioni che Claude legge (regole di grafica, testi, dati, consegna).
- `modello/modello.html`: il sistema grafico completo con quindici slide di esempio, una per componente. Si apre anche da solo nel browser per vedere come sono fatte.
- `modello/img/`: immagini segnaposto degli esempi.
- `scripts/costruisci.py`: mette immagini, caratteri e, se serve, le librerie dentro un unico file.
- `librerie/`: copie delle librerie per la versione senza internet.
- `fonts/`: i caratteri ufficiali HDD. Switzer non è nella repo per la licenza Fontshare: lo script lo scarica da Fontshare la prima volta.

## Scaricare l'ultima versione

Lo zip aggiornato è sempre qui:
https://github.com/magiaslab/hdd-presentazioni/releases/latest/download/hdd-presentazioni.zip

## Come si installa in Claude

1. Apri Claude (sito o app) e vai nelle impostazioni, alla sezione delle skill.
2. Controlla che sia attiva l'esecuzione del codice: lo script che costruisce il file è in Python.
3. Carica il file `hdd-presentazioni.zip`. Quando esce una versione nuova, carica il nuovo zip al posto del vecchio.

Da lì basta scrivere, per esempio, «prepara le slide HDD per il mio intervento su…». Claude parte dal modello e consegna la presentazione come Artifact, più il file da scaricare che funziona senza internet.

Chi usa Claude Code può copiare la cartella in `~/.claude/skills/hdd-presentazioni`.

## Proporre migliorie

Chi ha un account GitHub apre una «issue» su questa pagina, oppure propone la modifica direttamente. Chi non ce l'ha scrive la proposta ad Alessandro. A ogni modifica approvata lo zip si rifà da solo e compare tra le release. Il numero di versione sta nel file `VERSION`.

Qui va solo il sistema grafico. Le presentazioni dei singoli interventi restano fuori.

## Caratteri e logo

I caratteri sono quelli del sito HDD: Switzer per il testo, Newsreader corsivo e Hanken Grotesk per il logo. Newsreader e Hanken Grotesk sono in `fonts/`. Switzer lo scarica lo script da Fontshare la prima volta: se l'ambiente non ha internet, il testo usa il carattere di sistema. Il logo SVG è nel modello e in `modello/img/`. Gli altri materiali si prendono da hoteldigitaldistribution.it.

## Librerie

GSAP, ScrollTrigger e SplitText 3.13 (licenza standard GreenSock, gratuita), Lenis 1.1.20 (MIT), three.js r128 (MIT), qrcode-generator 1.4.4 (MIT).
