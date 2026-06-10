from scraper import WikiScraper

scraper = WikiScraper("Python")
titulo, parrafos = scraper.obtener_contenido()
print(titulo)
for parrafo in parrafos:
    print(parrafo)
