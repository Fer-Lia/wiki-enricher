from scraper import Scraper
from enricher import Enricher
from translator import Translator

VERDE = "\033[92m"
RESET = "\033[0m"
ROJO = "\033[91m"
RESET = "\033[0m"

tema = input(f"{VERDE}¿Qué tema quieres buscar? {RESET}")
scraper = Scraper(tema)
titulo, parrafos = scraper.obtener_contenido()
print(titulo)
for parrafo in parrafos:
    print(parrafo)

enriquecer = input(f"{VERDE}¿Quieres enriquecer el contenido con IA? (s/n) {RESET}")
if enriquecer.lower() == "s":
    enricher = Enricher()
    texto_enriquecido = enricher.enriquecer(titulo, parrafos)
    print(texto_enriquecido)
else:
    texto_enriquecido = "\n".join(parrafos)

while True:
    traducir = input(f"{VERDE}¿A qué idioma quieres traducir? (ej: en, fr, de, it, pt) {RESET}")
    translator = Translator(traducir)
    texto_traducido = translator.traducir(texto_enriquecido)
    if texto_traducido:
        print(texto_traducido)
        break
    else:
        print(f"{ROJO}Idioma no válido, inténtalo de nuevo{RESET}")