import os
import time
import json
from multiprocessing import Pool, cpu_count
from clean_markdown import procesar_md_pipeline
from config import get_config

config = get_config()

# Cargar la lista de archivos baneados desde el archivo JSON
def cargar_baneados():
    baneados_file = config['BANEADOS_FILE']
    if os.path.exists(baneados_file):
        with open(baneados_file, 'r') as f:
            # Eliminar la extensión .txt de los nombres de los archivos baneados
            return [os.path.splitext(archivo)[0] for archivo in json.load(f)]
    return []

def process_md(file_name):
    input_path_local = os.path.join(config['INPUT_PATH'], file_name)
    try:
        procesar_md_pipeline(input_path_local, config['OUTPUT_PATH'])  
    except Exception as e:
        print(f'Error procesando {file_name}: {e}')

def main():
    start_time = time.time()

    os.makedirs(config['OUTPUT_PATH'], exist_ok=True)
    
    # Cargar la lista de archivos baneados (sin extensión .txt)
    baneados = cargar_baneados()
    
    # Filtrar archivos MD que no están en la lista de baneados
    md_files = [
        f for f in os.listdir(config['INPUT_PATH'])
        if f.endswith('.md') and os.path.splitext(f)[0] not in baneados
    ]
    processed_files = {f.replace('.txt', '.md') for f in os.listdir(config['OUTPUT_PATH']) if f.endswith('.txt')}
    unprocessed_files = [f for f in md_files if f not in processed_files]
    
    if not unprocessed_files:
        print("Todos los archivos MD ya han sido procesados.")
        return
    
    num_processes = cpu_count()
    with Pool(processes=num_processes) as pool:
        pool.map(process_md, unprocessed_files)
    
    end_time = time.time() 
    elapsed_time = end_time - start_time 
    
    print(f"\n\nProcesamiento terminado. Tiempo total de ejecución: {elapsed_time:.2f} segundos\n")

if __name__ == "__main__":
    main()