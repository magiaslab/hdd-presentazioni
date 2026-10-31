# Crea il modello PowerPoint HDD (16:9). Serve python-pptx.
#   python3 crea_pptx.py
# Il file si apre anche in Keynote e in Google Slides (File › Importa).
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

qui = os.path.dirname(os.path.abspath(__file__))
C = {k: RGBColor.from_string(v) for k, v in {
    'nebbia': 'E6EAEE', 'inchiostro': '14181D', 'sec': '4A525C', 'accento': '123A5C',
    'fascia': '15191D', 'fascia_t': 'EEF1F4', 'fascia_s': 'A3AEBA', 'riga_s': '2B3239', 'riga': 'D5DBE2',
    'lav': 'A9ACD6', 'lime': 'D4EB86', 'cipria': 'EBDDD7', 'az': '7793C2', 'carta': 'FBFCFD', 'allarme': 'A8361F'}.items()}
TESTO, SEGUITO = 'Switzer', 'Newsreader'
SFONDI = {'chiaro': ('nebbia', 'inchiostro', 'sec', 'accento'), 'rosa': ('cipria', 'inchiostro', 'sec', 'accento'),
          'scura': ('fascia', 'fascia_t', 'fascia_s', 'lav'), 'blu': ('accento', 'fascia_t', 'fascia_s', 'lime')}

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
W, H = prs.slide_width, prs.slide_height
M = Inches(0.8)
vuoto = prs.slide_layouts[6]

def slide(sfondo):
    s = prs.slides.add_slide(vuoto)
    s.background.fill.solid(); s.background.fill.fore_color.rgb = C[SFONDI[sfondo][0]]
    s._tono = SFONDI[sfondo]
    return s

def scrivi(s, x, y, w, h, righe, ancora=MSO_ANCHOR.TOP):
    """righe: lista di (testo, dimensione, colore, font, corsivo, grassetto)"""
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = ancora
    for m in ('margin_left', 'margin_right', 'margin_top', 'margin_bottom'): setattr(tf, m, 0)
    for i, (t, dim, col, font, corsivo, grassetto) in enumerate(righe):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.05 if dim >= 28 else 1.35
        r = p.add_run(); r.text = t
        r.font.size = Pt(dim); r.font.color.rgb = C[col]; r.font.name = font; r.font.italic = corsivo; r.font.bold = grassetto
    return tb

def occhiello(s, y, t):
    scrivi(s, M, y, W - 2 * M, Inches(.4), [(t.upper(), 12, s._tono[2], TESTO, False, False)])

def titolo(s, y, t, seguito, w=None, dim=44):
    scrivi(s, M, y, w or W - 2 * M, Inches(2.4), [(t, dim, s._tono[1], TESTO, False, False), (seguito, dim, s._tono[3], SEGUITO, True, False)])

def testo(s, x, y, w, t, dim=18):
    scrivi(s, x, y, w, Inches(1.5), [(t, dim, s._tono[2], TESTO, False, False)])

def rett(s, x, y, w, h, col, forma=MSO_SHAPE.RECTANGLE):
    r = s.shapes.add_shape(forma, x, y, w, h); r.fill.solid(); r.fill.fore_color.rgb = C[col]; r.line.fill.background()
    r.shadow.inherit = False
    if forma == MSO_SHAPE.ROUNDED_RECTANGLE: r.adjustments[0] = 0.12
    return r

def barre(s, x, base, scala=1.0):
    # le barre del logo HDD
    dati = [(370, 'fascia_t'), (285, 'fascia_t'), (413, 'fascia_t'), (467, 'lav'), (338, 'lime'), (497, 'cipria'),
            (305, 'fascia_t'), (512, 'az'), (357, 'fascia_t'), (430, 'fascia_t'), (353, 'fascia_t'), (341, 'fascia_t')]
    for i, (h, col) in enumerate(dati):
        hh = Emu(int(Inches(h / 100) * scala * .9))
        rett(s, x + Emu(int(Inches(.33) * scala * i)), base - hh, Emu(int(Inches(.09) * scala)), hh, col)

def logo(s, x, y, h, scuro=True):
    s.shapes.add_picture(os.path.join(qui, 'logo-hdd-su-%s.png' % ('scuro' if scuro else 'chiaro')), x, y, height=h)

def nota(s, t):
    s.notes_slide.notes_text_frame.text = t

# 1 copertina
s = slide('scura')
barre(s, W - Inches(4.2), H, 0.75)
logo(s, M, Inches(.8), Inches(.55))
occhiello(s, Inches(2.2), 'Nome dell’evento · Luogo · data')
titolo(s, Inches(2.65), 'Il titolo dell’intervento', 'e la seconda riga in corsivo', w=Inches(8.5), dim=48)
testo(s, M, Inches(5.6), Inches(8), 'Nome Cognome · Hotel Digital Distribution')
nota(s, 'Copertina. Il titolo è breve; la seconda riga in corsivo porta il punto di vista.')

# 2 divisorio
s = slide('rosa')
occhiello(s, Inches(2.2), 'Prima parte')
titolo(s, Inches(2.65), 'Il nome del capitolo.', 'Cosa vedremo, in una frase.', dim=56)
testo(s, M, Inches(5.3), Inches(8), 'Una riga che spiega perché questa parte conta per chi è in sala.')
nota(s, 'Divisorio: apre ogni capitolo.')

# 3 immagine + concetto
s = slide('chiaro')
img = rett(s, M, Inches(1.2), Inches(6.2), Inches(4.6), 'carta', MSO_SHAPE.ROUNDED_RECTANGLE)
img.line.color.rgb = C['riga']
scrivi(s, M, Inches(3.2), Inches(6.2), Inches(.6), [('Trascina qui la schermata o la foto', 16, 'sec', TESTO, False, False)]).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
scrivi(s, M, Inches(6.05), Inches(6.2), Inches(.4), [('RICOSTRUZIONE  ·  Da dove vengono i dati, con la data.', 11, 'sec', TESTO, False, False)])
titolo(s, Inches(1.4), 'Il concetto in una frase.', 'La conseguenza, in corsivo.', w=Inches(5.2), dim=36)
s.shapes[-1].left = Inches(7.4)
testo(s, Inches(7.4), Inches(3.9), Inches(5.1), 'Due o tre righe al massimo. Il resto si dice a voce.')
nota(s, 'Schermata a sinistra, concetto a destra. Le schermate rifatte portano «Ricostruzione», le catture vere «Vero».')

# 4 numeri grandi
s = slide('scura')
occhiello(s, Inches(1.3), 'Cosa è successo')
titolo(s, Inches(1.7), 'Un risultato.', 'La seconda riga.')
for i, (n, t) in enumerate([('120', 'cosa misura il primo numero'), ('35', 'cosa misura il secondo numero')]):
    x = M + Inches(5.6) * i
    rett(s, x, Inches(4.2), Inches(5), Emu(9525), 'riga_s')
    scrivi(s, x, Inches(4.4), Inches(5), Inches(1.4), [(n, 72, 'lime', TESTO, False, False), (t, 16, 'fascia_s', TESTO, False, False)])
scrivi(s, M, Inches(6.6), Inches(10), Inches(.4), [('Periodo, fonte e cosa non è ancora misurato.', 11, 'fascia_s', TESTO, False, False)])
nota(s, 'Uno o due numeri misurati, ognuno con fonte e data.')

# 5 frase da ricordare
s = slide('rosa')
scrivi(s, M, Inches(1.8), Inches(10.5), Inches(3.2), [('Una frase sola, quella che vuoi che la sala si porti a casa.', 54, 'inchiostro', SEGUITO, True, False)], MSO_ANCHOR.MIDDLE)
nota(s, 'La frase chiave, da sola.')

# 6 barre orizzontali
s = slide('chiaro')
occhiello(s, Inches(1.1), 'Da dove arriva')
titolo(s, Inches(1.5), 'Un dato a barre.', 'Si legge da lontano.')
voci = [('Voce A', .45, 'inchiostro'), ('Voce B', .30, 'az'), ('Voce C', .20, 'lav'), ('Voce D', .05, 'allarme')]
for i, (n, v, col) in enumerate(voci):
    y = Inches(3.9) + Inches(.62) * i
    scrivi(s, M, y - Inches(.08), Inches(2.6), Inches(.4), [(n, 16, 'inchiostro', TESTO, False, False)])
    rett(s, M + Inches(2.8), y, Inches(8.3), Inches(.16), 'riga', MSO_SHAPE.ROUNDED_RECTANGLE)
    rett(s, M + Inches(2.8), y, Emu(int(Inches(8.3) * v / .45 * .95)), Inches(.16), col, MSO_SHAPE.ROUNDED_RECTANGLE)
    scrivi(s, W - M - Inches(.8), y - Inches(.08), Inches(.8), Inches(.4), [('%d%%' % round(v * 100), 16, 'inchiostro', TESTO, False, True)])
scrivi(s, M, Inches(6.6), Inches(10), Inches(.4), [('Fonte e data.', 11, 'sec', TESTO, False, False)])
nota(s, 'Barre: la voce più grande arriva quasi in fondo, le altre in proporzione.')

# 7 tabella di confronto
s = slide('scura')
titolo(s, Inches(1.1), 'Due modi a confronto.', 'Uno lo decidi tu.')
col_x = [M, M + Inches(3.2), M + Inches(7.3)]
for j, t in enumerate(['', 'COM’È', 'COME PUÒ ESSERE']):
    scrivi(s, col_x[j], Inches(3.4), Inches(4), Inches(.4), [(t, 12, 'lime' if j == 2 else 'fascia_s', TESTO, False, False)])
for i in range(3):
    y = Inches(3.9) + Inches(.85) * i
    rett(s, M, y, W - 2 * M, Emu(9525), 'riga_s')
    for j, (t, col, b) in enumerate([('Aspetto %d' % (i + 1), 'fascia_t', True), ('La situazione di partenza.', 'fascia_s', False), ('Quello che cambia.', 'fascia_t', False)]):
        scrivi(s, col_x[j], y + Inches(.2), Inches(3.9), Inches(.6), [(t, 17, col, TESTO, False, b)])
nota(s, 'Tabella: la terza colonna è quella buona.')

# 8 tre colonne
s = slide('blu')
occhiello(s, Inches(1.1), 'Come lavoriamo')
titolo(s, Inches(1.5), 'Tre cose da guardare.', 'In quest’ordine.')
for i, t in enumerate(['Uno', 'Due', 'Tre']):
    x = M + Inches(3.95) * i
    rett(s, x, Inches(3.9), Inches(3.5), Emu(9525), 'riga_s')
    scrivi(s, x, Inches(4.1), Inches(3.5), Inches(2), [(t.upper(), 12, 'lime', TESTO, False, True), ('Il %s punto' % ['primo', 'secondo', 'terzo'][i], 24, 'fascia_t', TESTO, False, False), ('Due righe che lo spiegano con un esempio vero.', 16, 'fascia_s', TESTO, False, False)])
nota(s, 'Un metodo in tre punti.')

# 9 cinque azioni
s = slide('rosa')
occhiello(s, Inches(1.1), 'Azioni')
titolo(s, Inches(1.5), 'Cinque cose da fare.', 'La seconda riga.')
for i in range(5):
    x = M + Inches(2.36) * i
    rett(s, x, Inches(3.9), Inches(2.2), Inches(2.4), 'carta', MSO_SHAPE.ROUNDED_RECTANGLE)
    scrivi(s, x + Inches(.25), Inches(4.1), Inches(1.8), Inches(2), [(str(i + 1), 36, 'accento', SEGUITO, True, False), ('Una prova che si fa dal telefono.', 15, 'inchiostro', TESTO, False, False)])
nota(s, 'Cose pratiche da fare dopo l’intervento.')

# 10 a tutta foto
s = slide('scura')
ph = rett(s, 0, 0, W, H, 'riga_s')
scrivi(s, Inches(4), Inches(.5), Inches(8.8), Inches(.5), [('Metti qui la foto a tutta pagina (almeno 1920 px), poi «Porta in secondo piano».', 13, 'fascia_s', TESTO, False, False)])
velo = rett(s, 0, 0, Inches(8), H, 'fascia')
velo.fill.fore_color.rgb = C['fascia']
from pptx.oxml.ns import qn
sf = velo.fill._xPr.find(qn('a:solidFill'))[0]
alpha = sf.makeelement(qn('a:alpha'), {'val': '70000'}); sf.append(alpha)
scrivi(s, M, Inches(3.4), Inches(9), Inches(2.6), [('La premessa, piccola.', 24, 'fascia_s', TESTO, False, False), ('La frase che emoziona.', 60, 'fascia_t', SEGUITO, True, False)])
nota(s, 'Il momento emotivo: una foto sola, una frase.')

# 11 invito con QR
s = slide('blu')
occhiello(s, Inches(2), 'Dopo l’intervento')
titolo(s, Inches(2.4), 'L’invito alla sala.', 'Parliamone.', w=Inches(7))
testo(s, M, Inches(4.8), Inches(6.5), 'Cosa può fare chi vuole approfondire, e dove trovarci.')
q = rett(s, Inches(8.9), Inches(1.8), Inches(3.6), Inches(3.6), 'carta', MSO_SHAPE.ROUNDED_RECTANGLE)
scrivi(s, Inches(8.9), Inches(3.4), Inches(3.6), Inches(.5), [('Incolla qui il QR', 14, 'sec', TESTO, False, False)]).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
scrivi(s, Inches(8.9), Inches(5.6), Inches(3.6), Inches(.4), [('hoteldigitaldistribution.it/contatti', 12, 'fascia_s', TESTO, False, False)]).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
nota(s, 'Il QR si crea gratis online; metti nell’indirizzo i parametri UTM dell’evento per vederlo in Analytics.')

# 12 grazie
s = slide('scura')
barre(s, W - Inches(4.2), H, 0.75)
scrivi(s, M, Inches(1.8), Inches(8), Inches(2), [('Grazie.', 120, 'lav', SEGUITO, True, False)])
testo(s, M, Inches(4.4), Inches(7), 'Nome Cognome · Hotel Digital Distribution')
logo(s, M, Inches(5.5), Inches(.55))
nota(s, 'Chiusura.')

dest = os.path.join(qui, 'modello-hdd.pptx')
prs.save(dest)
print(dest)
