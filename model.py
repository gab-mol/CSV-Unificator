'''CSV-Unificator: modelo
    Intento de recrear con en python y con interfaz grafica el script que hice en R 
    para compilar resultados del espectrofotometro que salen en .cvs en una tabla .xslx automaticamente

    ... meses después, quiero recrear esta app siguiendo MVC y OOP, estructurando el proyecto más seriamente,
    y almacenando proceso en github

'''
# Dependencias
from dotenv import load_dotenv
import os
import time
import shutil
import pandas as pd
from tkinter import filedialog # Repensar

class HoFe:
    '''
    Hora y fecha.
    '''
    def hora() -> str:
        hora = time.strftime("%H:%M:%S hs.", time.localtime(time.time()))
        return hora
    
    def h():
        h = int(time.strftime("%H", time.localtime(time.time())))
        return h
    
    def fecha() -> str:
        fecha = time.strftime("%d-%m-%Y", time.localtime(time.time()))
        return fecha


# Variables de entorno (.env)
load_dotenv()
__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__version__ = os.getenv("VERSION")
__copyright__ = f"Copyright {HoFe.fecha()}"
__annotations__ = 'Reescribiendo -01/09/23'


# Clases Modelo ###############

class EntrArchiv:
    '''Métodos para carga y procesado de .csv'''
    def __init__(self) -> None:
        pass

    def pedir_ruta(self) -> str:
        '''Solicita al usuario ubicación de directorio'''
        ruta_dir_csv = filedialog.askdirectory()
        return  ruta_dir_csv
