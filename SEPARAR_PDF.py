import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
import os

def separar_por_institucion(pdf_path, data_path, output_folder):
    try:
        # Validar la existencia de los archivos
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"El archivo PDF no fue encontrado en la ruta: {pdf_path}")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"El archivo de datos no fue encontrado en la ruta: {data_path}")

        # Crear carpeta de salida si no existe
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Leer los códigos de institución desde el archivo CSV o XLSX
        if data_path.endswith('.csv'):
            data = pd.read_csv(data_path)
        elif data_path.endswith('.xlsx'):
            data = pd.read_excel(data_path)
        else:
            raise ValueError("El archivo de datos debe ser un .csv o .xlsx")

        # Validar que la columna 'codigo' exista
        if 'codigo' not in data.columns:
            raise KeyError("La columna 'codigo' no existe en el archivo de datos.")

        # Eliminar valores nulos y duplicados
        codigos_instituciones = data['codigo'].dropna().drop_duplicates().tolist()

        # Leer el archivo PDF original
        reader = PdfReader(pdf_path)

        # Generar un PDF por institución
        paginas_totales = len(reader.pages)
        pagina_actual = 0  # Para rastrear la posición actual en el PDF

        for codigo in codigos_instituciones:
            writer = PdfWriter()
            paginas_agregadas = 0  # Contador de páginas agregadas para el código actual

            # Iterar a partir de la página actual para optimizar
            while pagina_actual < paginas_totales:
                page = reader.pages[pagina_actual]
                if codigo in page.extract_text():
                    writer.add_page(page)
                    paginas_agregadas += 1
                else:
                    # Si ya se encontraron páginas para el código y el texto cambia, detener la búsqueda
                    if paginas_agregadas > 0:
                        break
                
                # Avanzar a la siguiente página
                pagina_actual += 1

            if paginas_agregadas > 0:
                # Guardar el PDF para la institución
                output_path = f"{output_folder}/{codigo}.pdf"
                with open(output_path, "wb") as output_pdf:
                    writer.write(output_pdf)
                print(f"Archivo creado: {output_path}")
            else:
                print(f"No se encontraron páginas para el código: {codigo}")

    except Exception as e:
        print(f"Se produjo un error: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    pdf_path = "ORIGEN.pdf"  # Ruta al archivo PDF original
    data_path = "CODIGOS.csv"   # Ruta al archivo CSV o XLSX con los códigos de instituciones que serà utilizado para agrupar y generar archivos 
    output_folder = "CARPETA DESTINO"  # Carpeta donde se guardarán los PDFs generados

    separar_por_institucion(pdf_path, data_path, output_folder)
