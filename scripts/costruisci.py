# Costruisce la presentazione finale in un solo file HTML.
#
#   python3 -I scripts/costruisci.py mia.html finale.html            # immagini e font dentro il file
#   python3 -I scripts/costruisci.py mia.html finale.html --offline  # in più le librerie: funziona senza internet
#
# Le immagini si citano con src="img/nome.jpg" (percorso relativo al file di partenza).
# I caratteri ufficiali HDD stanno in fonts/ (famiglia-peso[-italic].woff2) e finiscono sempre dentro il file.
# Switzer non è nella repo: la prima volta lo script lo scarica da Fontshare.
import base64, mimetypes, os, re, sys

qui = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
offline = '--offline' in sys.argv
if len(args) != 2:
    sys.exit('Uso: costruisci.py partenza.html finale.html [--offline]')
src, dst = args
base = os.path.dirname(os.path.abspath(src))
s = open(src, encoding='utf-8').read()

def data_uri(percorso):
    tipo = mimetypes.guess_type(percorso)[0] or 'application/octet-stream'
    return 'data:%s;base64,%s' % (tipo, base64.b64encode(open(percorso, 'rb').read()).decode())

# immagini locali
mancanti = []
def immagine(m):
    p = os.path.join(base, m.group(2))
    if not os.path.exists(p):
        mancanti.append(m.group(2)); return m.group(0)
    return m.group(1) + data_uri(p) + m.group(3)
s = re.sub(r'(src=")((?!https?:|data:)[^"]+\.(?:jpe?g|png|webp|gif|svg))(")', immagine, s)

# font: Switzer non è nella repo (licenza Fontshare), si scarica da Fontshare la prima volta e resta in fonts/
regole = []
cartella = os.path.join(qui, 'fonts')
def scarica_switzer():
    import urllib.request
    try:
        css = urllib.request.urlopen('https://api.fontshare.com/v2/css?f[]=switzer@400,500&display=swap', timeout=15).read().decode()
        for blocco in css.split('@font-face')[1:]:
            peso = re.search(r'font-weight:\s*(\d+)', blocco).group(1)
            url = 'https:' + re.search(r"url\('(//[^']+\.woff2)'\)", blocco).group(1)
            dest = os.path.join(cartella, 'switzer-%s.woff2' % peso)
            if not os.path.exists(dest):
                open(dest, 'wb').write(urllib.request.urlopen(url, timeout=15).read())
    except Exception as e:
        print('Switzer non scaricato (%s): il testo usa il carattere di sistema.' % e)
if not os.path.exists(os.path.join(cartella, 'switzer-400.woff2')):
    scarica_switzer()
if os.path.isdir(cartella):
    for f in sorted(os.listdir(cartella)):
        m = re.match(r'([a-z-]+?)-(\d{3})(-italic)?\.woff2$', f)
        if not m: continue
        famiglia = m.group(1).replace('-', ' ').title()
        regole.append('@font-face{font-family:"%s";src:url(%s) format("woff2");font-weight:%s;font-style:%s;font-display:swap}'
                      % (famiglia, data_uri(os.path.join(cartella, f)), m.group(2), 'italic' if m.group(3) else 'normal'))
s = re.sub(r'/\*__FONT__\*/.*?/\*__FINE_FONT__\*/', lambda m: '\n'.join(regole), s, count=1, flags=re.S)

# librerie dentro il file
if offline:
    def libreria(m):
        nome = m.group(1).rsplit('/', 1)[1]
        codice = open(os.path.join(qui, 'librerie', nome), encoding='utf-8').read()
        return '<script>/* ' + nome + ' */\n' + codice.replace('</script', '<\\/script') + '\n</script>'
    s = re.sub(r'<script src="(https://[^"]+\.js)"></script>', libreria, s)

open(dst, 'w', encoding='utf-8').write(s)
print(dst, len(s) // 1024, 'KB', '· font:', len(regole), '· senza internet' if offline else '')
if mancanti:
    print('Immagini non trovate:', ', '.join(mancanti))
