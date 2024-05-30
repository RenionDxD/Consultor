import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
from modules.mainModule.logicMain import Actualizar_dato

ColorBgConstant = "#21201c"
ColorLetterConstant = "#da6b16"
BorderColor = "#da6b16"
font = "Fixedsys"

class Main(tk.Frame):
    from modules.mainModule.logicMain import obtener_valores_unicos, obtener_selecciones, copiar_al_portapapeles, Actualizar_dato, obtener_seleccionesIA, cambio_de_imagen
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        # Establecer un fondo gris oscuro
        self.configure(bg=ColorBgConstant)
        
        self.cambio_de_imagen()

        with open("data/data.json", 'r') as file:
                datos = json.load(file)
                datos = datos["datos"]

        #datos = Actualizar_dato()

        border_color = Frame(self, background=BorderColor)
        border_color.pack(side="left", fill="y")

        # Panel que muestra la información
        self.panel_izquierdo = tk.Frame(border_color, width=1, bg=ColorBgConstant, bd=1, relief="solid")
        self.panel_izquierdo.pack(side="left", fill="y",padx=2, pady=2)
        

        # Crear Frames para las etiquetas y Combobox
        frame_accion = tk.Frame(self.panel_izquierdo, bg=ColorBgConstant, width=30)
        frame_accion.grid(row=1, column=0, padx=5, pady=10, sticky="w")

        frame_lenguaje = tk.Frame(self.panel_izquierdo, bg=ColorBgConstant, width=30)
        frame_lenguaje.grid(row=2, column=0, padx=5, pady=10, sticky="w")

        frame_IA = tk.Frame(self.panel_izquierdo, bg=ColorBgConstant, width=30)
        frame_IA.grid(row=0, column=0, padx=5, pady=10, sticky="w")


    
        self.icono_chico = tk.PhotoImage(file="data/Cara_1.png")
        self.icono_chico = self.icono_chico.subsample(15)
        

        # Etiquetas
        tk.Label(frame_accion,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Acción:").pack(side="top", pady=10)
        tk.Label(frame_lenguaje,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Lenguaje:").pack(side="top",pady=10)
        tk.Label(frame_IA,background=BorderColor, fg=ColorLetterConstant, font=(font, 10), image=self.icono_chico ,text="IA:").pack(side="top",pady=10)



        # Combo boxes
        self.label_ia = tk.Label(frame_IA,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10))
        self.label_ia.pack(side="left")
        self.entry_accion = tk.Entry(frame_IA, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), width=25)
        self.entry_accion.pack(side="left")
        self.entry_accion.bind("<KeyRelease>", self.obtener_seleccionesIA)


        self.combo_accion = ttk.Combobox(frame_accion, width=25, foreground=ColorLetterConstant, background=ColorBgConstant, font=("Fixedsys", 10) , values=self.obtener_valores_unicos(datos, "accion"))
        self.combo_accion.set(">> Seleccionar Acción")
        self.combo_accion.pack(side="left")
        self.combo_accion.bind("<<ComboboxSelected>>", self.obtener_selecciones)

        self.combo_lenguaje = ttk.Combobox(frame_lenguaje, width=25, foreground=ColorLetterConstant, background=ColorBgConstant, font=("Fixedsys", 10) , values=self.obtener_valores_unicos(datos, "lenguaje"))
        self.combo_lenguaje.set(">> Seleccionar Lenguaje")
        self.combo_lenguaje.pack(side="left")
        self.combo_lenguaje.bind("<<ComboboxSelected>>", self.obtener_selecciones)

        
        


       # Contenedor para los botones en la parte superior
        self.labels_frame = tk.Frame(self)
        self.labels_frame.pack(side="top", fill="both", expand=False, padx=1, pady=1)
        self.labels_frame.configure(bg=ColorBgConstant)
        

        # Etiqueta Accion
        self.etiqueta_accion = tk.Label(self.labels_frame,background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text=">> Accion:")
        self.etiqueta_accion.grid(row=0, column=0, padx=20, pady=10)

        # Etiqueta Comentario
        self.etiqueta_comentario = tk.Label(self.labels_frame, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text=">> Comentario:")
        self.etiqueta_comentario.grid(row=0, column=1, padx=20, pady=10)

        # Etiqueta Fecha
        self.etiqueta_fecha = tk.Label(self.labels_frame, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text=">> Fecha:")
        self.etiqueta_fecha.grid(row=1, column=0, padx=20, pady=1)

        # Etiqueta Veces usado
        #self.etiqueta_usado = tk.Label(self.labels_frame, background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10), text="Veces usado:")
        #self.etiqueta_usado.grid(row=1, column=1, padx=20, pady=1)



        # Cuadro de texto para mostrar el resultado
        self.resultado_texto = tk.Text(self, wrap="none",background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 8), height=20, width=55)
        self.resultado_texto.config(state="disabled", selectbackground="gray")
        self.resultado_texto.pack(padx=20, pady=30)
        
        

        # Botón para copiar al portapapeles
        self.btn_expandirNota2 = tk.Button(self, text=">> Copiar al Portapapeles <<",background=ColorBgConstant, fg=ColorLetterConstant, font=(font, 10),activeforeground=ColorBgConstant, activebackground=ColorLetterConstant, command=self.copiar_al_portapapeles)
        self.btn_expandirNota2.pack(pady=10)


        

