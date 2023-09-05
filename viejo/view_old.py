'''CSV-Unificator: vista'''
from tkinter import Tk, Label, StringVar, Button, Entry, messagebox
from viejo.model_old import pedir_ruta, secuencia, preg_carp, dir_sal_cvs


root = Tk()
root.geometry("290x330")
root.config(bg="#C2E871")
root.title("CSV-Unificator")


instrucciones0 = Label(text="Previamente: Guardar solo los .cvs en una carpeta", 
font= ("Arial", 8, "bold") ,bg="#C2E871", pady=10, width=41, underline=21)
instrucciones0.grid(column=0, columnspan=2, row=0)

boton_rutacvs = Button(text="Buscar carpeta con archivos .cvs", 
    command=lambda:pedir_ruta(), pady=10, width=40, bg="#DBF1AD")
boton_rutacvs.grid(column=0, columnspan=2, row=1)

##Etiqueta con ruta:
ruta_carp_cvs_s = StringVar()
ruta_carp_cvs_s.set("<ruta a carpeta con .cvs>")
salida_ruta = Label(textvariable=ruta_carp_cvs_s, padx=1, pady=1, wraplength=280, anchor="center", bg="#C2E871")   
salida_ruta.grid(column=0, columnspan=2, row=2)
##
boton_rutacvs = Button(text="CONVERTIR", command=lambda:secuencia(), pady=10, 
width=40, bg="#DBF1AD")
boton_rutacvs.grid(column=0, columnspan=2, row=3)

filas = StringVar()
filas_ent = Entry(root, textvariable=filas, justify="center", width=10)
filas_ent.grid(column=1, columnspan=1, row=4, sticky="w")


filas_label = Label(text="n° de filas (+títulos): ", bg="#C2E871", padx=1)
filas_label.grid(column=0, columnspan=1, padx=20, row=4, sticky="e")

instrucciones1_sv = StringVar()
instrucciones1_sv.set("Los .cvs ya transformados no se mueven \
de la \ncarpeta donde se leen")

instrucciones2_sv = StringVar()
instrucciones2_sv.set("Los .cvs no se copian")

boton_consul_carp = Button(textvariable=instrucciones1_sv, 
command=lambda:preg_carp(), pady=10, width=40, bg="#DBF1AD")
boton_consul_carp.grid(column=0, columnspan=2, row=5)

boton_salida_csv = Button(textvariable=instrucciones2_sv, 
command=lambda:dir_sal_cvs(), pady=2, width=40, bg="#DBF1AD")
boton_salida_csv.grid(column=0, columnspan=2, row=6)

boton_salida_csv["state"] = "disabled"

ruta_carp_cvs = StringVar()
fuente0 = ("Arial", 8, "bold")
instrucciones2 = Label(master=root, text="Las columnas de Abs son tomadas y pegadas en \n\
una única tabla excel. La primera columna es la\n de tiempo. Se toma como referencia el \n\
primer archivo para establecer el n° de filas.\n Se puede editar el máximo de filas.\n\
SE ELIMINA las filas superiores a este n°.", font=fuente0, bg="#C2E871", width=41)
instrucciones2.grid(column=0, columnspan=2, row=7)

root.mainloop()