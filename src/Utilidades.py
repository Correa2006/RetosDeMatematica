from tkinter import END
import matplotlib.pyplot as plt


def limpiar_grafica():
    plt.clf()
    plt.show()


def limpiar_entradas(*args):
    for arg in args:
        try:
            arg.delete(0, END)
        except:
            continue


def ocultar_widgets(frame):
    widgets = frame.winfo_children()

    for widget in widgets:
        widget.destroy()

    frame.pack_forget()
