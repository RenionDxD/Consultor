import tkinter as tk
from tkinter import ttk
import json



class Agregar(tk.Frame):
    from modules.agregarModule.logicAgregar import registrar_codigo
    def __init__(self, root):
        super().__init__(root)
        
         # Panel que muestra la información
        self.panel_izquierdo = tk.Frame(self, width=200, bg="lightgray")
        self.panel_izquierdo.pack(side="left", fill="y")
        


        # Combobox para seleccionar el lenguaje
        self.label_lenguaje = tk.Label(self.panel_izquierdo, text="Lenguaje:")
        self.label_lenguaje.pack(side="top", pady=5)
        self.combo_lenguaje = ttk.Combobox(self.panel_izquierdo, values=["Python", "Java", "C++", "JavaScript", "PHP", "CSS", "C#", "HTML","ASPX","SQL","JSON"], state="readonly")
        self.combo_lenguaje.pack(side="top",  padx=10, pady=5)

        # Campo de entrada para la acción
        self.label_accion = tk.Label(self.panel_izquierdo, text="Acción:")
        self.label_accion.pack(side="top", pady=5)
        self.entry_accion = tk.Entry(self.panel_izquierdo, width=30)
        self.entry_accion.pack(side="top",  padx=10, pady=5)

        # Campo de entrada para comentario
        self.label_comentario = tk.Label(self.panel_izquierdo, text="Comentario:")
        self.label_comentario.pack(side="top", pady=5)
        self.entry_comentario = tk.Entry(self.panel_izquierdo, width=30)
        self.entry_comentario.pack(side="top",  padx=10, pady=5)




        # Botón para registrar el código
        self.registrar_boton = tk.Button(self, text="Registrar Código", command=self.registrar_codigo)
        self.registrar_boton.pack(pady=5)

        
        
        # Widget Text para mostrar el código en pantalla 2
        self.codigo_text = tk.Text(self, wrap="none", height=20, width=40)
        self.codigo_text.insert("1.0", "")
        self.codigo_text.pack(padx=10, pady=10)







    