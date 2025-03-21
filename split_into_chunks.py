import os
import re
import json
from config import get_config

config = get_config()

def dividir_en_chunks(texto, max_palabras=1500):
    parrafos = re.split(r'\.\s*\n+', texto)
    chunks = []
    chunk_actual = []
    palabras_actuales = 0

    for parrafo in parrafos:
        parrafo = parrafo.strip()
        if parrafo:
            parrafo += '.'
            palabras_parrafo = parrafo.split()
            num_palabras_parrafo = len(palabras_parrafo)

            if palabras_actuales + num_palabras_parrafo > max_palabras:
                chunks.append('\n\n'.join(chunk_actual))
                chunk_actual = []
                palabras_actuales = 0

            chunk_actual.append(parrafo)
            palabras_actuales += num_palabras_parrafo

    if chunk_actual:
        chunks.append('\n\n'.join(chunk_actual))

    return chunks

def cargar_archivos_procesados(archivo_procesados):
    if os.path.exists(archivo_procesados):
        with open(archivo_procesados, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_archivos_procesados(archivo_procesados, procesados):
    with open(archivo_procesados, 'w', encoding='utf-8') as f:
        json.dump(procesados, f, indent=4)

def procesar_archivos_txt(carpeta_origen, carpeta_destino, archivo_procesados, max_palabras=1500):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    archivos_procesados = cargar_archivos_procesados(archivo_procesados)

    for archivo in os.listdir(carpeta_origen):
        if archivo.endswith('.txt') and archivo not in archivos_procesados:
            ruta_archivo = os.path.join(carpeta_origen, archivo)

            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()

            chunks = dividir_en_chunks(contenido, max_palabras)

            nombre_base = os.path.splitext(archivo)[0]
            for i, chunk in enumerate(chunks):
                nombre_chunk = f"{nombre_base}_chunk_{i+1}.txt"
                ruta_chunk = os.path.join(carpeta_destino, nombre_chunk)
                with open(ruta_chunk, 'w', encoding='utf-8') as f:
                    f.write(chunk)

            print(f"Procesado: {archivo}, creado {len(chunks)} chunks.")
            archivos_procesados.append(archivo)

    guardar_archivos_procesados(archivo_procesados, archivos_procesados)

procesar_archivos_txt(config['OUTPUT_PATH'], config['CARPETA_DESTINO'], config['ARCHIVOS_PROCESADOS'])