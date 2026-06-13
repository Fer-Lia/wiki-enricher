import requests
from deep_translator import GoogleTranslator

class Translator:

    def __init__(self, idioma):
        if not idioma:
            raise ValueError("Error: el idioma no puede estar vacío")
        self.idioma = idioma

    def traducir(self, texto):
        if not texto:
            print("Error: el texto está vacío")
            return None

        try:
            translator = GoogleTranslator(source="auto", target=self.idioma)
            return translator.translate(texto)

        except requests.exceptions.ConnectionError:
            print("Error: no hay conexión a internet")
            return texto

        except ValueError as e:
            print(f"Error: idioma no válido → {e}")
            return None

        except Exception as e:
            print(f"Error inesperado: {e}")
            return None