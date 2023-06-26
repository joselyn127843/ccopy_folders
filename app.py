
import os
import shutil
from PyPDF2 import PdfFileMerger
import fitz



def copiarcarpetas(origen, destino, listacarpetas):
    for carpeta in listacarpetas:
        if not os.path.exists(origen + "/" + carpeta):
            print("Error al copiar carpeta:", carpeta)
        else:
            shutil.copytree(origen + "/" + carpeta, destino + "/" + carpeta)

    print("Copiado exitoso")




# leer archivo txt y convertir a lista
def leerarchivo(archivo):
    with open(archivo, "r") as f:
        lista = f.read().splitlines()
    return lista




def unir_pdf_en_carpeta(carpeta, nombre_archivo_salida, carpeta_guardado):
    salida = fitz.open()
    archivos_pdf = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.pdf')]

    for archivo_pdf in archivos_pdf:
        ruta_completa = os.path.join(carpeta, archivo_pdf)
        archivo = fitz.open(ruta_completa)
        salida.insert_pdf(archivo)

    archivo_salida = os.path.join(carpeta_guardado, nombre_archivo_salida)
    salida.save(archivo_salida)
    salida.close()

    print(f"Se ha creado el archivo '{nombre_archivo_salida}' en la carpeta '{carpeta_guardado}'.")



def verificar_archivos_pdf(carpeta_origen, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    archivos = os.listdir(carpeta_origen)

    archivos_pares = []
    archivos_impares = []

    for archivo in archivos:
        if archivo.lower().endswith('.pdf'):
            ruta_archivo = os.path.join(carpeta_origen, archivo)
            doc = fitz.open(ruta_archivo)

            if doc.page_count % 2 == 0:
                archivos_pares.append(archivo)
            else:
                archivos_impares.append(archivo)

            doc.close()

    archivo_union = os.path.join('1.pdf')
    for archivo in archivos_impares:
        ruta_archivo = os.path.join(carpeta_origen, archivo)
        destino = os.path.join(carpeta_destino, archivo)

        doc_union = fitz.open(archivo_union)
        doc_actual = fitz.open(ruta_archivo)
        
        doc_union.insert_pdf(doc_actual)
        doc_union.save(destino)
        
        doc_union.close()
        doc_actual.close()

    for archivo in archivos_pares:
        ruta_archivo = os.path.join(carpeta_origen, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        shutil.copyfile(ruta_archivo, destino)


carpetamaestra = "C:/Users/Joselyn/Downloads/Nueva"
carpetaarchivos = "C:/Users/Joselyn/Downloads/pdf_imprimi"

carpetas = [carpeta for carpeta in os.listdir(carpetamaestra) if os.path.isdir(os.path.join(carpetamaestra, carpeta))]


for carpeta in carpetas:
    nombre_archivo_salida = carpeta + '.pdf'
    carpeta_origen = os.path.join(carpetamaestra, carpeta)
    carpeta_destino = os.path.join(carpetamaestra, carpeta + '_procesado')

    try:
        verificar_archivos_pdf(carpeta_origen, carpeta_destino)
        unir_pdf_en_carpeta(carpeta_destino, nombre_archivo_salida, carpetaarchivos)
    except Exception as e:
        print(f"Error al procesar la carpeta {carpeta}: {str(e)}")



# copiar carpetas

#origen = "C:/Users/Joselyn/OneDrive/CONVERTIPAP/COMERCIO EXTERIOR 2023/PEDIMENTOS/REFERENCIAS EN PROCESO/DESCARGAS"
#destino = "C:/Users/Joselyn/Downloads/Nueva"
#listacarpetas = "lista.txt"

#copiarcarpetas(origen, destino, leerarchivo(listacarpetas))

