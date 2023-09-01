'''CSV-Unificator: vista'''

from tkinter import Label, StringVar, Button, Entry, messagebox

### para desarrollo ###
from tkinter import Tk
########################

from model import EntrArchiv

# colores
FONDO = "#FAD6D0"
ETIQUETAS = "#FAD8D0"
BOTONES = "#E79A7A"

class Window:
    def __init__(self, root_mainloop):
        root = root_mainloop
        root.geometry("490x330")
        root.config(bg=FONDO)
        root.title("CSV-Unificator")

        # Instanciación modelo
        entrada = EntrArchiv()

        # Texto instructivo
        instrucciones0 = Label(text="Previamente: Guardar solo los .csv en una carpeta", 
        font= ("Arial", 12, "bold") ,bg=ETIQUETAS, pady=0, padx=0, width=41, underline=21)
        instrucciones0.grid(column=0, columnspan=1, row=0)

        filas_label = Label(text="n° de filas (+títulos): ", bg=ETIQUETAS, padx=1)
        filas_label.grid(column=0, columnspan=1, padx=0, row=4, sticky="e")
        
        # Salida de info
        ruta_carp_cvs_s = StringVar()
        ruta_carp_cvs_s.set("<ruta a carpeta con .cvs>")

        salida_ruta = Label(textvariable=ruta_carp_cvs_s, padx=1, 
                pady=1, wraplength=280, anchor="center", bg=ETIQUETAS)   
        salida_ruta.grid(column=1, columnspan=1, row=2)        

        # Botones
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", 
        command=lambda:boton_pedir_csv(), pady=10, padx=5, width=40, bg=BOTONES)
        boton_rutacvs.grid(column=0, columnspan=1, row=1, sticky="w")

        # Eventos de botones
        def boton_pedir_csv():
            ruta_csv_str = entrada.pedir_ruta()
            ruta_carp_cvs_s.set(ruta_csv_str)
        
        def pedir_ruta():
            ...



### para desarrollo ###
if __name__=="__main__":
    root = Tk()
    lanzar = Window(root)
    root.mainloop()