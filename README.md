# 🗂️ Separar PDF por Institución

Este proyecto permite dividir automáticamente un archivo PDF grande en múltiples archivos más pequeños, cada uno correspondiente a una institución educativa específica. El código se basa en la coincidencia de códigos únicos dentro del texto de cada página del PDF.

## 📌 Características

* Divide un PDF en varios archivos individuales, uno por cada código de institución.
* Soporta archivos `.csv` o `.xlsx` con la lista de códigos.
* Manejo de errores y validaciones integradas.
* Organiza los archivos PDF generados en una carpeta de salida definida.

## 🛠️ Requisitos

* Python 3.7 o superior
* Bibliotecas:

  * `pandas`
  * `PyPDF2`

Instalación de dependencias:

```bash
pip install pandas PyPDF2
```



