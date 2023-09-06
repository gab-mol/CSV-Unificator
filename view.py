'''CSV-Unificator: vista'''

from tkinter import Label, StringVar, Button, Entry, messagebox, Text, END

### para desarrollo ###
from tkinter import Tk
########################

from model import EventosBot

# colores
FONDO = "#FAD6D0"
ETIQUETAS = "#FAD8D0"
BOTONES = "#E79A7A"

# Fuentes
F_TITULO = ("Arial", 14, "bold")

class Window:
    def __init__(self, root_mainloop):
        root = root_mainloop
        root.geometry("800x330")
        root.config(bg=FONDO)
        root.title("CSV-Unificator")
        
        # Texto instructivo
        instrucciones0 = Label(text="Guardar los .csv en una carpeta (SOLOS)",
        font= F_TITULO, bg=ETIQUETAS, pady=0, padx=0, width=50, underline=21)
        instrucciones0.place(relx = 0.5, rely = 0.01, anchor="n")
        instrucciones1 = Label(text="Nombre del libro de excel:",
        font= ("Arial", 12, "bold"), bg=ETIQUETAS, pady=0, padx=0, width=25)
        instrucciones1.place(relx = 0.63, rely = 0.62, anchor="n")
        # filas_label = Label(text="n° de filas (+títulos): ", bg=ETIQUETAS, padx=1)
        # filas_label.place(relx = 0.01, rely = 0.15)

        
        # Variables entrada/salida
        ruta_carp_cvs_s = StringVar() # hace falta? - supongo que para pasar a modelo 
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
        
        salida_ruta_excel = Text(root, height = 3, width = 50)
        salida_ruta_excel.place(relx = 0.45, rely = 0.4)
        salida_ruta_excel.insert(END, "\n   ruta salida como .xlsx ..")
        
        # Botones
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs",
        command=lambda:pedir_csv.csv_a_df(END), pady=10, padx=5, height = 2, 
        width=40, bg=BOTONES)
        boton_rutacvs.place(relx = 0.01, rely = 0.15)
        
        boton_rutasal = Button(text="Elegir salida del libro excel  ",
        command=lambda:ruta_salida.entr_ruta(END), pady=10, padx=5, height = 2, 
        width=40, bg=BOTONES)
        boton_rutasal.place(relx = 0.01, rely = 0.4)

        boton_convert = Button(text="> Convertir archivos <",
        command=lambda:ruta_salida.convert(ruta_xlsx_s.get(), nombre_xlsx.get()), pady=5, padx=1, height = 2, 
        width=29, bg=BOTONES, font=("Arial", 12, "bold"))
        boton_convert.place(relx = 0.01, rely = 0.65)

        # Eventos de botones
        pedir_csv = EventosBot(ruta_carp_cvs_s, salida_ruta_csv)
        ruta_salida = EventosBot(ruta_xlsx_s, salida_ruta_excel)
        

### para desarrollo ###
if __name__=="__main__":
    root = Tk()
    lanzar = Window(root)
    root.mainloop()