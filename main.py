from scraper import Scraper

tema = input("¿Qué tema quieres buscar? ")
scraper = Scraper(tema)
titulo, parrafos = scraper.obtener_contenido()
print(titulo)
for parrafo in parrafos:
    print(parrafo)
