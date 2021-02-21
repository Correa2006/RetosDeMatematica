from tkinter import *
from PIL import Image, ImageTk
from src.ecuacion_cuadratica import ecuacion_cuadratica

ventana = Tk()
ventana.title("Pydrático")
ventana.tk_setPalette(background="gray93")
ventana.wm_attributes("-topmost", 1)

imagen = Image.open("media/logo.png")
logo = ImageTk.PhotoImage(imagen)
'''
#barra de menu

menu_barra = Menu(ventana)
ventana.config(menu=menu_barra)

#menu items

menu_file = Menu(menu_barra)
menu_help = Menu(menu_barra)

menu_barra.add_cascade(label='File', menu=menu_file)
menu_barra.add_cascade(label='Help', menu=menu_help)

#menu items command

menu_file.add_command(label='Exit', command=ventana.quit)

menu_help.add_command(label='about...', command=lambda: print("x"))
'''

#encabezado
logo_etiqueta = Label(ventana, image=logo)
logo_etiqueta.grid(column=0, row=0, padx=5, pady=5)

encabezado = Label(
    ventana,
    text="Republica Bolivariana de Venezuela\nLiceo Antonio José Pacheco\n\"Reto de matemáticas\"",
    justify="center",
    font="LiberationSans 16",
    background="gray93",
    foreground="gray13"
)
datos_alumno = Label(
    ventana,
    text="José Correa\n4to año\nSección \"D\"",
    justify="right",
    background="gray93",
    foreground="gray37"
)

encabezado.grid(column=1, columnspan=2, row=0, padx=5, pady=15)
datos_alumno.grid(column=3, row=0, padx=5)

ecuacion_cuadratica(logo, ventana)

ventana.mainloop()
