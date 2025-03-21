# Documentación del Proyecto de Procesamiento de Documentos

Este proyecto es una aplicación diseñada para procesar archivos PDF, convertirlos a formato Markdown, limpiar el contenido, analizar la salida y dividir el texto en chunks más pequeños para su posterior uso. A continuación se detalla la descripción de la aplicación, cómo ejecutarla y qué hace cada archivo.

## Descripción de la Aplicación

La aplicación está compuesta por varios scripts que trabajan en conjunto para procesar documentos PDF. El flujo de trabajo es el siguiente:

1. **Conversión de PDF a Markdown**: Los archivos PDF se convierten a formato Markdown utilizando una herramienta externa llamada `LlamaParse`.
2. **Limpieza del Markdown**: El contenido Markdown se limpia eliminando tablas, citaciones, referencias y secciones no deseadas.
3. **Análisis de la Salida**: Se analiza la longitud promedio de las palabras en los archivos procesados y se eliminan aquellos que tienen promedios anormales.
4. **División en Chunks**: El texto limpio se divide en chunks más pequeños para facilitar su procesamiento posterior.

## Cómo Ejecutar la Aplicación

Para ejecutar la aplicación, sigue estos pasos:

1. **Clona el repositorio** (si no lo has hecho ya):
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Instala las dependencias**:
   Asegúrate de tener Python instalado y luego instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno**:
   Crea un archivo `.env` en la raíz del proyecto y añade las variables de entorno necesarias, como las credenciales para `LlamaParse`.

4. **Ejecuta el pipeline**:
   Ejecuta el script `run_pipeline.py` para iniciar el proceso completo:
   ```bash
   python run_pipeline.py --data_dir data
   ```
   Si deseas ejecutar el pipeline en un directorio diferente, puedes especificarlo:
   ```bash
   python run_pipeline.py --data_dir test
   ```
# Procesamiento de Nuevos Archivos

Para procesar nuevos archivos en el pipeline de la aplicación, simplemente sigue estos dos pasos:

1. **Añadir Archivos a la Carpeta de Entrada**:
   - Coloca los archivos PDF que deseas procesar en la carpeta `data/input/raw/` (o en la carpeta equivalente si estás utilizando un directorio diferente, como `test/input/raw/`).
   - La aplicación está diseñada para detectar automáticamente los archivos nuevos en esta carpeta y procesarlos.

2. **Ejecutar el Pipeline**:
   - Una vez que hayas añadido los archivos, ejecuta el pipeline completo con el siguiente comando:
     ```bash
     python run_pipeline.py --data_dir data
     ```
   - Si estás utilizando un directorio diferente, asegúrate de especificarlo:
     ```bash
     python run_pipeline.py --data_dir test
     ```

El pipeline se encargará de:
- Convertir los archivos PDF a Markdown.
- Limpiar el contenido Markdown eliminando tablas, citaciones, referencias y secciones no deseadas.
- Analizar la salida para detectar y eliminar archivos con promedios de longitud de palabras anormales.
- Dividir el texto limpio en chunks más pequeños para facilitar su uso posterior.

La aplicación se encargará del resto, procesando los nuevos archivos y guardando los resultados en las carpetas correspondientes.

## Descripción de los Archivos

### `clean_markdown.py`

Este archivo contiene funciones para limpiar el contenido Markdown. Las funciones incluyen:

- **eliminar_tablas**: Elimina tablas en formato Markdown.
- **remove_fig_table_titles_regex**: Elimina títulos de figuras y tablas.
- **eliminar_citaciones**: Elimina citaciones en formato (Autor, Año) o [Número].
- **eliminar_referencias**: Elimina la sección de referencias.
- **eliminar_secciones_no_deseadas**: Elimina secciones como "Acknowledgements" o "Conflict of Interest".
- **eliminar_lineas_vacias**: Elimina líneas vacías del texto.
- **procesar_archivo_md**: Aplica todas las funciones de limpieza en orden.
- **procesar_md_pipeline**: Lee un archivo Markdown, lo procesa y guarda el resultado en un archivo de texto.

### `pdf_to_markdown.py`

Este archivo se encarga de convertir archivos PDF a Markdown utilizando `LlamaParse`. Las funciones incluyen:

- **transform_pdf**: Convierte un archivo PDF a Markdown y lo guarda en un directorio de salida.
- **pre_process_pdf**: Pre-procesa un archivo PDF llamando a `transform_pdf`.
- **main**: Ejecuta el proceso de conversión en paralelo para todos los archivos PDF en el directorio de entrada.

### `process_markdown.py`

Este archivo procesa los archivos Markdown generados por `pdf_to_markdown.py`. Las funciones incluyen:

- **cargar_baneados**: Carga la lista de archivos baneados desde un archivo JSON.
- **process_md**: Procesa un archivo Markdown utilizando las funciones de `clean_markdown.py`.
- **main**: Ejecuta el procesamiento de todos los archivos Markdown en el directorio de entrada.

### `analyze_output.py`

Este archivo analiza los archivos de texto procesados y elimina aquellos con promedios de longitud de palabras anormales. Las funciones incluyen:

- **cargar_baneados**: Carga la lista de archivos baneados desde un archivo JSON.
- **guardar_baneados**: Guarda la lista de archivos baneados en un archivo JSON.
- **calcular_longitud_promedio_palabras**: Calcula la longitud promedio de las palabras en un texto.
- **calcular_iqr**: Calcula el rango intercuartílico (IQR) de una lista de datos.
- **procesar_archivos**: Analiza los archivos de texto y elimina aquellos con promedios anormales.

### `split_into_chunks.py`

Este archivo divide los archivos de texto procesados en chunks más pequeños. Las funciones incluyen:

- **dividir_en_chunks**: Divide un texto en chunks de un máximo de palabras especificado.
- **cargar_archivos_procesados**: Carga la lista de archivos ya procesados desde un archivo JSON.
- **guardar_archivos_procesados**: Guarda la lista de archivos procesados en un archivo JSON.
- **procesar_archivos_txt**: Procesa todos los archivos de texto en el directorio de entrada y los divide en chunks.

### `config.py`

Este archivo contiene la configuración del proyecto. Define los directorios de entrada y salida, así como los nombres de los archivos de configuración.

### `run_pipeline.py`

Este archivo ejecuta todos los scripts en el orden correcto para completar el pipeline de procesamiento de documentos.

## Conclusión

Este proyecto es una herramienta poderosa para procesar documentos PDF, limpiar su contenido y prepararlo para su uso en aplicaciones de procesamiento de lenguaje natural (NLP). Siguiendo los pasos descritos, puedes ejecutar el pipeline completo y obtener archivos de texto limpios y divididos en chunks para su posterior análisis.