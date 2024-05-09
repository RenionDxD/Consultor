import json
import tkinter as tk
from tkinter import ttk


with open("data/data.json", 'r') as file:
        datos = json.load(file)
        datos = datos["datos"]






def obtener_valores_unicos(self, datos, clave):
        return list(set(d[clave] for d in datos))


def guardar_nota(self, event):
        # Obtener el contenido del campo de texto
    contenido = self.notas_text.get("1.0", "end-1c")  # Obtiene todo el texto menos el último salto de línea
    # Guardar el contenido en un archivo de texto
    with open("data/notas.txt", "w") as archivo:
        archivo.write(contenido)


