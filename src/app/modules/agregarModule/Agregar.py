import tkinter as tk
from tkinter import ttk
import json
from tkinter import *


ColorBgConstant = "#21201c"
ColorLetterConstant = "#da6b16"
BorderColor = "#da6b16"
font = "Fixedsys"

class Agregar(tk.Frame):
    from modules.agregarModule.logicAgregar import registrar_codigo
    def __init__(self, root):
        super().__init__(root)
        self.configure(bg=ColorBgConstant)



        border_color = Frame(self, background=BorderColor)
        border_color.pack(side="left", fill="y")
        
         # Panel que muestra la información
        self.panel_izquierdo = tk.Frame(border_color, width=1, bg=ColorBgConstant,bd=1, relief="solid")
        self.panel_izquierdo.pack(side="left", fill="y",padx=2, pady=2)
        


        # Combobox para seleccionar el lenguaje
        self.label_lenguaje = tk.Label(self.panel_izquierdo,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Lenguaje:")
        self.label_lenguaje.pack(side="top", pady=5)
        self.combo_lenguaje = ttk.Combobox(self.panel_izquierdo, foreground=ColorLetterConstant, background=ColorBgConstant, font=("Fixedsys", 10), values=["Python", "Java", "C++", "JavaScript", "PHP", "CSS", "C#", "HTML","ASPX","SQL","JSON"], state="readonly")
        self.combo_lenguaje.pack(side="top",  padx=1, pady=10)

        # Campo de entrada para la acción
        self.label_accion = tk.Label(self.panel_izquierdo,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Acción:")
        self.label_accion.pack(side="top", pady=5)
        self.entry_accion = tk.Entry(self.panel_izquierdo, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), width=30)
        self.entry_accion.pack(side="top",  padx=1, pady=10)

        # Campo de entrada para comentario
        self.label_comentario = tk.Label(self.panel_izquierdo,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Comentario:")
        self.label_comentario.pack(side="top", pady=5)
        self.entry_comentario = tk.Entry(self.panel_izquierdo, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), width=30)
        self.entry_comentario.pack(side="top",  padx=1, pady=10)

        self.label_Etiqueta = tk.Label(self.panel_izquierdo,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Etiquetas:")
        self.label_Etiqueta.pack(side="top", pady=5)
        self.label_Etiqueta = tk.Text(self.panel_izquierdo, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), width=30,height=10)
        self.label_Etiqueta.pack(side="top",  padx=1, pady=10)


        

        # Botón para registrar el código
        self.registrar_boton = tk.Button(self, text="Registrar Código",background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, command=self.registrar_codigo)
        self.registrar_boton.pack(pady=5)

        
        
        # Widget Text para mostrar el código en pantalla 2
        self.codigo_text = tk.Text(self, wrap="none",background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), height=20, width=45)
        self.codigo_text.insert("1.0", "")
        self.codigo_text.pack(padx=35, pady=20)


        self.etiqueta_info = tk.Label(self,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="")
        self.etiqueta_info.pack(padx=20, pady=10)








    