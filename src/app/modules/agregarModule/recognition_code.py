import joblib
from keras import models
import numpy as np
import tensorflow as tf
import warnings
from sklearn.exceptions import InconsistentVersionWarning
from joblib import load

# Ignorar todas las advertencias de scikit-learn
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

def tokenizeVec(sentence):
        tokens = sentence.split()
        return tokens

def recognition_code(codigo):

    real_vectorizer = load('data/VectorizadorCoderecognition.pkl')
    modelo = models.load_model('data/SuperIntendenteCodeRecognition.h5')

    vectors = real_vectorizer.transform([codigo]).toarray()

    prediccion = modelo.predict(vectors)
    

    indice_maximo = np.argmax(prediccion)

    # Usando instrucciones if para imprimir el resultado según el índice máximo
    if indice_maximo == 0:
        return 'ASPX'
    elif indice_maximo == 1:
        return 'C#'
    elif indice_maximo == 2:
        return 'CSS'
    elif indice_maximo == 3:
        return 'JavaScript'
    elif indice_maximo == 4:
        return 'Python'
    elif indice_maximo == 5:
        return 'SQL'



