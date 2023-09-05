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
__annotations__ = 'Código no funcional. Solo se formateó proyecto -31/08/23'


# Modelo #####################################################################################################
def secuencia():
    tabla_salida = archivos()
    al_excel(tabla_salida)
    pedir_ruta()
    if guardar == True: dir_sal()

def pedir_ruta():
    global lista_cvs, filas_cvs0, t_0
    filename = filedialog.askdirectory()
    ruta_carp_cvs.set(filename)
    ruta_carp_cvs_s.set(filename)
    lista_cvs = os.listdir(ruta_carp_cvs.get())
    ruta_0 = os.path.join(ruta_carp_cvs.get(), lista_cvs[0])
    t_0 = pd.read_csv(ruta_0, skiprows=[0], header = None)
    t_0 = t_0.drop(labels=0, axis=0)
    filas_cvs0 = len(t_0.index)
    filas.set(str(filas_cvs0))

def archivos():
    global lista_cvs, t_0
    tabla_salida = t_0.drop(t_0.columns[[1]], axis=1)
    tabla_salida.columns = ["Time/sec"]
    for i in lista_cvs:
        ruta_i = os.path.join(ruta_carp_cvs.get(), i)
        cvs_i = pd.read_csv(ruta_i, skiprows=[0], header = None)
        cvs_i = cvs_i.drop(labels=0, axis=0)
        cvs_i = cvs_i.drop(cvs_i.columns[[0]], axis=1)
        #print(type(cvs_i))
        #print(cvs_i.head())
        #cvs_i = pd.to_numeric((list(cvs_i)))
        #cvs_i = pd.DataFrame(cvs_i)
        n_corte = int(filas.get())
        if len(cvs_i.index)>filas_cvs0: cvs_i = cvs_i.iloc[0:n_corte]
        cvs_i.columns = [f"{i[:-4]}"]
        tabla_salida = pd.merge(tabla_salida, cvs_i, left_index=True, 
                                right_index=True)  
    return tabla_salida



def al_excel(tabla_salida):
    preg_usuario = filedialog.askdirectory()
    ruta_salida = os.path.join(preg_usuario, "tabla_salida.xlsx")
    print("salida: " + ruta_salida)
    tabla_salida = tabla_salida.apply(lambda x: x.str.replace('.', ',')) #Esta f cambia los decimales a puntos
    #writer = pd.ExcelWriter(ruta_salida,
    #                    engine='xlsxwriter',
    #                    engine_kwargs={'options': {'strings_to_numbers': True}})
    tabla_salida.to_excel(ruta_salida, index=False) #write
    #writer.close()

carpeta_pasadas = ""
def dir_sal_cvs():
    global carpeta_pasadas
    preg_usuario2 = filedialog.askdirectory()
    carpeta_pasadas = os.path.join(preg_usuario2, 'pasadas a tabla')
    
def dir_sal():
    if carpeta_pasadas == "": messagebox.showwarning("Advertencia:", "No se eligió carpeta de salida .cvs")
    if not os.path.exists(carpeta_pasadas):
        os.makedirs(carpeta_pasadas)
        print("se creó carpeta")
    for i in lista_cvs:
        shutil.move(os.path.join(ruta_carp_cvs.get(), i), carpeta_pasadas)



swich_boton = False
def des_boton():
    if swich_boton==True:
        boton_salida_csv["state"] = "normal"
    else:
        boton_salida_csv["state"] = "disabled"

swich = False
guardar = False
def preg_carp():
    global swich, guardar, swich_boton
    if swich == True:
        instrucciones1_sv.set("Los .cvs ya transformados se mueven a carpeta: \
\n'pasadas a tabla' (creada donde se ejecute esta app)")
        guardar = True
        swich = False
        swich_boton = True
        print("guardar")
        instrucciones2_sv.set(">>>Elegir ubicación")
    else:
        instrucciones1_sv.set("Los .cvs ya transformados no se mueven \
de la \ncarpeta donde se leen")
        guardar = False
        swich = True
        swich_boton = False
        instrucciones2_sv.set("Los .cvs no se copian")
        print("no guardar")
    des_boton()

