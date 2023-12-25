import json
import tkinter as tk
from tkinter import ttk
from modules.mainModule.Main import Main
from modules.agregarModule.Agregar import Agregar

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultor")

        # Contenedor para los botones en la parte superior
        self.botones_frame = tk.Frame(root)
        self.botones_frame.pack(side="top", fill="both", expand=False, padx=1, pady=10)

        # Botones para cambiar entre pantallas dentro del contenedor
        self.btn_pantalla1 = tk.Button(self.botones_frame, text="Pagina principal", command=self.mostrar_pantalla1)
        self.btn_pantalla1.pack(side="left", padx=10)

        self.btn_pantalla2 = tk.Button(self.botones_frame, text="Pagina Agregar codigo", command=self.mostrar_pantalla2)
        self.btn_pantalla2.pack(side="left", padx=10)

        self.btn_pantallaTareas = tk.Button(self.botones_frame, text="Lista de tareas", command=self.mostrar_pantalla2)
        self.btn_pantallaTareas.pack(side="left", padx=10)




        # Panel que muestra notas
        self.panel_notas = tk.Frame(root, bg="lightgray", bd=1, relief="solid")
        self.panel_notas.pack(side="bottom", fill="both", expand=True)


        # Notas
        self.notas_text = tk.Text(self.panel_notas, wrap="none", height=5, width=70)
        self.notas_text.config(selectbackground="green")
        self.notas_text.insert("1.0", "")
        self.notas_text.pack(side="bottom", padx=5, pady=5)
        self.altura_original = self.notas_text['height']

        # Expandir notas
        self.btn_expandirNota = tk.Button(self.panel_notas, text="Expandir notas", command=self.expandirNotas)
        self.btn_expandirNota.pack(side="left", padx=10)
        

        # Etiqueta de notas
        tk.Label(self.panel_notas, text="Notas: ").pack(side="top")

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



