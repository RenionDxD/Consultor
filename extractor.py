import glob
import os

# Carpeta de entrada y salida
carpeta_entrada = r'C:\Users\DAD\Desktop\Proyecto chat\ChatBot\controllers\services'
carpeta_salida = r'../data_blocks/python'

# Crear la carpeta de salida si no existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Buscar todos los archivos .aspx.c# en la carpeta de entrada
#archivos_csharp = glob.glob(os.path.join(carpeta_entrada, '*.aspx.cs'))
#archivos_csharp = glob.glob(os.path.join(carpeta_entrada, '*.aspx'))
archivos_csharp = glob.glob(os.path.join(carpeta_entrada, '*.python'))



# Iterar sobre cada archivo encontrado
for archivo_csharp in archivos_csharp:
    # Leer el contenido del archivo C#
    with open(archivo_csharp, 'r') as f:
        contenido = f.read()

    # Crear el nombre del archivo de salida
    nombre_archivo_salida = os.path.splitext(os.path.basename(archivo_csharp))[0] + '.txt'
    ruta_archivo_salida = os.path.join(carpeta_salida, nombre_archivo_salida)

    # Escribir el contenido en un archivo de texto en la carpeta de salida
    with open(ruta_archivo_salida, 'w') as f:
        f.write(contenido)

print("Se han guardado los archivos en la carpeta de salida.")
