import json
import tkinter as tk
from tkinter import ttk
import pyperclip

with open("data/data.json", 'r') as file:
        json_data = json.load(file)
        datos = json_data["datos"]


def obtener_valores_unicos(self, datos, clave):
        return list(set(d[clave] for d in datos))

def obtener_selecciones(self ,event):
        seleccion_lenguaje = self.combo_lenguaje.get()
        seleccion_accion = self.combo_accion.get()


        for elementos in datos:
                if elementos['lenguaje'] == seleccion_lenguaje and elementos['accion'] == seleccion_accion:
                        codigo = elementos['codigo']

                        lenguaje = elementos['lenguaje']
                        accion = elementos['accion']
                        comentario = elementos['comentario']


                        self.resultado_texto.config(state="normal")  # Habilitar la edición
                        self.resultado_texto.delete(1.0, tk.END)  # Limpiar el contenido actual
                        self.resultado_texto.insert(tk.END, codigo)  # Insertar el nuevo contenido
                        self.resultado_texto.config(state="disabled")  # Volver a deshabilitar la edición



def copiar_al_portapapeles(self):
        contenido = self.resultado_texto.get("1.0", tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(contenido)
        self.root.update()




def Actualizar_dato():
        with open("data/data.json", 'r') as file:
                datos = json.load(file)
                datos = datos["datos"]
                return datos