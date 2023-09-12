'''CSV-Unificator: vista'''

from tkinter import Label, StringVar, Button, Entry, Text, END, PhotoImage
from dotenv import load_dotenv
import os

from model import EventosBot, __version__

# colores
FONDO = "#EADBD8"
ETIQUETAS = "#EADBD8"
BOTONES = "#E79A7A"
BOTONES2 = "#F5B59A"
TEXTO = "#F1B9AC"

# Fuentes
F_TITULO = ("Arial", 15, "bold")
F_BOTONES0 = ("Arial", 11)

# Anchos
BW0 = 32

# Variables de entorno
load_dotenv()
VERS = __version__

class Window:
    def __init__(self, root_mainloop):
        root = root_mainloop
        root.geometry("875x367")
        root.resizable(width=False, height=False)
        root.config(bg=FONDO)
        root.title("CSV-Unificator")
        '''Estudiar como usar strings para codificar imágenes'''
        #root.iconphoto(True,PhotoImage(file=os.path.join(os. getcwd(),"icoTR.png")))
        
        # Info
        info0 = Label(text=f"Versión:  {VERS}",
        font= ("Century Gothic", 8, "italic"), bg=ETIQUETAS, pady=0, padx=0, width=50)
        info0.place(relx = 0.74, rely = 0.96, anchor="s")       

        # Texto instructivo
        instrucciones0a = Label(text="                                      ", # fondo
        font= F_TITULO, bg="#EAB2A6", pady=1, padx=0, width=130, height=1)
        instrucciones0a.place(relx = 0.26, rely = 0.02, anchor="n")
        
        instrucciones0b = Label(text="Guardar los .csv en una carpeta (SOLOS)",
        font= F_TITULO, bg="#EAB2A6", pady=0, padx=0, width=60)
        instrucciones0b.place(relx = 0.65, rely = 0.02, anchor="ne")

        instrucciones1 = Label(text="Nombre del libro Excel:",
        font= ("Arial", 12, "bold"), bg=ETIQUETAS, pady=0, padx=0, width=25)
        instrucciones1.place(relx = 0.48, rely = 0.55, anchor="n")
        
        instrucciones2 = Label(text="(sin .xlsx)",
        font= ("Arial", 10), bg=ETIQUETAS, pady=4, padx=1, width=25)
        instrucciones2.place(relx = 0.3, rely = 0.7)

        # Variables entrada/salida
        ruta_carp_cvs_s = StringVar()
        ruta_xlsx_s = StringVar()
        nombre_xlsx = StringVar()

        # Entrada nombre
        caja_nomb = Entry(root, textvariable=nombre_xlsx, width=33,
            font=('calibre', 14, 'bold'))
        caja_nomb.place(relx = 0.38, rely = 0.64)

        # Salida de info
        XREL = 0.38
        TH = 3.4
        WD = 46
        salida_ruta_csv = Text(root, height = TH, width = WD, bg=TEXTO)
        salida_ruta_csv.place(relx = XREL, rely = 0.15)
        salida_ruta_csv.insert(END, "\n   ruta a carpeta con .cvs ..")
        salida_ruta_csv.config(state="disabled")

        salida_ruta_excel = Text(root, height = TH, width = WD, bg=TEXTO)
        salida_ruta_excel.place(relx = XREL, rely = 0.35)
        salida_ruta_excel.insert(END, "\n   ruta salida como .xlsx ..")
        salida_ruta_excel.config(state="disabled")

        salida_lista_csv = Text(root, height = 18, width = 17, bg=TEXTO)
        salida_lista_csv.place(relx = 0.83, rely = 0.15)
        salida_lista_csv.insert(END, "\n\n\n  Archivos \n  a \n  unir...")
        salida_lista_csv.config(state="disabled")

        # Botones
        BPY = 5
        BPX = 4
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", font=F_BOTONES0,
        command=lambda:pedir_csv.csv_a_df(END, salida_lista_csv), pady=BPY, padx=BPX, height = 2, 
        width=BW0, bg=BOTONES)
        boton_rutacvs.place(relx = 0.01, rely = 0.15)
        
        boton_rutasal = Button(text="Elegir salida del libro excel  ", font=F_BOTONES0,
        command=lambda:ruta_salida.entr_ruta(END), pady=BPY, padx=BPX, height = 2, 
        width=BW0, bg=BOTONES)
        boton_rutasal.place(relx = 0.01, rely = 0.35)

        boton_convert = Button(text="> Convertir archivos <",
        command=lambda:pedir_csv.convert(ruta_xlsx_s.get(), nombre_xlsx.get()), pady=5, 
        padx=0, height = 2, 
        width=33, bg=BOTONES, font=("Arial", 11, "bold"))
        boton_convert.place(relx = 0.01, rely = 0.55)

        boton_info = Button(text="Primera columna\n(Tiempo)",
        command=lambda:EventosBot.info(), pady=2, padx=1, height = 2, 
        width=20, bg=BOTONES2, font=("Arial Black", 9))
        boton_info.place(relx = 0.01, rely = 0.82)      

        boton_about = Button(text="Sobre CSV-Unificator",
        command=lambda:EventosBot.sobre(), pady=1, padx=1, height = 1, 
        width=19, bg=BOTONES2, font=("Arial", 9))
        boton_about.place(relx = 0.83, rely = 0.025)

        # Eventos de botones
        pedir_csv = EventosBot(ruta_carp_cvs_s, salida_ruta_csv)
        ruta_salida = EventosBot(ruta_xlsx_s, salida_ruta_excel)
