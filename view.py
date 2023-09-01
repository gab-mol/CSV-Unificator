'''CSV-Unificator: vista'''

from tkinter import Label, StringVar, Button, Entry, messagebox

### para desarrollo ###
from tkinter import Tk
########################

import model


class Window:
    def __init__(self, root_mainloop):
        root = root_mainloop
        root.geometry("290x330")
        root.config(bg="#C2E871")
        root.title("CSV-Unificator")

        # Texto instructivo
        instrucciones0 = Label(text="Previamente: Guardar solo los .cvs en una carpeta", 
        font= ("Arial", 8, "bold") ,bg="#C2E871", pady=10, width=41, underline=21)
        instrucciones0.grid(column=0, columnspan=2, row=0)

        filas_label = Label(text="n° de filas (+títulos): ", bg="#C2E871", padx=1)
        filas_label.grid(column=0, columnspan=1, padx=20, row=4, sticky="e")
        
        # Salida de info
        self.ruta_carp_cvs_s = StringVar()
        self.ruta_carp_cvs_s.set("<ruta a carpeta con .cvs>")

        salida_ruta = Label(textvariable=self.ruta_carp_cvs_s, padx=1, 
                pady=1, wraplength=280, anchor="center", bg="#C2E871")   
        salida_ruta.grid(column=0, columnspan=2, row=2)        

        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", 
            command=lambda:boton_pedir_csv(), pady=10, width=40, bg="#DBF1AD")
        boton_rutacvs.grid(column=0, columnspan=2, row=1)

        # Botones
        boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", 
        command=lambda:pedir_ruta(), pady=10, width=40, bg="#DBF1AD")
        boton_rutacvs.grid(column=0, columnspan=2, row=1)
        
        # Eventos de botones
        def boton_pedir_csv(self):
            pedir_ruta = model.pedir_ruta(self.ruta_carp_cvs_s)
        
        def pedir_ruta(self):
            ...



### para desarrollo ###
if __name__=="__main__":
    root = Tk()
    lanzar = Window(root)
    root.mainloop()