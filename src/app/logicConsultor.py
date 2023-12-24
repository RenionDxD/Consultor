import json
import tkinter as tk
from tkinter import ttk


with open("Consultor/data/data.json", 'r') as file:
        datos = json.load(file)
        datos = datos["datos"]


def obtener_valores_unicos(self, datos, clave):
        return list(set(d[clave] for d in datos))
