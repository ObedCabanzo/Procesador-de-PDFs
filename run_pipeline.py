import os
import subprocess
import sys

data_dir = sys.argv[1] if len(sys.argv) > 1 else 'data'

scripts = [
    f"python pdf_to_markdown.py --data_dir {data_dir}",
    f"python process_markdown.py --data_dir {data_dir}",
    f"python analyze_output.py --data_dir {data_dir}",
    f"python split_into_chunks.py --data_dir {data_dir}"
]

for script in scripts:
    print("----------------------------------------")
    print(f"Ejecutando: {script}")
    print("----------------------------------------\n\n")
    
    try:
        subprocess.run(script, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {script}: {e}")
        break
else:
    print("Todos los scripts han sido ejecutados exitosamente.\n\n")