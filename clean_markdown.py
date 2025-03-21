import re
import os


def eliminar_tablas(texto):
    # Eliminar líneas que contengan tablas en formato Markdown y que incluyan "table" en asteriscos o numerales
    texto_sin_tablas = re.sub(r'^\|.*\|\s*$', '', texto, flags=re.MULTILINE)  # Elimina líneas de tablas
    texto_sin_tablas = re.sub(r'(^|\s)(\*+|#+)\s*.*\s*table\s*(\*+|#+)(\s|$)', '', texto_sin_tablas, flags=re.IGNORECASE)
    return texto_sin_tablas

def remove_fig_table_titles_regex(md_text):
    # Expresión regular para encontrar líneas que comienzan con "table", "fig." o "Figure", incluyendo variantes con negritas (**) y encabezados (#)
    cleaned_text = re.sub(r'^\s*(\#|\*\*|\*)?\s*(TABLE|FIGURE|fig\.\s*|figure)\s+\d+.*(\*\*|\*)?\s*$', '', md_text, flags=re.IGNORECASE | re.MULTILINE)
    return cleaned_text.strip()

def eliminar_citaciones(texto):
    # Eliminar citaciones de tipo (Nombre Apellido, Año) o (Nombre Apellido et al., Año)
    texto_sin_citaciones = re.sub(r'\(\s*(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:\s+et al\.)?,?\s*\d{4}(?:[a-z]?)?)\s*(?:;\s*(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:\s+et al\.)?,?\s*\d{4}(?:[a-z]?)?)\s*)*\)', '', texto)
    
    # Eliminar citaciones de tipo [Número] (Ej: [1], [12], [123])
    texto_sin_citaciones = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', texto_sin_citaciones)
    
    # Eliminar citaciones de tipo [Número1 - Número2] (Ej: [1-3], [12-15])
    texto_sin_citaciones = re.sub(r'\[\d+\s*-\s*\d+\]', '', texto_sin_citaciones)
    
    # Eliminar citas con varios autores: (Nombre Apellido, Nombre Apellido, y Nombre Apellido, Año)
    texto_sin_citaciones = re.sub(r'\(\s*(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:,\s*)?)+\s*(?:y\s*)?[A-Z][a-z]+(?:\s+et al\.)?\s*,\s*\d{4}\s*\)', '', texto_sin_citaciones)

    # Eliminar citaciones de la forma .número o .número1, número2
    texto_sin_citaciones = re.sub(r'\.\d+(?:,\d+)?', '', texto_sin_citaciones)  # .38, .34, .38,57

    return texto_sin_citaciones



def eliminar_referencias(texto):
    # Eliminar todo el contenido después de un título "References" hasta el siguiente título
    texto_sin_referencias = re.sub(r'(?i)(#+\s*references\s*.*\n)([\s\S]*?)(?=#+|$)', '', texto)
    return texto_sin_referencias

def eliminar_secciones_no_deseadas(texto):
    # Eliminar todo el contenido después de los títulos mencionados hasta el siguiente título
    texto_sin_secciones = re.sub(
        r'(?i)(#+\s*(\d+\.|[IVXLCDM]+\.)?\s*(correspondence|funding information|conflict of interest|acknowledgements?|acknowledgment)\s*.*\n)([\s\S]*?)(?=#+|$)',
        '',
        texto
    )
    return texto_sin_secciones

def eliminar_lineas_vacias(texto):
    # Dividir el texto en líneas y eliminar las vacías
    lineas = texto.splitlines()
    lineas_no_vacias = [linea for linea in lineas if linea.strip()]
    
    # Unir nuevamente las líneas no vacías en un solo string
    texto_limpio = "\n".join(lineas_no_vacias)
    
    return texto_limpio

def procesar_archivo_md(texto):
    # Aplicar las funciones en orden
    texto = eliminar_tablas(texto)
    texto = remove_fig_table_titles_regex(texto)
    texto = eliminar_citaciones(texto)
    texto = eliminar_referencias(texto)
    texto = eliminar_secciones_no_deseadas(texto)
    texto = eliminar_lineas_vacias(texto)
    
    return texto


def procesar_md_pipeline(ruta_archivo_md, directorio_salida):
    # Leer el archivo markdown
    with open(ruta_archivo_md, 'r', encoding='utf-8') as file:
        texto_md = file.read()
    
    # Procesar el archivo usando el pipeline de funciones
    texto_procesado = procesar_archivo_md(texto_md)
    
    # Obtener el nombre del archivo sin la extensión
    nombre_archivo = os.path.basename(ruta_archivo_md).replace('.md', '.txt')
    
    # Crear el directorio de salida si no existe
    os.makedirs(directorio_salida, exist_ok=True)
    
    # Guardar el archivo procesado en el directorio de salida
    ruta_salida = os.path.join(directorio_salida, nombre_archivo)
    with open(ruta_salida, 'w', encoding='utf-8') as file:
        file.write(texto_procesado)
    
    print(f'Archivo procesado guardado en: {ruta_salida}')
