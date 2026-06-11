import requests
from bs4 import BeautifulSoup
from config import WIKIPEDIA_URL, HEADERS

class Scraper:

    def __init__(self, tema):
        self.tema = tema
        self.url = f"{WIKIPEDIA_URL}{tema}"

    def obtener_contenido(self):
        try:
            respuesta = requests.get(self.url, headers=HEADERS)
            soup = BeautifulSoup(respuesta.text, "html.parser")

            elemento_titulo = soup.find(id="firstHeading")
            titulo = elemento_titulo.text if elemento_titulo else "Sin título"

            parrafos = [p.get_text() for p in soup.find_all("p")[:5]]

            return titulo, parrafos

        except requests.exceptions.ConnectionError:
            print("Error: no hay conexión a internet")
            return None, None

        except requests.exceptions.Timeout:
            print("Error: Wikipedia tardó demasiado en responder")
            return None, None

        except Exception as e:
            print(f"Error inesperado: {e}")
            return None, None