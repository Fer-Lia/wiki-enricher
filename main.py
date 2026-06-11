from scraper import WikiScraper

tema = input("¿Qué tema quieres buscar? ")
scraper = WikiScraper(tema)
titulo, parrafos = scraper.obtener_contenido()
print(titulo)
for parrafo in parrafos:
    print(parrafo)
