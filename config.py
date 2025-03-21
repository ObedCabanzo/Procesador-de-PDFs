import os
import argparse

def get_config():
    parser = argparse.ArgumentParser(description='Procesamiento de documentos.')
    parser.add_argument('--data_dir', type=str, default='data', help='Directorio de trabajo (data o test)')
    args = parser.parse_args()
    
    DATA_DIR = args.data_dir
    
    config = {
        'DATA_DIR': DATA_DIR,
        'PRE_INPUT_DIRECTORY': os.path.join(DATA_DIR, 'input/raw/'),
        'PRE_OUTPUT_DIRECTORY': os.path.join(DATA_DIR, 'input/markdown'),
        'INPUT_PATH': os.path.join(DATA_DIR, 'input/markdown'),
        'OUTPUT_PATH': os.path.join(DATA_DIR, 'output'),
        'BANEADOS_FILE': os.path.join(DATA_DIR, 'baneados.json'),
        'ARCHIVOS_PROCESADOS': os.path.join(DATA_DIR, 'procesados.json'),
        'CARPETA_DESTINO': os.path.join(DATA_DIR, 'chunks')
    }
    
    return config