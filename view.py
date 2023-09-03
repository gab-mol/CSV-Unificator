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
F_TITULO = ("Arial", 15, "bold")

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

        # filas_label = Label(text="n° de filas (+títulos): ", bg=ETIQUETAS, padx=1)
        # filas_label.place(relx = 0.01, rely = 0.15)

        
        # Variables entrada/salida
        ruta_carp_cvs_s = StringVar() # hace falta? - supongo que para pasar a modelo 
        ruta_xlsx_s = StringVar()
        
        # Salida de info
        salida_ruta_csv = Text(root, height = 3, width = 50)
        salida_ruta_csv.place(relx = 0.45, rely = 0.15)
        salida_ruta_csv.insert(END, "\n   ruta a carpeta con .cvs ..")
        
        salida_ruta_excel = Text(root, height = 3, width = 50)
        salida_ruta_excel.place(relx = 0.45, rely = 0.4)
        salida_ruta_excel.insert(END, "\n   ruta salida como .xlsx ..")
        
        # Botones
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs",
        command=lambda:pedir_csv.entr_ruta(END), pady=10, padx=5, height = 2, 
        width=40, bg=BOTONES)
        boton_rutacvs.place(relx = 0.01, rely = 0.15)
        
        boton_rutasal = Button(text="Elegir salida del libro excel  ",
        command=lambda:ruta_salida.entr_ruta(END), pady=10, padx=5, height = 2, 
        width=40, bg=BOTONES)
        boton_rutasal.place(relx = 0.01, rely = 0.4)

        # Eventos de botones
        pedir_csv = EventosBot(ruta_carp_cvs_s, salida_ruta_csv)
        ruta_salida = EventosBot(ruta_xlsx_s, salida_ruta_excel)
        

### para desarrollo ###
if __name__=="__main__":
    root = Tk()
    lanzar = Window(root)
    root.mainloop()