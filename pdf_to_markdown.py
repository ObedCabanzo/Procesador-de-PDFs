import os
import time
from multiprocessing import Pool, cpu_count
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from config import get_config

# Cargar variables de entorno
load_dotenv()

config = get_config()

def transform_pdf(pdf_path, output_directory): 
    instructions = "Do not include in the result the following sections of pdf: images, headers, footers, figures, tables, citations, references and authors."

    parser = LlamaParse(
        result_type="markdown",
        parsing_instruction=instructions,
        user_prompt=instructions
    )

    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(input_files=[pdf_path], file_extractor=file_extractor).load_data()

    output_dir = output_directory
    text = ""
    filename = os.path.basename(pdf_path)
    
    for doc in documents:
        text += "\n\n" + doc.text

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, filename.replace(".pdf", ".md"))
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
        print(f"Markdown guardado exitosamente en {output_path}")

def pre_process_pdf(file_name):
    transform_pdf(os.path.join(config['PRE_INPUT_DIRECTORY'], file_name), config['PRE_OUTPUT_DIRECTORY'])

def main(n_files_to_process=None):
    start_time = time.time()

    os.makedirs(config['PRE_OUTPUT_DIRECTORY'], exist_ok=True)
    
    pdf_files = [f for f in os.listdir(config['PRE_INPUT_DIRECTORY']) if f.endswith('.pdf')]
    processed_files = {f.replace('.md', '.pdf') for f in os.listdir(config['PRE_OUTPUT_DIRECTORY']) if f.endswith('.md')}
    unprocessed_files = [f for f in pdf_files if f not in processed_files]
    
    if not unprocessed_files:
        print("Todos los archivos PDF ya han sido pre-procesados.\n\n")
        return

    if n_files_to_process is not None:
        unprocessed_files = unprocessed_files[:n_files_to_process]

    num_processes = min(cpu_count(), len(unprocessed_files))
    with Pool(processes=num_processes) as pool:
        pool.map(pre_process_pdf, unprocessed_files)
    
    end_time = time.time() 
    elapsed_time = end_time - start_time 
    
    print(f"\n\nPre-procesamiento terminado. Tiempo total de ejecución: {elapsed_time:.2f} segundos\n")

if __name__ == "__main__":
    main(n_files_to_process=1 if config['DATA_DIR'] == 'data' else None)