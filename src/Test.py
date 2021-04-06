from fractions import Fraction
from .polinomio.polinomio import Incognita, Termino
from .polinomio.polinomio import Agregar_Terminos, Dividir_Polinomios
from .polinomio.polinomio import Imprimir_Polinomio


###############################################################
#Pruebas: Incognita

def Prueba_Incognita():
    x1 = Incognita()
    x6 = Incognita(exponente=6)
    z6 = Incognita()

    print("INCOGNITA")
    print("---------------------------------------------------")
    print("BASE")

    for i in ["xy", "2", 10, "z"]:
        z6.base = i
        print(z6)

    print("EXPONENTE")

    for i in [10, 10.0, "", 6]:
        z6.exponente = i
        print(z6)

    print("MULTIPLICACION")

    print(x1 * 2)
    print((x1 * x6)[0])
    print((x1 * z6)[0], (x1 * z6)[1])

    print("DIVISION")

    print(x1 / 10.0)
    print((x1 / z6)[0], (x1 / z6)[1])
    print((x1 / x6)[0])

    print("IGUAL")

    print(x1 == x1)
    print(x1 == x6)
    print(x1 == z6)

    print("DIFERENTE")

    print(x1 != x1)
    print(x1 != x6)
    print(x1 != z6)

    print("MENOR")

    print(x1 < x6)
    print(x6 < x1)
    print(x1 < z6)

    print("MAYOR")

    print(x1 > x6)
    print(x6 > x1)
    print(x1 > z6)

    print("NEGATIVO")

    print(-x1)
    print(-(-x1))


###############################################################
#Pruebas: Termino

def Prueba_Termino():
    print("TERMINO")
    print("---------------------------------------------------")
    print("COEFICIENTE")

    print(Termino(""))
    print(Termino(3j))
    print(Termino(Fraction(4, 5)))
    print(Termino(0.8))
    print(Termino(10))

    print("INCOGNITAS")
    print(Termino(incognitas={}))
    print(Termino(incognitas=""))
    print(Termino(incognitas=[
        Incognita("a"),
        Incognita("z"),
    ]))
    print(Termino(incognitas=[
        Incognita("z"),
        Incognita("A"),
    ]))
    print(Termino(incognitas=[
        Incognita("z", 6),
        Incognita("a"),
        Incognita("z", -1),
    ]))

    print("IGUAL")

    a11 = Termino(
        2,
        [Incognita("a", 11)],
    )
    b1 = Termino(
        2,
        [Incognita("b")],
    )
    ab11c7 = Termino(
        5 / 4,
        [
            Incognita("a"),
            Incognita("b", 11),
            Incognita("c", -7),
        ]
    )
    ab11c71 = Termino(
        2,
        [
            Incognita("a"),
            Incognita("b", 11),
            Incognita("c", -7),
        ]
    )
    x2z = Termino(
        1,
        [
            Incognita("x", -2),
            Incognita("z"),
        ]
    )
    a1 = Termino(
        10,
        [Incognita("a")]
    )

    print(a11 == b1)
    print(b1 == a11)
    print(ab11c7 == ab11c71)
    print(2 == x2z)

    print("DESIGUAL")

    print(a11 != b1)
    print(b1 != a11)
    print(ab11c7 != ab11c7)
    print(2 != x2z)

    print("MENOR")

    print(a11 < b1)
    print(b1 < a11)
    print(ab11c7 < ab11c7)
    print(2 < x2z)
    print(a1 < (-a1))
    print((-a1) < a1)

    print("MAYOR")

    print(a11 > b1)
    print(b1 > a11)
    print(ab11c7 > ab11c7)
    print(2 > x2z)
    print(a1 > (-a1))
    print((-a1) > a1)

    print("SUMA")

    x1 = Termino(1, [Incognita()])
    x31 = Termino(3, [Incognita()])
    x2 = Termino(1, [Incognita(exponente=2)])
    z31 = Termino(3, [Incognita("z")])

    print(x1 + x31)
    print(x2 + x31)
    print(x1 + z31)

    print("RESTA")

    print(x1 - x31)
    print(x2 - x31)
    print(x1 - z31)

    print("MULTIPLICACION")

    a11b2mx10 = Termino(
        5,
        [
            Incognita("a", -11),
            Incognita("b", 2),
            Incognita("m"),
            Incognita("x", 10),
        ],
    )
    a1x7y2z10 = Termino(
        4,
        [
            Incognita("a", 1),
            Incognita("x", -7),
            Incognita("y", 2),
            Incognita("z", 10),
            Incognita("x", 1),
            Incognita("z", -10),
        ],
    )

    print(a11b2mx10 * a1x7y2z10)

    print("DIVISION")

    print(a11b2mx10 / a1x7y2z10)


###############################################################
#Pruebas: Polinomio


def Prueba_Polinomio():
    pol_dividendo = Agregar_Terminos([
        Termino(
            3,
            [Incognita("x", 5)]
        ),
        Termino(
            3,
            [Incognita("x", 3)]
        ),
        Termino(
            9,
            [Incognita("x", 2)]
        ),
        Termino(
            1 / 2,
            []
        )
    ])

    pol_divisor = Agregar_Terminos([
        Termino(
            1,
            [Incognita("x", 1)]
        ),
        Termino(
            5,
            []
        ),
    ])

    print("POLINOMIO")
    print("---------------------------------------------------")

    print("DIVIDENDO")
    print(Imprimir_Polinomio(pol_dividendo))
    print("DIVISOR")
    print(Imprimir_Polinomio(pol_divisor))
    print("COCIENTE")
    print(Imprimir_Polinomio(Dividir_Polinomios(pol_dividendo, pol_divisor)))
