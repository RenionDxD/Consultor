import json
import tkinter as tk
from tkinter import ttk
from modules.mainModule.Main import Main
from modules.agregarModule.Agregar import Agregar
from PIL import Image, ImageTk
from tkinter import *

ColorBgConstant = "#21201c"
ColorLetterConstant = "#da6b16"
BorderColor = "#da6b16"
font = "Fixedsys"

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultor")
        

        root.configure(bg=ColorBgConstant)

        border_color = Frame(root, background=BorderColor)
        border_color.pack(side="top", fill="both", expand=False, padx=2, pady=2)
        
        # Contenedor para los botones en la parte superior
        self.botones_frame = tk.Frame(border_color,background=ColorBgConstant)
        self.botones_frame.pack(side="top", fill="both", expand=False, padx=2, pady=2)

        # Botones para cambiar entre pantallas dentro del contenedor
        self.btn_pantalla1 = tk.Button(self.botones_frame, text="Pagina principal",background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, command=self.mostrar_pantalla1)
        self.btn_pantalla1.pack(side="left",pady=5, padx=10)

        self.btn_pantalla2 = tk.Button(self.botones_frame,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, text="Pagina Agregar codigo", command=self.mostrar_pantalla2)
        self.btn_pantalla2.pack(side="left",pady=5, padx=10)

        self.btn_pantallaTareas = tk.Button(self.botones_frame,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, text="Lista de tareas", command=self.mostrar_pantalla2)
        self.btn_pantallaTareas.pack(side="left",pady=5, padx=10)



        


        border_color = Frame(root, background=BorderColor)
        border_color.pack(side="bottom", fill="both", expand=True)

        # Panel que muestra notas
        self.panel_notas = tk.Frame(border_color, bg=ColorBgConstant, bd=1, relief="solid")
        self.panel_notas.pack(side="bottom", fill="both", expand=True,padx=2, pady=2)


        # Notas
        self.notas_text = tk.Text(self.panel_notas, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), wrap="none", height=7.5, width=85)
        self.notas_text.config(selectbackground=ColorLetterConstant)
        self.notas_text.insert("1.0", "")
        self.notas_text.pack(side="bottom", padx=5, pady=5)
        self.altura_original = self.notas_text['height']

        # Expandir notas
        self.btn_expandirNota = tk.Button(self.panel_notas, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, text="Expandir notas", command=self.expandirNotas)
        self.btn_expandirNota.pack(side="left", padx=10)
        

        # Etiqueta de notas
        self.etiqutaNota = tk.Label(self.panel_notas, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Notas:").pack(side="top",padx=30)


        # Inicializar dos pantallasS
        self.pantalla1 = Main(root)
        self.pantalla2 = Agregar(root)

        # Ocultar ambas pantallas al inicio
        self.mostrar_pantalla1()



    def mostrar_pantalla1(self):
        self.pantalla2.pack_forget()  # Ocultar pantalla 2 si está visible
        self.pantalla1.pack(expand=True)
        self.notas_text.config(height=self.altura_original)
        self.btn_expandirNota.pack(side="left", padx=10)
        #self.btn_pantalla1.destroy()  # Destruir la ventana actual

    def mostrar_pantalla2(self):
        self.pantalla1.pack_forget()  # Ocultar pantalla 1 si está visible
        self.pantalla2.pack(expand=True)
        self.notas_text.config(height=self.altura_original)
        self.btn_expandirNota.pack(side="left", padx=10)
        #self.pantalla1.destroy()
        #self.root.destroy()  # Destruir la ventana actual

    def expandirNotas(self):
        self.pantalla1.pack_forget()
        self.pantalla2.pack_forget()
        self.btn_expandirNota.pack_forget()
        nueva_altura = self.notas_text['height'] + 35
        self.notas_text.config(height=nueva_altura)
        
        

            

      
    

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()



