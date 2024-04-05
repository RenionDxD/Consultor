from tabulate import tabulate
import csv
import pandas as pd
import nltk
#from nltk.corpus import stopwords
import unicodedata
from unidecode import unidecode
import joblib
import json
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
#nltk.download('stopwords')
#nltk.download('punkt')





def guardar_limpiar():
    with open("data/data.json", 'r') as file:
                datos = json.load(file)

    ids = [item["id"] for item in datos["datos"]]
    etiquetas = [item["Etiquetas"] for item in datos["datos"]]

    lista_etiquetas_con_id = [(id_, etiqueta) for id_, etiquetas in zip(ids, etiquetas) for etiqueta in etiquetas]

    # Ruta del archivo CSV
    ruta_archivo_csv = "data/datos_entrenamiento.csv"

    # Escribir los datos en el archivo CSV
    with open(ruta_archivo_csv, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir encabezados
        escritor_csv.writerow(["ID", "Etiqueta"])
        
        # Escribir datos
        for id_, etiqueta in lista_etiquetas_con_id:
            escritor_csv.writerow([id_, etiqueta])

def limpieza():
      data = pd.read_csv('data/datos_entrenamiento.csv')
      columnas_a_limpiar = ['Etiqueta']
      for columna in columnas_a_limpiar:
                data[columna] = data[columna].apply(limpiar_texto)
      data.to_csv('data/texto_procesado.csv', index=False)


def crear_modelos_cercania():
    try:
        df = pd.read_csv('data/datos_entrenamiento.csv')
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        tfidf_vectorizer.fit_transform(df['Etiqueta'])
        joblib.dump(tfidf_vectorizer, "data/vectorizador.pkl")
        X_train_tfidf = tfidf_vectorizer.fit_transform(df['Etiqueta'])
        nbrs = NearestNeighbors(n_neighbors=5, algorithm='auto').fit(X_train_tfidf)
        joblib.dump(nbrs, 'data/modelo_nbrs.pkl')
        
        return True,"El proceso de creacion de vectores de cercania ha sido exitoso"
    except:
        return False,"Error: El proceso de creacion de vectores de cercania ha fallado, verificar la columna Etiqueta"



def limpiar_texto(text):
    """
    Limpia el texto eliminando stopwords y acentos.

    Args:
        text (str): El texto a limpiar.

    Returns:
        str: El texto limpio.
    """

    palabras_minusculas = nltk.word_tokenize(text.lower(),'spanish')  # Convertir a minúsculas
   
    # Reconstruir el texto limpio
    texto_limpio = unidecode(' '.join(palabras_minusculas))
    
    return texto_limpio