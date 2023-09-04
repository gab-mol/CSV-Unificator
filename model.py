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


# Entrada de variables de entorno (.env)
load_dotenv()

# 
__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__version__ = os.getenv("VERSION")
__copyright__ = f"Copyright {HoFe.fecha()}"
__annotations__ = 'Reescribiendo -01/09/23'


# Clases Modelo ###############

class Archivos:
    '''Métodos para ingreso y procesado de archivos.'''
    
    @staticmethod
    def pedir_ruta() -> str:
        '''Solicita al usuario ubicación de directorio'''
        ruta_dir_csv = filedialog.askdirectory()
        return  ruta_dir_csv
    
    def cargar_csv(ruta_carp_cvs_s:str):
        '''Carga todos los csv en: [[nombre.csv, dataframe], ..n]'''
        lista_csv = os.listdir(ruta_carp_cvs_s)
        lista_dfs = []
        for i in range(len(lista_csv)):
            df = pd.read_csv(os.path.join(ruta_carp_cvs_s, lista_csv[i]), skiprows=[0], header = None)
            lista_dfs.append([lista_csv[i], df])
        return lista_dfs
    
    def unir_csv(lista_dfs:list):
        '''Crea la tabla conjunta \nNOTA: recordar que deben tener = nfilas'''

        # ruta al primer archivo
        ruta_0 = os.path.join(ruta_carp_cvs_s, lista_csv[0])
        t_0 = pd.read_csv(ruta_0, skiprows=[0], header = None)
        t_0 = t_0.drop(labels=0, axis=0)
        
        #filas_cvs0 = len(t_0.index)
        #filas.set(str(filas_cvs0))
    
    def verificar_nfilas(lista_dfs):
        '''Avisar al usuario si no todos los csv tienen el mismo largo.
        NOTA: esto pasa cuando se varió el tiempo de ensayo durante el mismo.'''
        largos = []
        for csv in lista_dfs:
            largos.append(csv[1].shape[0])


class EventosBot:
    '''Acciones de los botones'''
    def __init__(self, strvar, sal_tex) -> None:
        self.strvar = strvar
        self.sal_tex = sal_tex
        
    def entr_ruta(self, END):
        '''Solicita ruta, la guarda en stringvar y muestra en
        widget.'''
        ruta_csv_str = Archivos.pedir_ruta()
        
        self.strvar.set(ruta_csv_str)
        
        self.sal_tex.delete("1.0", "end")
        self.sal_tex.insert(END, ruta_csv_str)
        print("\nRUTA ELEGIDA: ", self.strvar.get(),"\n")
        
        