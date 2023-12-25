import tkinter as tk
import json
from datetime import datetime


def registrar_codigo(self):
        codigo = self.codigo_text.get("1.0", "end-1c")
        print("Código de pantalla 2 copiado al portapapeles.")

        lenguaje = self.combo_lenguaje.get()
        accion = self.entry_accion.get()
        comentario = self.entry_comentario.get()
        contenido_texto = self.codigo_text.get("1.0", tk.END)

        with open("Consultor/data/data.json", 'r') as file:
            datos = json.load(file)
           
        fecha_actual = datetime.now()


        nuevo_elemento = {
            "favoitos":False,
            "lenguaje": lenguaje,
            "accion": accion,
            "dependencias": "",
            "comentario": comentario,
            "codigo": contenido_texto,
            "estadistica":0,
            "fecha":fecha_actual.strftime("%Y-%m-%d")
        }
        datos["datos"].append(nuevo_elemento)

        # Escribir la estructura de datos actualizada en el archivo JSON
        with open("Consultor/data/data.json", 'w') as file:
            json.dump(datos, file, indent=2)

        

        # Limpiar el contenido actual del widget Text
        self.codigo_text.delete("1.0", tk.END)

        # Insertar el nuevo texto en el widget Text
        #self.codigo_text.insert("1.0", texto_a_mostrar)
        self.combo_lenguaje.set("Seleccionar Lenguaje")
        self.entry_accion.delete(0, tk.END)
        self.entry_comentario.delete(0, tk.END)
        self.codigo_text.delete("1.0", tk.END)
        
