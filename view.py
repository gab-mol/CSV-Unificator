'''CSV-Unificator: vista'''

from tkinter import Label, StringVar, Button, Entry, Text, END
from dotenv import load_dotenv
import os

from model import EventosBot

# colores
FONDO = "#EADBD8"
ETIQUETAS = "#EADBD8"
BOTONES = "#E79A7A"

# Fuentes
F_TITULO = ("Arial", 15, "bold")
F_BOTONES0 = ("Arial", 11)

# Anchos
BW0 = 32

# Variables de entorno
load_dotenv()
VERS = os.getenv("VERSION")

class Window:
    def __init__(self, root_mainloop):
        root = root_mainloop
        root.geometry("800x330")
        root.resizable(width=False, height=False)
        root.config(bg=FONDO)
        root.title("CSV-Unificator")
        
        # Info
        info0 = Label(text=f"Versión:  {VERS}",
        font= ("Century Gothic", 8, "italic"), bg=ETIQUETAS, pady=0, padx=0, width=50)
        info0.place(relx = 0.9, rely = 0.97, anchor="s")       

        # Texto instructivo
        instrucciones0 = Label(text="Guardar los .csv en una carpeta (SOLOS)",
        font= F_TITULO, bg="#EAB2A6", pady=0, padx=0, width=100)
        instrucciones0.place(relx = 0.26, rely = 0.02, anchor="n")

        instrucciones1 = Label(text="Nombre del libro Excel:",
        font= ("Arial", 12, "bold"), bg=ETIQUETAS, pady=0, padx=0, width=25)
        instrucciones1.place(relx = 0.63, rely = 0.62, anchor="n")
        
        instrucciones2 = Label(text="(sin .xlsx)",
        font= ("Arial", 10), bg=ETIQUETAS, pady=4, padx=1, width=25)
        instrucciones2.place(relx = 0.54, rely = 0.87, anchor="s")

        # Variables entrada/salida
        ruta_carp_cvs_s = StringVar()
        ruta_xlsx_s = StringVar()
        nombre_xlsx = StringVar()

        # Entrada nombre
        caja_nomb = Entry(root, textvariable=nombre_xlsx, width=30,
            font=('calibre',12, 'bold'))
        caja_nomb.place(relx = 0.5, rely = 0.72)

        # Salida de info
        salida_ruta_csv = Text(root, height = 3, width = 50)
        salida_ruta_csv.place(relx = 0.45, rely = 0.15)
        salida_ruta_csv.insert(END, "\n   ruta a carpeta con .cvs ..")
        salida_ruta_csv.config(state="disabled")

        salida_ruta_excel = Text(root, height = 3, width = 50)
        salida_ruta_excel.place(relx = 0.45, rely = 0.4)
        salida_ruta_excel.insert(END, "\n   ruta salida como .xlsx ..")
        salida_ruta_excel.config(state="disabled")

        # Botones
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", font=F_BOTONES0,
        command=lambda:pedir_csv.csv_a_df(END), pady=10, padx=5, height = 2, 
        width=BW0, bg=BOTONES)
        boton_rutacvs.place(relx = 0.01, rely = 0.15)
        
        boton_rutasal = Button(text="Elegir salida del libro excel  ", font=F_BOTONES0,
        command=lambda:ruta_salida.entr_ruta(END), pady=10, padx=5, height = 2, 
        width=BW0, bg=BOTONES)
        boton_rutasal.place(relx = 0.01, rely = 0.4)

        boton_convert = Button(text="> Convertir archivos <",
        command=lambda:pedir_csv.convert(ruta_xlsx_s.get(), nombre_xlsx.get()), pady=5, padx=1, height = 2, 
        width=33, bg=BOTONES, font=("Arial", 11, "bold"))
        boton_convert.place(relx = 0.01, rely = 0.65)

        boton_info = Button(text="Primera columna",
        command=lambda:EventosBot.info(), pady=1, padx=1, height = 1, 
        width=20, bg="#FFD2AA", font=("Arial", 9))
        boton_info.place(relx = 0.2, rely = 0.97, anchor="se")      

        boton_about = Button(text="Sobre CSV-Unificator",
        command=lambda:EventosBot.sobre(), pady=1, padx=1, height = 1, 
        width=18, bg="#FAD9BF", font=("Arial", 9))
        boton_about.place(relx = 0.9, rely = 0.025, anchor="n")

        # Eventos de botones
        pedir_csv = EventosBot(ruta_carp_cvs_s, salida_ruta_csv)
        ruta_salida = EventosBot(ruta_xlsx_s, salida_ruta_excel)
