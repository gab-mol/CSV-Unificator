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
from tkinter import filedialog, messagebox, simpledialog
import re

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
__version__ = "Pre-Release-1.0"
__copyright__ = f"Copyright {HoFe.fecha()}"
__annotations__ = 'Desarrollo concluído.'

# Nombre de primera columna
global nom_col0
nom_col0 = "Time/sec"

# Clases Modelo ###############

class Archivos:
    '''Métodos para carga y procesado de archivos.'''
    def __init__(self, ruta_dir_csv) -> None:
        '''Recibe ruta y carga todos los archivos .csv
        en df (pandas).'''
        self.ruta_dir_csv = ruta_dir_csv
        self.lista_csv = os.listdir(self.ruta_dir_csv)
        
        # aviso carpeta vacía
        if self.lista_csv == []:
            messagebox.showwarning("Problema con carpeta de archivos:",
                "\nCarpeta seleccionada vacía.")
            raise Exception("No se recuperaron archivos de directorio seleccionado")
        
        # limpiar de no-.csv
        self.lista_csv_v = Verificador.limp_nocsv(self.lista_csv)
        
        # Carga todos los csv en: [[nombre.csv, dataframe], ..n]
        lista_dfs = []
        for i in range(len(self.lista_csv_v)):
            df = pd.read_csv(os.path.join(self.ruta_dir_csv, self.lista_csv_v[i]), 
                skiprows=[0], header = None)
            lista_dfs.append([self.lista_csv_v[i].replace(".csv",""), df])
        self.lista_dfs = lista_dfs
    
    def verificar_nfilas(self, END, salida_lista_csv):
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
                
                salida_lista_csv.config(state="normal")
                salida_lista_csv.delete("1.0", "end")
                salida_lista_csv.insert(END, "\n\n\n...\nEsperando\nque el usuario\n\
resuelva\ninconsistencia\nen los archivos\n...")
                salida_lista_csv.config(state="disabled")
                
                messagebox.showerror("Inconsistencia en N° filas", 
                    "Conflicto: revisar los archivos, probablemente se hayan \
                    realizado medidas a tiempos distintos")
                
                raise Exception("Archivos con distinto n° de filas EN PROPORCIONES IDÉNTICAS")
            #########################    
            else:
                # Informar sobre archivos problemáticos
                conflictos_iyl = []
                i = 0
                for l in largos:
                    print(self.lista_csv[i], l, largos_unicos[i_mayor])
                    if l != largos_unicos[i_mayor]:
                        conflictos_iyl.append([i, l])
                    i += 1

                conflictos_n = []
                for i in conflictos_iyl:
                    conflictos_n.append([self.lista_csv[i[0]], i[1]])
                print("¡¡¡Hay archivos con distinto número de fila!!!")
                print("Largos:", largos_unicos)
                print("Revisar:", conflictos_n)
                
                salida_lista_csv.config(state="normal")
                salida_lista_csv.delete("1.0", "end")
                salida_lista_csv.insert(END, "\n\n\n...\nEsperando\nque el usuario\n\
resuelva\ninconsistencia\nen los archivos\n...")
                salida_lista_csv.config(state="disabled")
                # formateo de aviso..
                largos_unicos_str = []
                for n in largos_unicos:
                    largos_unicos_str.append(str(n))
                largos_unicos_str = "\n ".join(largos_unicos_str)
                conflictos_n_str = []
                for conf in conflictos_n:
                    conflictos_n_str.append(conf[0]+" ("+str(conf[1])+")")
                conflictos_n_str = "\n ".join(conflictos_n_str)
                
                messagebox.showerror("Inconsistencia en N° filas",
                    f"\nN° filas registrados:\n {largos_unicos_str} \n (Siendo: {largos_unicos[i_mayor]} \
el más común)\n\nREVISAR:\n {conflictos_n_str}")
                raise Exception("Archivos con distinto n° de filas")
    
    def unir_csv(self,ruta_salida):
        '''Crea la tabla conjunta 
        NOTA: recordar que deben tener = nfilas'''

        # revisar columnas de tiempo (NO funcional)
        Verificador.prim_col(self.lista_dfs, self.lista_csv_v, ruta_salida)
        
        # ruta al primer archivo
        csv0 = self.lista_dfs[0]
        t0 = csv0[1]
        tabla_salida = t0.drop(t0.columns[[1]], axis=1)
        tabla_salida.columns = [nom_col0]
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

        self.sal_tex.config(state="normal")
        self.sal_tex.delete("1.0", "end")
        self.sal_tex.insert(END, self.ruta)
        self.sal_tex.config(state="disabled")

        print("\nRUTA ELEGIDA: ", self.strvar.get(),"\n")
    
    def csv_a_df(self, END, salida_lista_csv):
        '''Recibe ruta a carpeta de csv, y carga a df 
        los mismos.'''
        self.entr_ruta(END)
        self.archivos = Archivos(self.ruta)
        self.archivos.verificar_nfilas(END, salida_lista_csv)

        # mostrar lista de archivos
        l_arch = "\n ".join(self.archivos.lista_csv_v)
        l_arch = "-- CSV a unir --\n "+ l_arch
        
        salida_lista_csv.config(state="normal")
        salida_lista_csv.delete("1.0", "end")
        salida_lista_csv.insert(END, l_arch)
        salida_lista_csv.config(state="disabled")

    def convert(self, ruta_salida:str, nombre:str):
        if nombre == "":
            messagebox.showwarning("Falta nombre de archivo", 
                "Especificar nombre de libro excel.")
            raise Exception("Sin nombre")
            
        Verificador.nom_xlsx(nombre, self.archivos.lista_csv)
            
        try: 
            self.tabla_salida = self.archivos.unir_csv(ruta_salida)
        except:
            messagebox.showerror("ERROR","Algo falló en conversión.")
            raise Exception("Error de conversión")

        ruta_arch = os.path.join(ruta_salida, f"{nombre}.xlsx")
        print("salida: " + ruta_salida)

        # Creación de archivo .xlsx
        try:
            self.tabla_salida.to_excel(ruta_arch, index=False)
        except:
            messagebox.showerror("ERROR", 
                "No fue posible crear el archivo excel")
            raise Exception("Falla en creacción de archivo .xlsx")
        messagebox.showinfo("Aviso",f"\nLibro excel '{nombre}' creado exitosamente")

    @staticmethod
    def sobre():
        '''Brinda información sobre el programa.'''
        messagebox.showinfo(f"CSV-Unificator: Unificador de archivos .csv | vers.: {__version__}",
        "Este programa fue desarrollado como una herramienta para usar en conjunto \
con el espectrofotómetro Shimadzu UV-1280 del \
laboratorio de Bioquimica de Arañas del INIBIOLP. \
Su objetivo es facilitar el manejo del output de datos del equipo, \
limitado a archivos .csv separados.\n\n\
\tDesarrollo/Mantenimiento por: \n\tLic. Gabriel Molina - g-abox@hotmail.com\n\n\t\t\
-- Septiembre, 2023")
        
    @staticmethod
    def info():
        '''Información que me pareció relevante ofrecer al usuario.'''
        res = messagebox.askquestion("Primera col. (tiempo medida):", "\n\t- Se toma al primer archivo \
de la carpeta como referencia para la columna inicial de tiempo.\n\t- Nombre por defecto es `Time/sec`.\n\n\
¿Desea cambiarlo?")
        if res == "yes":
            global nom_col0
            nom_col0 = simpledialog.askstring(title="Cambiar nombre Primera Col.",
            prompt="Introduzca el título que desee:")


class Verificador():
    '''
    Verificación de cadenas. En campos, en nombres de archivos, en celdas (proximamente).
    '''
    @staticmethod
    def nom_xlsx(cadena:str, lista_dir:list[str]):
        '''
        Uso de modulo re para controlar campos, y consultar posible reescritura.
        '''
        if re.search(r'[$%&"\'()¡!¿?#\][/\\]',cadena):
            messagebox.showwarning("Advertencia", "Introdujo un nómbre no válido \n\
            Sin caracteres especiales (#, $, /, etc.)")
            raise Exception("Nombre con caracteres especiales.")
        else:
            print("excel: nombre válido")
            if (cadena+".xlsx") in lista_dir:
                res = messagebox.askquestion("Advertencia", 
                    "Introdujo un nombre ya presente en la carpeta que seleccionó ¿Sobrescribir?")
                if res != "yes":raise Exception("Usuario abortó el proceso antes de sobrescribir.")
    
    @staticmethod
    def limp_nocsv(lista_csv:list) -> list:
        '''Elimina de la lista de archivos los que no terminan en `.csv`\n
        Notifica los nombres eliminados.'''
        print("LISTA:")
        a_rm = []
        lista_csv_sal = []
        for n in lista_csv:
            if re.search(r"^.+\.csv$",n):
                lista_csv_sal.append(n)
                print(n,"aprobado")
            else:
                a_rm.append(n)
                print(n,"descartado")
        if a_rm != []:
            print("lista final: ",lista_csv_sal)
            print("Descartados:",a_rm)
            a_rm_str = "\n ".join(a_rm)
            messagebox.showwarning("AVISO:", 
                f"Se ignoraron archivos no .cvs:\n {a_rm_str}")
        return lista_csv_sal
    
    @staticmethod
    def prim_col(lista_dfs:list[list], lista_nombres:list,ruta_salida):
        '''Revisa consistencia de tiempos en primera columna de archivos'''
        lista_col0s = []
        for l in lista_dfs:
            lista_col0s.append(l[1].iloc[:,0])
        
        i_lista_col0s = []
        for i in range(len(lista_col0s)):
            for j in range(i+1,len(lista_col0s)):
                comp = list(lista_col0s[i]==lista_col0s[j])
                i_fal = [i for i, v in enumerate(comp) if v == False]
        
                i_lista_col0s.append([lista_nombres[i], lista_nombres[j], i_fal])
        
        #  Usar expresión de compresión de listas para separar listas de errores,
        # si esas listas están todas vecías (sin errores), la suma de sus largos 
        # tiene que ser 0
        if sum([len(err) for n0, n1, err in i_lista_col0s]) != 0:
            inconsist = [[n0, n1, err] for n0, n1, err in i_lista_col0s if err != []]
            res = messagebox.askquestion("Advertencia sobre filas de tiempo",
            "Si bien todas las columnas de tiempo tienen el mismo largo, no todas sus celdas son iguales\n\
Recuerde que se usa el primer archivo como referencia.\n\n\n\
¿Guardar también lista de comparaciones entre csv y n° de filas en conflicto?\n(se junto al excel)")
            if res == "yes":
                ruta=os.path.join(ruta_salida,"CSV-Unif_inconsistencias_"+HoFe.fecha()+".txt")
                print("SE GUARDA .TXT ACÁ:\n",ruta)
                with open(ruta, "w") as inform:
                    inform.write(f"CSV-Unificator | Informe de inconsistencias entre filas de tiempo\n\
{HoFe.hora()} del {HoFe.fecha()}\n\nSe enumera: par de archivos comparados / número de fila en conflicto\n\n")
                    for error in inconsist:
                        form = [str(i) for i in error[2]]
                        inform.write("Entre "+error[0]+" y "+error[1]+" -> Diferencias en filas n°: "+", ".join(form)+"\n")
                