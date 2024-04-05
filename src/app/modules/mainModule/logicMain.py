import json
import tkinter as tk
from tkinter import ttk
import pyperclip
import time
import joblib
import pandas as pd

#with open("Consultor/data/data.json", 'r') as file:
        #json_data = json.load(file)
        #datos = json_data["datos"]


def obtener_valores_unicos(self, datos, clave):
        return list(set(d[clave] for d in datos))


def obtener_seleccionesIA(self, event):
        accion = self.entry_accion.get()
        respuesta = verify_request(accion)
        metaData = Actualizar_dato()
        datos = metaData["datos"]
        for elementos in datos:
               if elementos['id'] == respuesta:
                        if not accion or len(accion) == 1:
                                self.etiqueta_accion.config(text=f"Accion: {""}")
                                self.etiqueta_comentario.config(text=f"Comentario: {""}")
                                self.etiqueta_fecha.config(text=f"Fecha: {""}")
                                self.etiqueta_usado.config(text=f"Veces usado: {""}")
                                self.resultado_texto.delete("1.0", tk.END)
                               
                        else:
                                codigo = elementos['codigo']

                                
                                accion = elementos['accion']
                                fecha = elementos['fecha']
                                comentario = elementos['comentario']
                                estadistica = elementos['estadistica']
                                elementos['estadistica'] = estadistica+1

                                with open("data/data.json", 'w') as file:
                                        json.dump(metaData, file, indent=2)
                                

                                # Actualizar etiquetas en la ventana principal
                                self.etiqueta_accion.config(text=f"Accion: {accion}")
                                self.etiqueta_comentario.config(text=f"Comentario: {comentario}")
                                self.etiqueta_fecha.config(text=f"Fecha: {fecha}")
                                self.etiqueta_usado.config(text=f"Veces usado: {""}")

                                


                                self.resultado_texto.config(state="normal")  # Habilitar la edición
                                self.resultado_texto.delete(1.0, tk.END)  # Limpiar el contenido actual
                                self.resultado_texto.insert(tk.END, codigo)  # Insertar el nuevo contenido
                                self.resultado_texto.config(state="disabled")  # Volver a deshabilitar la edición
        


def obtener_selecciones(self ,event):
        seleccion_lenguaje = self.combo_lenguaje.get()
        seleccion_accion = self.combo_accion.get()

        metaData = Actualizar_dato() 
        datos = metaData["datos"]
        for elementos in datos:
                if elementos['lenguaje'] == seleccion_lenguaje and elementos['accion'] == seleccion_accion:
                        codigo = elementos['codigo']

                        
                        accion = elementos['accion']
                        fecha = elementos['fecha']
                        comentario = elementos['comentario']
                        estadistica = elementos['estadistica']
                        elementos['estadistica'] = estadistica+1

                        with open("data/data.json", 'w') as file:
                                  json.dump(metaData, file, indent=2)
                        

                        # Actualizar etiquetas en la ventana principal
                        self.etiqueta_accion.config(text=f"Accion: {accion}")
                        self.etiqueta_comentario.config(text=f"Comentario: {comentario}")
                        self.etiqueta_fecha.config(text=f"Fecha: {fecha}")
                        self.etiqueta_usado.config(text=f"Veces usado: {estadistica}")

                        


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
                #datos = datos["datos"]
                return datos
        

def verify_request(pregunta):
    """
    Esta función toma una pregunta como entrada y busca respuestas similares en un conjunto de datos previamente cargado.
    
    Args:
        pregunta (str): La pregunta de entrada que se desea comparar con preguntas en el conjunto de datos.
        
    Returns:
        solucion (str): La solución correspondiente a la pregunta más similar encontrada.
        similares (list): Una lista de preguntas similares excluyendo la pregunta principal.
        """
    umbral = 0.99
    
    data_search = pd.read_csv('data/datos_entrenamiento.csv')

    # Cargar el vectorizador TF-IDF y el modelo NBRs previamente entrenados
    tfidf_vectorizer = joblib.load("data/vectorizador.pkl")
    nbrs = joblib.load("data/modelo_nbrs.pkl")
    
    
    texto_vectorizado = tfidf_vectorizer.transform([pregunta])
    
    distances, indices = nbrs.kneighbors(texto_vectorizado)
    #print(distances.min())
    
      
    try:
        similar_questions = [data_search.iloc[i]['Etiqueta'] for i in indices[0]]
        respuesta = similar_questions[0]
        fila = data_search[data_search['Etiqueta'] == respuesta]
        #print(similar_questions)
       
        if distances.min() > umbral:
            solucion = 0

        else:
            solucion = fila['ID'].values[0]
    except Exception as e:
        return "eRROR"
    
    return solucion


        
