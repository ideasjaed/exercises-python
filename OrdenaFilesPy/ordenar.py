import os
import sys
import shutil
import time
from random import randint

path = "D:\Descargas"
ext_texto = ['.docx', '.txt', '.doc', '.pdf', '.pptx']
ext_foto = ['.png', '.jpg', '.jpeg', '.gif']
ext_video = ['.mov', '.mp4']

def Buscar_archivo():
    return [arch.name for arch in os.scandir(path) if arch.is_file()]

def Ordenar():
    for archivo in Buscar_archivo():
        try:
            nombre_archivo, ext = os.path.splitext(archivo)
            for i in ext_texto:
                if ext == i:
                    if os.path.exists(path + "\\Texto"):