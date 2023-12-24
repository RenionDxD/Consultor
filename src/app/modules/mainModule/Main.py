import tkinter as tk
from tkinter import ttk
import json
from modules.mainModule.logicMain import Actualizar_dato



class Main(tk.Frame):
    from modules.mainModule.logicMain import obtener_valores_unicos, obtener_selecciones, copiar_al_portapapeles, Actualizar_dato
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        datos = Actualizar_dato()

        # Panel que muestra la información
        self.panel_izquierdo = tk.Frame(self, width=1, bg="lightgray", bd=1, relief="solid")
        self.panel_izquierdo.pack(side="left", fill="y")

        # Crear Frames para las etiquetas y Combobox
        frame_accion = tk.Frame(self.panel_izquierdo, bg="lightgray", width=30)
        frame_accion.grid(row=0, column=0, padx=1, pady=10, sticky="w")

        frame_lenguaje = tk.Frame(self.panel_izquierdo, bg="lightgray", width=30)
        frame_lenguaje.grid(row=1, column=0, padx=1, pady=10, sticky="w")

        # Etiquetas
        tk.Label(frame_accion, text="Acción:").pack(side="top")
        tk.Label(frame_lenguaje, text="Lenguaje:").pack(side="top")

        # Combo boxes
        self.combo_accion = ttk.Combobox(frame_accion, values=self.obtener_valores_unicos(datos, "accion"))
        self.combo_accion.set("Seleccionar Acción")
        self.combo_accion.pack(side="left")
        self.combo_accion.bind("<<ComboboxSelected>>", self.obtener_selecciones)

        self.combo_lenguaje = ttk.Combobox(frame_lenguaje, values=self.obtener_valores_unicos(datos, "lenguaje"))
        self.combo_lenguaje.set("Seleccionar Lenguaje")
        self.combo_lenguaje.pack(side="left")
        self.combo_lenguaje.bind("<<ComboboxSelected>>", self.obtener_selecciones)




       # Contenedor para los botones en la parte superior
        self.labels_frame = tk.Frame(self)
        self.labels_frame.pack(side="top", fill="both", expand=False, padx=1, pady=1)

        # Etiqueta Accion
        self.etiqueta_accion = tk.Label(self.labels_frame, text="Accion:")
        self.etiqueta_accion.grid(row=0, column=0, padx=20, pady=1)

        # Etiqueta Comentario
        self.etiqueta_comentario = tk.Label(self.labels_frame, text="Comentario:")
        self.etiqueta_comentario.grid(row=0, column=1, padx=20, pady=1)

        # Etiqueta Fecha
        self.etiqueta_fecha = tk.Label(self.labels_frame, text="Fecha:")
        self.etiqueta_fecha.grid(row=1, column=0, padx=20, pady=1)

        # Etiqueta Veces usado
        self.etiqueta_usado = tk.Label(self.labels_frame, text="Veces usado:")
        self.etiqueta_usado.grid(row=1, column=1, padx=20, pady=1)



        # Cuadro de texto para mostrar el resultado
        self.resultado_texto = tk.Text(self, wrap="none", height=20, width=45)
        self.resultado_texto.config(state="disabled", selectbackground="gray")
        self.resultado_texto.pack(padx=20, pady=30)

        # Botón para copiar al portapapeles
        boton_copiar = ttk.Button(self, text="Copiar al Portapapeles", command=self.copiar_al_portapapeles)
        boton_copiar.pack(pady=10)



        

