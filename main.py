from scraper import Scraper
from enricher import Enricher

VERDE = "\033[92m"
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