from tkinter import *
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from .Utilidades import limpiar_grafica, limpiar_entradas


def ecuacion_cuadratica(logo, ventana):
    #termino cuadratico etiqueta lado (0, 1)
    termino_cuadratico_etiqueta = Label(
        ventana,
        text="Termino\nCuadratico (a)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_cuadratico_etiqueta.grid(
        column=0,
        row=1,
        pady=2
    )

    #terminio lineal etiqueta lado (0, 2)
    termino_lineal_etiqueta = Label(
        ventana,
        text="Termino\nLineal (b)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_lineal_etiqueta.grid(
        column=0,
        row=2,
        pady=2
    )

    #termino independiente etiqueta lado (0, 3)
    termino_independiente_etiqueta = Label(
        ventana,
        text="Termino\nIndependiente (c)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_independiente_etiqueta.grid(
        column=0,
        row=3,
        padx=5
    )

    #termino cuadratico caja de texto lado (1, 1)
    termino_cuadratico_texto = Entry(
        ventana,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_cuadratico_texto.grid(
        column=1,
        columnspan=3,
        row=1,
    )

    #termino lineal caja de texto lado (1, 2)
    termino_lineal_texto = Entry(
        ventana,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_lineal_texto.grid(
        column=1,
        columnspan=3,
        row=2,
    )

    #termino independiente caja de texto lado (1, 3)
    termino_independiente_texto = Entry(
        ventana,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_independiente_texto.grid(
        column=1,
        columnspan=3,
        row=3,
    )

    #signo discriminativo triangulo lado (0, 5)
    signo_discriminativo_triangulo = Label(
        ventana,
        text="Δ:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37"
    )
    signo_discriminativo_triangulo.grid(
        column=0,
        columnspan=2,
        row=5,
    )

    #signo discriminativo resultado lado (0, 6)
    signo_discriminativo_resultado = Label(
        ventana,
        text="Δ = b² - 4ac",
        font="Calibri 12",
        justify="center",
        background="gray93",
        foreground="gray39"
    )
    signo_discriminativo_resultado.grid(
        column=0,
        columnspan=2,
        row=6,
    )

    #ecuacion general etiqueta lado (0, 7)
    ecuacion_general_etiqueta = Label(
        ventana,
        text="Ecuación General:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37",
    )
    ecuacion_general_etiqueta.grid(
        column=0,
        columnspan=2,
        row=7,
        padx=15,
        pady=2,
    )

    #ecuacion general resultado lado (0, 8)
    ecuacion_general_resultado = Label(
        ventana,
        text="x12 = (-b ∓ √(b² - 4ac)) / (2a)",
        font="Calibri 12",
        justify="center",
        background="gray93",
        foreground="gray39",
    )
    ecuacion_general_resultado.grid(
        column=0,
        columnspan=2,
        row=8,
        rowspan=5,
        padx=15,
        pady=5,
    )

    #x1 etiqueta lado (2, 9)
    x1_etiqueta = Label(
        ventana,
        text="x1:",
        font="LiberationSans 18",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    x1_etiqueta.grid(
        column=2,
        row=9,
    )

    #x1 resultado lado (2, 10)
    x1_resultado = Label(
        ventana,
        font="Calibri 12",
        background="gray93",
        foreground="gray39"
    )
    x1_resultado.grid(
        column=2,
        row=10,
        pady=5
    )

    #x2 etiqueta lado (3, 9)
    x2_etiqueta = Label(
        ventana,
        text="x2:",
        font="LiberationSans 18",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    x2_etiqueta.grid(
        column=3,
        row=9,
    )

    #x2 resultado lado (3, 10)
    x2_resultado = Label(
        ventana,
        font="Calibri 12",
        background="gray93",
        foreground="gray39"
    )
    x2_resultado.grid(
        column=3,
        row=10,
        pady=5,
        padx=5,
    )

    #vertice etiqueta lado (2, 5)
    vertice_etiqueta = Label(
        text="Vertice:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37",
    )
    vertice_etiqueta.grid(
        column=2,
        columnspan=2,
        row=5,
    )

    #vertice resultado lado (2, 6)
    vertice_resultado = Label(
        ventana,
        text="V = (-b / (2a), ((4ac) - (b²)) / (4a))",
        font="Calibri 12",
        background="gray93",
        foreground="gray39",
    )
    vertice_resultado.grid(
        column=2,
        columnspan=2,
        row=6,
        rowspan=3,
        pady=5,
        padx=5
    )

    def graficar(a, b, c, signo_discriminativo, **kwards):
        plt.clf()
        if signo_discriminativo >= 0:
            plt.axvline(kwards["x1"], color='green', lw=1, label=r'$x_1$')
            plt.axvline(kwards["x2"], color='red', lw=1, label=r'$x_2$')

        eje_parabola = -b / (2*a)

        x = np.linspace(eje_parabola-8, eje_parabola+8, 100)
        y = (a*(x**2)) + (b*x) + c

        plt.plot(x, y, 'r.', label=r'$y$')
        plt.axvline(
            kwards["vertice"][0],
            color='gray',
            lw=1,
            label=r'$VerticeY$'
        )
        plt.axhline(
            kwards["vertice"][1],
            color='brown',
            lw=1,
            label=r'$VerticeX$'
        )
        plt.plot(
            kwards["vertice"][0],
            kwards["vertice"][1],
            'y.',
            label='vertice'
        )

        plt.title('f(x)')
        plt.xlabel('x')
        plt.ylabel(r'$y=x^2$')
        plt.grid(True)

        plt.axhline(0, color='blue', lw=1)
        plt.axvline(0, color='blue', lw=1)

        plt.legend()

        plt.show()

    def ecuacion():
        try:
            a = float(termino_cuadratico_texto.get())
            b = float(termino_lineal_texto.get())
            c = float(termino_independiente_texto.get())

            limpiar_entradas(
                termino_cuadratico_texto,
                termino_lineal_texto,
                termino_independiente_texto
            )
        except:
            limpiar_entradas(
                termino_cuadratico_texto,
                termino_lineal_texto,
                termino_independiente_texto
            )

            termino_cuadratico_texto.insert(0, "Solamente números")
            termino_lineal_texto.insert(0, "Solamente números")
            termino_independiente_texto.insert(0, "Solamente números")
            limpiar_grafica()
            return

        if(a == 1 and b == 1):
            ecuacion_general_resultado["text"] = f"x² + x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b**2)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif(a == 1 and b == -1):
            ecuacion_general_resultado["text"] = f"x² - x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b**2)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif(a == -1 and b == 1):
            ecuacion_general_resultado["text"] = f"- x² + x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b**2)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif(a == -1 and b == -1):
            ecuacion_general_resultado["text"] = f"- x² - x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b**2)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif((a != 1 or a != -1) and b == 1):
            ecuacion_general_resultado["text"] = f"{int(a)}x² + x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b*-1)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif((a != 1 or a != -1) and b == -1):
            ecuacion_general_resultado["text"] = f"{int(a)}x² - x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b*-1)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif(a == 1 and (b != 1 or b != -1)):
            ecuacion_general_resultado["text"] = f"x² + ({int(b)})x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b*-1)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        elif(a == -1 and (b != 1 or b != -1)):
            ecuacion_general_resultado["text"] = f"- x² + ({int(b)})x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b*-1)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"
        else:
            ecuacion_general_resultado["text"] = f"{int(a)}x² + ({int(b)})x + ({int(c)}) = 0\n\nx12 = (-{int(b)} ∓ √({int(b)}² - 4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = (-({int(b)}) ∓ √(({int(b)})² -4({int(a)})({int(c)}))) / (2({int(a)}))\n\nx12 = ({int(b*-1)} ∓ √({int(b*-1)} + ({int(-4*a*c)}))) / ({int(2*a)})\n\nx12 = ({int(b*-1)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)})"

        signo_discriminativo = b**2 - 4*a*c
        signo_discriminativo_resultado["text"] = f"Δ = ({int(b)})² - 4({int(a)})({int(c)})\n\nΔ = ({int(b)**2}) - ({int(4*a*c)})\n\nΔ = {signo_discriminativo}"

        vertice = (-b / (a*2), ((4*a*c) - (b**2))/(4*a))
        vertice_resultado['text'] = f"V = (-({int(b)}) / (({int(a)})2), (4({int(a)})({int(c)}) - ({int(b)})²) / (4({int(a)})))\n\nV = (({-int(b)}) / ({int(a)*2}), ({int(4*a*c)} - {int(b)**2}) / ({int(4*a)}))\n\nV = ({vertice[0]}, ({int(4*a*c)} - {int(b)**2}) / ({int(4*a)}))\n\nV = ({vertice[0]}, ({int((4*a*c) - (b**2))}) / ({int(4*a)}))\n\nV = ({vertice[0]}, {vertice[1]})"

        if signo_discriminativo >= 0:
            x1 = ((b*(-1)) + (sqrt((b**2) + (-4*a*c)))) / (2*a)
            x2 = ((b*(-1)) - (sqrt((b**2) + (-4*a*c)))) / (2*a)

            x1_resultado["text"] = f"x1 = ({int(b*-1)} + {int(sqrt((b**2) + (-4*a*c)))}) / ({int(2*a)})\n\nx1 = ({int((b*(-1))) + (int(sqrt((b**2) + (-4*a*c))))}) / ({int(2*a)})\n\nx1 = {x1}"
            x2_resultado["text"] = f"x2 = ({int(b*-1)} - {int(sqrt((b**2) + (-4*a*c)))}) / ({int(2*a)})\n\nx2 = ({int((b*(-1))) - (int(sqrt((b**2) + (-4*a*c))))}) / ({int(2*a)})\n\nx2 = {x2}"

            graficar(
                a,
                b,
                c,
                signo_discriminativo,
                x1=x1,
                x2=x2,
                vertice=vertice
            )
        else:
            x1_resultado["text"] = f"x1 = ({int(b*-1)} + {int(sqrt(-((b**2) + (-4*a*c))))}i) / ({int(2*a)})"
            x2_resultado["text"] = f"x2 = ({int(b*-1)} - {int(sqrt(-((b**2) + (-4*a*c))))}i) / ({int(2*a)})"

            graficar(a, b, c, signo_discriminativo, vertice=vertice)

    comenzar_ecuacion = Button(
        ventana,
        text="APLICAR ECUACIÓN",
        font="Calibri 30",
        background="white",
        foreground="gray25",
        command=ecuacion,
        relief="groove",
        overrelief="raised"
    )
    comenzar_ecuacion.grid(
        column=0,
        columnspan=4,
        row=4,
        pady=5
    )

    ventana.bell()

    limpiar_grafica()
