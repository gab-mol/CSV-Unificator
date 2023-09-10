'''CSV-Unificator: controlador'''

import tkinter

import view
from model import __version__, __copyright__, __annotations__

class Launcher:
    '''
    Instancia la clase importada de la vista
    '''
    def __init__(self, main):
        self.root_mainloop=main
        self.objeto_vista=view.Window(main)

if __name__=="__main__":
    print("")
    print("|||||||||||||| <CSV-Unificator: Herramienta para procesar salida del Espectrofotómetro> ||||||||||||||")
    print("\t\t    - Version del programa:", __version__)
    print("\t\t    -",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
    print(__annotations__)
    main=tkinter.Tk()
    aplicacion=Launcher(main)
    main.mainloop()