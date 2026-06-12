import requests
import os
from dotenv import load_dotenv
from config import GROQ_URL, GROQ_MODEL

load_dotenv()

class Enricher:

    def __init__(self):
        self._api_key = os.getenv("GROQ_API_KEY")
        if not self._api_key:
            raise ValueError("Error: no se encontró la API key")
        self.url = GROQ_URL
        self._headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json"
        }

    def enriquecer(self, titulo, parrafos):
        if not titulo or not parrafos:
            print("Error: el texto está vacío")
            return None
        texto_original = f"{titulo}\n\n" + "\n".join(parrafos)
        datos = {
            "model": GROQ_MODEL,
            "max_tokens": 1024,
            "messages": [
                {"role": "user", "content": f"Mejora este texto de Wikipedia: {texto_original}"}
            ]
        }

        try:
            respuesta = requests.post(self.url, headers=self._headers, json=datos, timeout=10)
            respuesta.raise_for_status()
            resultado = respuesta.json()
            choices = resultado.get('choices', [])
            if not choices:
                print("Error: respuesta vacía de la API")
                return texto_original
            return choices[0]['message']['content']

        except requests.exceptions.ConnectionError:
            print("Error: no hay conexión a internet")
            return texto_original

        except requests.exceptions.Timeout:
            print("Error: la API tardó demasiado en responder")
            return texto_original

        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP: {e}")
            return texto_original

        except Exception as e:
            print(f"Error inesperado: {e}")
            return texto_original