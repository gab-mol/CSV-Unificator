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
# import shutil
import pandas as pd
from tkinter import filedialog, messagebox

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

def unique(lista:list):
    '''Algoritmo (google) para quedarse con valores
    únicos de lista.'''
    largos_unicos = []
    for x in lista:
        # solo agrega si no está presente (pasa 1 vez)
        if x not in largos_unicos:
            largos_unicos.append(x)

    return largos_unicos

class Archivos:
    '''Métodos para carga y procesado de archivos.'''
    def __init__(self, ruta_dir_csv) -> None:
        '''Recibe ruta y carga todos los archivos .csv
        en df (pandas).'''
        self.ruta_dir_csv = ruta_dir_csv
        self.lista_csv = os.listdir(self.ruta_dir_csv)
        
        '''Carga todos los csv en: [[nombre.csv, dataframe], ..n]'''
        lista_dfs = []
        for i in range(len(self.lista_csv)):
            df = pd.read_csv(os.path.join(self.ruta_dir_csv, self.lista_csv[i]), skiprows=[0], header = None)
            lista_dfs.append([self.lista_csv[i], df])
        self.lista_dfs = lista_dfs
    
    def verificar_nfilas(self):
        '''Avisar al usuario si no todos los csv tienen el mismo largo.
        NOTA: esto pasa cuando se varió el tiempo de ensayo durante el mismo.'''
        largos = []
        for csv in self.lista_dfs:
            largos.append(csv[1].shape[0])

        # obtener valores únicos de largos
        largos_unicos = []
        for valor in largos:
            # (solo agrega si no está presente)
            if valor not in largos_unicos:
                largos_unicos.append(valor)
        # contar sus frecuencias (respeta posición arg: lista)
        frecuencias_largos = []
        for valor in largos_unicos:
            frecuencias_largos.append(largos.count(valor))

        # Si hay variación en n de filas: ###########
        if len(frecuencias_largos) > 1:
            
            i_mayor = 0
            for frec in frecuencias_largos:
                if frec == max(frecuencias_largos): break 
                else: i_mayor+=1
            
            # por si llegara a pasar que 2 o + frecuencias iguales
            j = 0
            for frec in frecuencias_largos:
                if frec == max(frecuencias_largos): 
                    j+=1
            
            if j > 1: 
                print("ERROR: MUCHOS ARCHIVOS CON DISTINTO N° DE FILAS")
                messagebox.showerror("Inconsistencia en N° filas", 
                    "Conflicto: revisar los archivos, probablemente se hayan \
                    realizado medidas a tiempos distintos")
            #########################    
            else:
                # Informar sobre archivos problemáticos
                conflictos_i = []
                i = 0
                for l in largos:
                    print(self.lista_csv[i], l, largos_unicos[i_mayor])
                    if l != largos_unicos[i_mayor]:
                        conflictos_i.append(i)
                    i += 1

                conflictos_n = []
                for i in conflictos_i:
                    conflictos_n.append(self.lista_csv[i])
                print("¡¡¡Hay archivos con distinto número de fila!!!")
                print("Largos:", largos_unicos)
                print("Revisar:", conflictos_n)
                messagebox.showerror("Inconsistencia en N° filas",
                    f"\nN° filas registrados:, {largos_unicos} \nRevisar: {conflictos_n}")
    
    def unir_csv(self):
        '''Crea la tabla conjunta 
        NOTA: recordar que deben tener = nfilas'''

        # ruta al primer archivo
        csv0 = self.lista_dfs[0]
        t0 = csv0[1]
        tabla_salida = t0.drop(t0.columns[[1]], axis=1)
        tabla_salida.columns = ["Time/sec"]
        for l in self.lista_dfs:
            df = l[1].drop(labels=0, axis=0)
            df = df.drop(df.columns[[0]], axis=1)
            df.columns = [l[0]]
            tabla_salida = pd.merge(tabla_salida, df,
                 left_index=True, right_index=True)
        
        #Esta f cambia los decimales a puntos
        tabla_salida = tabla_salida.apply(lambda x: x.str.replace('.', ','))
        
        return tabla_salida

class EventosBot:
    '''Acciones de los botones'''
    def __init__(self, strvar, sal_tex) -> None:
        self.strvar = strvar
        self.sal_tex = sal_tex
        
    def entr_ruta(self, END):
        '''Solicita ruta, la guarda en stringvar y muestra en
        widget.'''
        self.ruta = filedialog.askdirectory()
        
        self.strvar.set(self.ruta)
        
        self.sal_tex.delete("1.0", "end")
        self.sal_tex.insert(END, self.ruta)
        print("\nRUTA ELEGIDA: ", self.strvar.get(),"\n")
    
    def csv_a_df(self, END):
        '''Recibe ruta a carpeta de csv, y carga a df 
        los mismos.'''
        self.entr_ruta(END)
        self.archivos = Archivos(self.ruta)
        self.archivos.verificar_nfilas()
    

    def convert(self, ruta_salida:str, nombre:str):
        if nombre == "":
            messagebox.showerror("Falta nombre de archivo", 
                "Especificar nombre de libro excel.")
        self.tabla_salida = self.archivos.unir_csv()
        ruta_arch = os.path.join(ruta_salida, f"{nombre}.xlsx")
        print("salida: " + ruta_salida)

        # Creación de archivo .xlsx
        self.tabla_salida.to_excel(ruta_arch, index=False)
        
