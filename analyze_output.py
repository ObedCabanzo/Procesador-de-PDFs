import os
import statistics
import json
from config import get_config

config = get_config()

def cargar_baneados():
    if os.path.exists(config['BANEADOS_FILE']):
        with open(config['BANEADOS_FILE'], 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_baneados(baneados):
    with open(config['BANEADOS_FILE'], 'w', encoding='utf-8') as f:
        json.dump(baneados, f, ensure_ascii=False, indent=4)

def calcular_longitud_promedio_palabras(texto):
    palabras = texto.split()
    if len(palabras) == 0:
        return 0
    longitudes = [len(palabra) for palabra in palabras]
    return sum(longitudes) / len(palabras)

def calcular_iqr(data):
    q1 = statistics.quantiles(data, n=4)[0]
    q3 = statistics.quantiles(data, n=4)[2]
    return q3 - q1

def procesar_archivos():
    archivos = [f for f in os.listdir(config['OUTPUT_PATH']) if f.endswith('.txt')]
    promedios_por_archivo = []
    baneados = cargar_baneados()
    
    for archivo in archivos:
        ruta_archivo = os.path.join(config['OUTPUT_PATH'], archivo)
        
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
            promedio_longitud = calcular_longitud_promedio_palabras(texto)
            promedios_por_archivo.append(promedio_longitud)
    
    if len(promedios_por_archivo) == 0:
        print("No hay archivos para procesar.")
        return

    iqr = calcular_iqr(promedios_por_archivo)
    q1 = statistics.quantiles(promedios_por_archivo, n=4)[0]
    q3 = statistics.quantiles(promedios_por_archivo, n=4)[2]

    umbral_superior = q3 + 1.5 * iqr
    umbral_inferior = q1 - 1.5 * iqr

    print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
    print(f"Umbral superior: {umbral_superior:.2f}, Umbral inferior: {umbral_inferior:.2f}")
    print("Archivos con promedios anormales:")

    for i, promedio in enumerate(promedios_por_archivo):
        ruta_archivo = os.path.join(config['OUTPUT_PATH'], archivos[i])
        if promedio > umbral_superior or promedio < umbral_inferior:
            print(f"Eliminando archivo: {archivos[i]} - Promedio de longitud: {promedio:.2f}")
            try:
                os.remove(ruta_archivo)
                if archivos[i] not in baneados:
                    baneados.append(archivos[i])
            except FileNotFoundError:
                print(f"El archivo {archivos[i]} ya no existe.")
    
    guardar_baneados(baneados)

if __name__ == "__main__":
    print("\n")
    procesar_archivos()
    print("\n")