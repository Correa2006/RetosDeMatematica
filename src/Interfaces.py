import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageTk
from math import sqrt
from .Utilidades import limpiar_grafica, limpiar_entradas, ocultar_widgets
from .polinomio.polinomio import Imprimir_Polinomio, Agregar_Terminos
from .polinomio.polinomio import Termino, Incognita, Sumar_Polinomios
from .polinomio.polinomio import Restar_Polinomios, Multiplicar_Polinomios
from .polinomio.polinomio import Dividir_Polinomios


def main(**kwargs):
    ventana = tk.Tk()
    ventana.title("Pydrático")
    ventana.tk_setPalette(background="gray93")
    ventana.wm_attributes("-topmost", 1)

    imagen = Image.open("media/logo.png")
    logo = ImageTk.PhotoImage(imagen)

    #####################################################
    #frame: frame

    #frame (1, 0)
    frame = tk.LabelFrame(
        ventana
    )
    frame.grid(
        column=0,
        row=1,
        ipadx=5,
        ipady=5
    )

    pydratico = tk.Label(
        frame,
        text="PyDrático",
        justify="center",
        font="LiberationSans 50",
        background="gray93",
        foreground="gray13"
    )
    pydratico.grid(
        column=0,
        row=0
    )

    #frame: frame
    #####################################################

    #####################################################
    #menu: menu bar

    #menu bar
    menu = tk.Menu(ventana)
    ventana.config(menu=menu)

    #menu item herramientas
    herramientas_menu = tk.Menu(menu)

    #menu add cascade herramientas
    menu.add_cascade(
        label="Herramientas",
        menu=herramientas_menu
    )

    #command ecuacion cuadratica
    herramientas_menu.add_command(
        label="Ecuación Cuadrática",
        command=lambda: kwargs["ecuacion_cuadratica"](frame)
    )

    #command polinomios
    herramientas_menu.add_command(
        label="Polinomios",
        command=lambda: kwargs["polinomios"](frame)
    )

    #menu: menu bar
    #####################################################

    #####################################################
    #frame: ecabezado_frame

    #encabezado_frame (0,0)
    encabezado_frame = tk.Frame(ventana)
    encabezado_frame.grid(
        column=0,
        row=0,
    )

    #logo_etiqueta (0, 0)
    logo_etiqueta = tk.Label(
        encabezado_frame,
        image=logo
    )
    logo_etiqueta.grid(
        column=0,
        row=0,
        padx=5,
        pady=5
    )

    #encabezado (1, 0)
    encabezado = tk.Label(
        encabezado_frame,
        text="Republica Bolivariana de Venezuela\nLiceo Antonio José Pacheco\n\"Reto de matemáticas\"",
        justify="center",
        font="LiberationSans 16",
        background="gray93",
        foreground="gray13"
    )
    encabezado.grid(
        column=1,
        columnspan=2,
        row=0,
        padx=5,
        pady=15
    )

    #datos_alumno (3, 0)
    datos_alumno = tk.Label(
        encabezado_frame,
        text="José Correa\n4to año\nSección \"D\"",
        justify="right",
        background="gray93",
        foreground="gray37"
    )
    datos_alumno.grid(
        column=3,
        row=0,
        padx=5
    )

    #frame: ecabezado_termino
    #####################################################

    ventana.bell()
    ventana.mainloop()


def ecuacion_cuadratica(frame):
    ocultar_widgets(frame)

    frame["text"] = "Ecuación Cuadrática"

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

        if a == 0:
            limpiar_entradas(
                termino_cuadratico_texto,
                termino_lineal_texto,
                termino_independiente_texto
            )
            termino_cuadratico_texto.insert(0, "No puede ser igual a cero")
            return

        ecuacion_general_resultado["text"] = "1) "

        if(a == 1 and b == 1):
            ecuacion_general_resultado["text"] += f"x² + x + ({int(c)}) = 0"
        elif(a == 1 and b == -1):
            ecuacion_general_resultado["text"] += f"x² - x + ({int(c)}) = 0"
        elif(a == -1 and b == 1):
            ecuacion_general_resultado["text"] += f"- x² + x + ({int(c)}) = 0"
        elif(a == -1 and b == -1):
            ecuacion_general_resultado["text"] += f"- x² - x + ({int(c)}) = 0"
        elif((a != 1 or a != -1) and b == 1):
            ecuacion_general_resultado["text"] += f"{int(a)}x² + x + ({int(c)}) = 0"
        elif((a != 1 or a != -1) and b == -1):
            ecuacion_general_resultado["text"] += f"{int(a)}x² - x + ({int(c)}) = 0"
        elif(a == 1 and (b != 1 or b != -1)):
            ecuacion_general_resultado["text"] += f"x² + ({int(b)})x + ({int(c)}) = 0"
        elif(a == -1 and (b != 1 or b != -1)):
            ecuacion_general_resultado["text"] += f"- x² + ({int(b)})x + ({int(c)}) = 0"
        else:
            ecuacion_general_resultado["text"] += f"{int(a)}x² + ({int(b)})x + ({int(c)}) = 0"

        ecuacion_general_resultado["text"] += f"\n\n2) x12 = (-({int(b)}) ∓ √(({int(b)})² - 4({int(a)})({int(c)}))) / (2({int(a)}))"
        ecuacion_general_resultado["text"] += f"\n\n3) x12 = ({int(-1*b)} ∓ √({int(b**2)} + ({int(-4*a*c)}))) / ({int(2*a)})"
        ecuacion_general_resultado["text"] += f"\n\n4) x12 = ({int(-1*b)} ∓ √({int((b**2) + (-4*a*c))})) / ({int(2*a)}))"

        signo_discriminativo = b**2 - 4*a*c
        signo_discriminativo_resultado["text"] = f"1) Δ = ({int(b)})² - 4({int(a)})({int(c)})"
        signo_discriminativo_resultado["text"] += f"\n\n2) Δ = ({int(b)**2}) - ({int(4*a*c)})"
        signo_discriminativo_resultado["text"] += f"\n\n3) Δ = {signo_discriminativo}"

        vertice = (-b / (a*2), ((4*a*c) - (b**2))/(4*a))
        vertice_resultado['text'] = f"1) V = (-({int(b)}) / (({int(a)})2), (4({int(a)})({int(c)}) - ({int(b)})²) / (4({int(a)})))"
        vertice_resultado['text'] += f"\n\n2) V = (({-int(b)}) / ({int(a)*2}), ({int(4*a*c)} - {int(b)**2}) / ({int(4*a)}))"
        vertice_resultado['text'] += f"\n\n3) V = ({vertice[0]}, ({int(4*a*c)} - {int(b)**2}) / ({int(4*a)}))"
        vertice_resultado['text'] += f"\n\n4) V = ({vertice[0]}, ({int((4*a*c) - (b**2))}) / ({int(4*a)}))"
        vertice_resultado['text'] += f"\n\n5) V = ({vertice[0]}, {vertice[1]})"

        x1_resultado["text"] = x2_resultado["text"] = "5) "

        if signo_discriminativo >= 0:
            x1 = ((b*(-1)) + (sqrt((b**2) + (-4*a*c)))) / (2*a)
            x2 = ((b*(-1)) - (sqrt((b**2) + (-4*a*c)))) / (2*a)

            x1_resultado["text"] += f"x1 = ({int(b*-1)} + {int(sqrt((b**2) + (-4*a*c)))}) / ({int(2*a)})"
            x1_resultado["text"] += f"\n\n6) x1 = ({int((b*(-1))) + (int(sqrt((b**2) + (-4*a*c))))}) / ({int(2*a)})"
            x1_resultado["text"] += f"\n\n7) x1 = {x1}"

            x2_resultado["text"] += f"x2 = ({int(b*-1)} - {int(sqrt((b**2) + (-4*a*c)))}) / ({int(2*a)})"
            x2_resultado["text"] += f"\n\n6) x2 = ({int((b*(-1))) - (int(sqrt((b**2) + (-4*a*c))))}) / ({int(2*a)})"
            x2_resultado["text"] += f"\n\n7) x2 = {x2}"

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
            x1_resultado["text"] += f"x1 = ({int(b*-1)} + {int(sqrt(-((b**2) + (-4*a*c))))}i) / ({int(2*a)})"
            x2_resultado["text"] += f"x2 = ({int(b*-1)} - {int(sqrt(-((b**2) + (-4*a*c))))}i) / ({int(2*a)})"

            graficar(a, b, c, signo_discriminativo, vertice=vertice)

    #####################################################
    #frame: Ingresar Terminos

    #ingresar terminos lado (0, 0)
    ingresar_terminos = tk.LabelFrame(
        frame,
        text="Ingresar Términos"
    )
    ingresar_terminos.grid(
        column=0,
        row=0,
        padx=2,
        pady=2,
        ipadx=5,
        ipady=5
    )

    #termino cuadratico etiqueta lado (0, 0)
    termino_cuadratico_etiqueta = tk.Label(
        ingresar_terminos,
        text="Termino\nCuadratico (a)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_cuadratico_etiqueta.grid(
        column=0,
        row=0,
        pady=2
    )

    #terminio lineal etiqueta lado (0, 1)
    termino_lineal_etiqueta = tk.Label(
        ingresar_terminos,
        text="Termino\nLineal (b)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_lineal_etiqueta.grid(
        column=0,
        row=1,
        pady=2
    )

    #termino independiente etiqueta lado (0, 2)
    termino_independiente_etiqueta = tk.Label(
        ingresar_terminos,
        text="Termino\nIndependiente (c)",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    termino_independiente_etiqueta.grid(
        column=0,
        row=2,
        padx=5
    )

    #termino cuadratico caja de texto lado (1, 0)
    termino_cuadratico_texto = tk.Entry(
        ingresar_terminos,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_cuadratico_texto.grid(
        column=1,
        columnspan=2,
        row=0,
    )

    #termino lineal caja de texto lado (1, 1)
    termino_lineal_texto = tk.Entry(
        ingresar_terminos,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_lineal_texto.grid(
        column=1,
        row=1,
    )

    #termino independiente caja de texto lado (1, 2)
    termino_independiente_texto = tk.Entry(
        ingresar_terminos,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    termino_independiente_texto.grid(
        column=1,
        row=2,
    )

    #comenzar ecuacion lado (0, 3)
    comenzar_ecuacion = tk.Button(
        ingresar_terminos,
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
        columnspan=2,
        row=3,
        pady=5
    )

    #frame: Ingresar Terminos
    #####################################################

    #####################################################
    #frame: Datos de la Ecuacion

    #datos ecuacion lado (0, 1)
    datos_ecuacion = tk.LabelFrame(
        frame,
        text="Datos de la Ecuación"
    )
    datos_ecuacion.grid(
        column=1,
        row=0,
        padx=2,
        pady=2,
        ipadx=5,
        ipady=5
    )

    #signo discriminativo triangulo lado (0, 0)
    signo_discriminativo_triangulo = tk.Label(
        datos_ecuacion,
        text="Δ:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37"
    )
    signo_discriminativo_triangulo.grid(
        column=0,
        row=0,
    )

    #signo discriminativo resultado lado (0, 1)
    signo_discriminativo_resultado = tk.Label(
        datos_ecuacion,
        text="Δ = b² - 4ac",
        font="Calibri 12",
        justify="left",
        background="gray93",
        foreground="gray39"
    )
    signo_discriminativo_resultado.grid(
        column=0,
        row=1,
    )

    #ecuacion general etiqueta lado (0, 2)
    ecuacion_general_etiqueta = tk.Label(
        datos_ecuacion,
        text="Ecuación General:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37",
    )
    ecuacion_general_etiqueta.grid(
        column=0,
        row=2,
        padx=15,
        pady=2,
    )

    #ecuacion general resultado lado (0, 3)
    ecuacion_general_resultado = tk.Label(
        datos_ecuacion,
        text="x12 = (-b ∓ √(b² - 4ac)) / (2a)",
        font="Calibri 12",
        justify="left",
        background="gray93",
        foreground="gray39",
    )
    ecuacion_general_resultado.grid(
        column=0,
        row=3,
        rowspan=5,
        padx=15,
        pady=5,
    )

    #vertice etiqueta lado (1, 0)
    vertice_etiqueta = tk.Label(
        datos_ecuacion,
        text="Vertice:",
        font="LiberationSans 18",
        background="gray93",
        foreground="gray37",
    )
    vertice_etiqueta.grid(
        column=1,
        columnspan=2,
        row=0,
    )

    #vertice resultado lado (1, 1)
    vertice_resultado = tk.Label(
        datos_ecuacion,
        text="V = (-b / (2a), ((4ac) - (b²)) / (4a))",
        justify="left",
        font="Calibri 12",
        background="gray93",
        foreground="gray39",
    )
    vertice_resultado.grid(
        column=1,
        columnspan=2,
        row=1,
        rowspan=3,
        pady=5,
        padx=5
    )

    #x1 etiqueta lado (1, 4)
    x1_etiqueta = tk.Label(
        datos_ecuacion,
        text="x1:",
        font="LiberationSans 18",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    x1_etiqueta.grid(
        column=1,
        row=4,
    )

    #x1 resultado lado (1, 5)
    x1_resultado = tk.Label(
        datos_ecuacion,
        font="Calibri 12",
        justify="left",
        background="gray93",
        foreground="gray39"
    )
    x1_resultado.grid(
        column=1,
        row=5,
        pady=5
    )

    #x2 etiqueta lado (2, 4)
    x2_etiqueta = tk.Label(
        datos_ecuacion,
        text="x2:",
        font="LiberationSans 18",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    x2_etiqueta.grid(
        column=2,
        row=4,
    )

    #x2 resultado lado (2, 5)
    x2_resultado = tk.Label(
        datos_ecuacion,
        font="Calibri 12",
        justify="left",
        background="gray93",
        foreground="gray39"
    )
    x2_resultado.grid(
        column=2,
        row=5,
        pady=5,
        padx=5,
    )

    #frame: Datos de la Ecuacion
    #####################################################

    limpiar_grafica()


def polinomios(frame):
    ocultar_widgets(frame)
    frame["text"] = "Suma, Resta, Multiplicación y División de Polinomios"

    polinomio_lista = []
    polinomio1_lista = []
    polinomio2_lista = []

    def ingresar_termino_F(pol):
        try:
            exponente = int(exponente_texto.get())
            coeficiente = float(coeficiente_texto.get())

            limpiar_entradas(
                exponente_texto,
                coeficiente_texto,
            )
        except:
            limpiar_entradas(
                exponente_texto,
                coeficiente_texto,
            )

            exponente_texto.insert(0, "Solamente números")
            coeficiente_texto.insert(0, "Solamente números")

            return

        if exponente >= 0:
            termino = Termino(
                coeficiente,
                [
                    Incognita("x", exponente)
                ]
            )

            pol.append(termino)
            Agregar_Terminos(pol)

            polinomio_etiqueta["text"] = Imprimir_Polinomio(pol)
        else:
            exponente_texto.insert(0, "Debe ser positivo")

        if coeficiente == 0:
            coeficiente_texto.insert(0, "No puede ser igual a cero")

    def agregar_polinomio(pol, pol1, pol2):
        if pol and not pol1:
            pol1.clear()

            for termino in pol:
                pol1.append(termino)

            Agregar_Terminos(pol1)

            polinomio1_etiqueta["text"] = Imprimir_Polinomio(pol1)

        elif pol and not pol2:
            pol2.clear()

            for termino in pol:
                pol2.append(termino)

            Agregar_Terminos(pol2)

            polinomio2_etiqueta["text"] = Imprimir_Polinomio(pol2)

        pol.clear()
        polinomio_etiqueta["text"] = "..."

    def aplicar_operacion_F(pol1, pol2):
        if pol1 and pol2:
            #agregando resultado_frame lado (0, 2)
            resultado_frame.grid(
                column=0,
                columnspan=2,
                row=2,
                padx=2,
                pady=2,
                ipadx=5,
                ipady=5
            )

            ocultar_widgets(resultado_frame)

            #resultado_etiqueta lado (1, 0)
            resultado_etiqueta = tk.Label(
                resultado_frame,
                justify="right",
                font="Calibri 12",
                background="gray93",
                foreground="gray39",
            )
            resultado_etiqueta.grid(
                column=1,
                row=0,
                padx=5,
                pady=5
            )

            #resto_etiqueta lado (0, 0)
            dividendo_resto_etiqueta = tk.Label(
                resultado_frame,
                justify="left",
                font="Calibri 12",
                background="gray93",
                foreground="gray39",
            )
            dividendo_resto_etiqueta.grid(
                column=0,
                row=0,
                rowspan=10,
                padx=5,
                pady=5
            )

            operador = operacion_var.get()
            operacion_aplicada = {
                "+": Sumar_Polinomios,
                "-": Restar_Polinomios,
                "×": Multiplicar_Polinomios,
                "÷": Dividir_Polinomios
            }
            resultado = (operacion_aplicada[operador](pol1, pol2))[1]
            resultado_str = ""

            if operador != "÷":
                if dividendo_resto_etiqueta["text"]:
                    dividendo_resto_etiqueta["text"] = ""

                pol1 = Imprimir_Polinomio(pol1)
                pol2 = Imprimir_Polinomio(pol2)
                resultado_str += pol1 + "\n"
                resultado_str += pol2 + "\n"
                resultado_str += "-" * (len(pol1) + len(pol2)) + "\n"
                resultado_str += resultado

                resultado_etiqueta["text"] = ""
                resultado_etiqueta["text"] = resultado_str

                if operador == "+":
                    operaciones["text"] = "Suma"
                    frame["text"] = "Suma de Polinomios"
                elif operador == "-":
                    operaciones["text"] = "Resta"
                    frame["text"] = "Resta de Polinomios"
                elif operador == "×":
                    operaciones["text"] = "Multiplicación"
                    frame["text"] = "Multiplicación de Polinomios"
            else:
                resultado_etiqueta["justify"] = "left"
                operaciones["text"] = "División"
                frame["text"] = "División de Polinomios"

                if pol1[0].incognitas:
                    grado_dividendo = pol1[0].incognitas[0].exponente
                else:
                    grado_dividendo = 0

                if pol2[0].incognitas:
                    grado_divisor = pol2[0].incognitas[0].exponente
                else:
                    grado_divisor = 0

                if grado_dividendo < grado_divisor:
                    resultado_str = "No se puede dividir"
                else:
                    resultado_str += "¦"
                    resultado_str += Imprimir_Polinomio(pol2) + "\n"
                    resultado_str += "--" * len(Imprimir_Polinomio(pol2)) + "\n"
                    resultado_str += Imprimir_Polinomio(
                        (operacion_aplicada[operador](pol1, pol2))[0]
                    )

                    dividendo_resto_etiqueta["text"] = Imprimir_Polinomio(pol1) + "\n"
                    dividendo_resto_etiqueta["text"] += resultado

                resultado_etiqueta["text"] = resultado_str

            polinomio1_etiqueta["text"] = "..."
            polinomio2_etiqueta["text"] = "..."
            polinomio1_lista.clear()
            polinomio2_lista.clear()

    #####################################################
    #frame: Ingresar Terminos

    #ingresar terminos lado (0, 0)
    ingresar_terminos = tk.LabelFrame(
        frame,
        text="Ingresar Términos"
    )
    ingresar_terminos.grid(
        column=0,
        row=0,
        rowspan=2,
        padx=2,
        pady=2,
        ipadx=5,
        ipady=5
    )

    #exponente etiqueta lado (0, 0)
    exponente_etiqueta = tk.Label(
        ingresar_terminos,
        text="Exponente",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    exponente_etiqueta.grid(
        column=0,
        row=0,
        pady=5
    )

    #coeiciente etiqueta lado (0, 1)
    coeficiente_etiqueta = tk.Label(
        ingresar_terminos,
        text="Coeficiente",
        justify="center",
        font="bold 12",
        background="gray93",
        foreground="gray39"
    )
    coeficiente_etiqueta.grid(
        column=0,
        row=1,
        pady=5
    )

    #exponente caja de texto lado (1, 0)
    exponente_texto = tk.Entry(
        ingresar_terminos,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    exponente_texto.grid(
        column=1,
        columnspan=2,
        row=0,
    )

    #coeficiente caja de texto lado (1, 1)
    coeficiente_texto = tk.Entry(
        ingresar_terminos,
        font="bold 14",
        bg="white",
        fg="gray1",
        relief="ridge"
    )
    coeficiente_texto.grid(
        column=1,
        row=1,
    )

    #ingresar termino lado (0, 2)
    ingresar_termino = tk.Button(
        ingresar_terminos,
        text="INGRESAR TÉRMINO",
        font="Calibri 30",
        background="white",
        foreground="gray25",
        command=lambda: ingresar_termino_F(polinomio_lista),
        relief="groove",
        overrelief="raised"
    )
    ingresar_termino.grid(
        column=0,
        columnspan=2,
        row=2,
        pady=5
    )

    #frame: Ingresar Terminos
    #####################################################

    #####################################################
    #frame: Polinomio

    #ingresar terminos lado (1, 0)
    polinomio = tk.LabelFrame(
        frame,
        text="Polinomio"
    )
    polinomio.grid(
        column=1,
        row=0,
        padx=2,
        pady=2,
        ipadx=5,
        ipady=5
    )

    #polinomio etiqueta lado (0, 0)
    polinomio_etiqueta = tk.Label(
        polinomio,
        text="...",
        font="LiberationSans 12",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    polinomio_etiqueta.grid(
        column=0,
        row=0,
        padx=5,
        pady=5
    )

    #cargar lado (1, 0)
    cargar = tk.Button(
        polinomio,
        text="CARGAR",
        font="Calibri 14",
        background="white",
        foreground="gray25",
        command=lambda: agregar_polinomio(
            polinomio_lista,
            polinomio1_lista,
            polinomio2_lista
        ),
        relief="groove",
        overrelief="raised"
    )
    cargar.grid(
        column=1,
        row=0,
        padx=5,
        pady=5
    )

    #frame: Ingresar Polinomio
    #####################################################

    #####################################################
    #frame: operaciones

    #string var
    operacion_var = tk.StringVar(value="+")

    #operaciones lado (1, 0)
    operaciones = tk.LabelFrame(
        frame,
        text="Operaciones"
    )
    operaciones.grid(
        column=1,
        row=1,
        padx=2,
        pady=2,
        ipadx=5,
        ipady=5
    )

    #polinomio1 etiqueta lado (0, 0)
    polinomio1_etiqueta = tk.Label(
        operaciones,
        text="...",
        font="LiberationSans 12",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    polinomio1_etiqueta.grid(
        column=0,
        row=0,
        padx=5,
        pady=5
    )

    #operacion lado (0, 1)
    operacion = tk.OptionMenu(
        operaciones,
        operacion_var,
        "+",
        "-",
        "×",
        "÷"
    )
    operacion.grid(
        column=1,
        row=0,
        padx=5,
        pady=5
    )

    #polinomio2 etiqueta lado (2, 0)
    polinomio2_etiqueta = tk.Label(
        operaciones,
        text="...",
        font="LiberationSans 12",
        justify="left",
        background="gray93",
        foreground="gray37"
    )
    polinomio2_etiqueta.grid(
        column=2,
        row=0,
        padx=5,
        pady=5
    )

    #aplicar operacion lado (0, 1)
    aplicar_operacion = tk.Button(
        operaciones,
        text="APLICAR OPERACIÓN",
        font="Calibri 30",
        background="white",
        foreground="gray25",
        command=lambda: aplicar_operacion_F(
            polinomio1_lista,
            polinomio2_lista
        ),
        relief="groove",
        overrelief="raised"
    )
    aplicar_operacion.grid(
        column=0,
        columnspan=3,
        row=1,
        padx=5,
        pady=5
    )

    #frame: operaciones
    #####################################################

    #####################################################
    #frame: resultado

    resultado_frame = tk.LabelFrame(
        frame,
        text="Resultado"
    )
