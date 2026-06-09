import requests
from bs4 import BeautifulSoup

class WikiScraper:

    def __init__(self, tema):
        self.tema = tema
        self.url = f"https://es.wikipedia.org/wiki/{tema}"

    def obtener_contenido(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        respuesta = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(respuesta.text, "html.parser")

        elemento_titulo = soup.find(id="firstHeading")
        titulo = elemento_titulo.text if elemento_titulo else "Sin título"

        parrafos = [p.get_text() for p in soup.find_all("p")[:5]]

        return titulo, parrafos