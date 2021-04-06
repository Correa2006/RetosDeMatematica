import string
from fractions import Fraction

###############################################################
#clase Incognita


class Incognita:

    def __AgregarBase(self, base):
        if type(base) is str and len(base) != 0:
            char = base[0]
            if not char in string.punctuation and not char in string.digits:
                return char
        return "x"

    def __AgregarExponente(self, exponente):
        if type(exponente) is int:
            return exponente
        else:
            return 1

    def __init__(self, base="x", exponente=1):
        self.__base = self.__AgregarBase(base)
        self.__exponente = self.__AgregarExponente(exponente)

    def __str__(self):
        return self.__base + "^" + str(self.__exponente)

    def __mul__(self, incognita):
        if type(incognita) is Incognita:
            producto = []
            if incognita.base == self.__base:
                producto.append(Incognita(
                    self.__base,
                    self.__exponente + incognita.exponente
                ))
            else:
                producto.append(self)
                producto.append(incognita)
            return producto
        else:
            return False

    def __truediv__(self, incognita):
        if type(incognita) is Incognita:
            cociente = []
            if incognita.base == self.__base:
                cociente.append(Incognita(
                    self.__base,
                    self.__exponente - incognita.exponente
                ))
            else:
                cociente.append(self)
                cociente.append(-incognita)
            return cociente
        else:
            False

    def __eq__(self, incognita):
        if type(incognita) == Incognita:
            return self.__base == incognita.base and self.__exponente == incognita.exponente

    def __ne__(self, incognita):
        if type(incognita) == Incognita:
            return not self == incognita

    def __gt__(self, incognita):
        if type(incognita) == Incognita:
            return self.__base == incognita.base and self.__exponente > incognita.exponente

    def __lt__(self, incognita):
        if type(incognita) == Incognita:
            return self.__base == incognita.base and self.__exponente < incognita.exponente

    def __neg__(self):
        return Incognita(self.__base, -self.__exponente)

    def __ObtenerBase(self):
        return self.__base

    def __ModificarBase(self, base):
        self.__base = self.__AgregarBase(base)

    def __EliminarBase(self):
        del self.__base

    def __ObtenerExponente(self):
        return self.__exponente

    def __ModificarExponente(self, exponente):
        self.__exponente = self.__AgregarExponente(exponente)

    def __EliminarExponente(self):
        del self.__exponente

    def copy(incognita):
        if type(incognita) is Incognita:
            return Incognita(
                incognita.base,
                incognita.exponente
            )

    base = property(
        __ObtenerBase,
        __ModificarBase,
        __EliminarBase,
        "base"
    )
    exponente = property(
        __ObtenerExponente,
        __ModificarExponente,
        __EliminarExponente,
        "exponente"
    )

###############################################################
#clase Termino


class Termino:

    def __OrdenarIncognitas(self, incognitas):
        i = 0

        while i < len(incognitas):
            j = 0

            while j < (len(incognitas) - 1):
                if incognitas[j].base > incognitas[j + 1].base:
                    incognita_acutal = incognitas[j]
                    incognitas[j] = incognitas[j + 1]
                    incognitas[j + 1] = incognita_acutal

                elif incognitas[j].base == incognitas[j + 1].base:
                    incognitas[j] = (incognitas[j + 1] * incognitas[j])[0]
                    incognitas.pop(j + 1)
                j += 1
            i += 1

    def __AgregarCoeficiente(self, coeficiente):
        if type(coeficiente) in [int, float, Fraction]:
            return coeficiente
        else:
            return 1

    def __AgregarIncognitas(self, incognitas):
        if type(incognitas) is list:
            incognitas_finales = []

            for incognita in incognitas:
                if type(incognita) is Incognita:
                    incognitas_finales.append(incognita)

            self.__OrdenarIncognitas(incognitas_finales)

            for incognita in incognitas_finales:
                if incognita.exponente == 0:
                    incognitas_finales.remove(incognita)

            return incognitas_finales
        else:
            return []

    def __init__(self, coeficiente=1, incognitas=[]):
        self.__coeficiente = self.__AgregarCoeficiente(coeficiente)
        self.__incognitas = self.__AgregarIncognitas(incognitas)

    def __str__(self):
        termino = str(self.__coeficiente)
        for incognita in self.__incognitas:
            termino += " " + str(incognita)
        return termino

    def __eq__(self, termino):
        if type(termino) is Termino:
            return self.__incognitas == termino.incognitas

    def __ne__(self, termino):
        if type(termino) is Termino:
            return not self == termino

    def __lt__(self, termino):
        if type(termino) is Termino:
            return self.__coeficiente < termino.coeficiente and self.__incognitas == termino.incognitas

    def __gt__(self, termino):
        if type(termino) is Termino:
            return self.__coeficiente > termino.coeficiente and self.__incognitas == termino.incognitas

    def __neg__(self):
        return Termino(-self.__coeficiente, self.__incognitas)

    def __add__(self, termino):
        if type(termino) is Termino:
            if self.__incognitas == termino.incognitas:
                return Termino(
                    self.__coeficiente + termino.coeficiente,
                    self.__incognitas
                )
        else:
            return False

    def __sub__(self, termino):
        if type(termino) is Termino:
            if self.__incognitas == termino.incognitas:
                return Termino(
                    self.__coeficiente - termino.coeficiente,
                    self.__incognitas
                )
        else:
            return False

    def __mul__(self, termino):
        if type(termino) is Termino:
            incognitas_producto = []
            incognitas_self = list.copy(self.__incognitas)
            incognitas_termino = list.copy(termino.incognitas)
            i_IT = 0

            while incognitas_termino or incognitas_self:
                if not incognitas_self:
                    incognitas_producto.append(
                        incognitas_termino[i_IT]
                    )
                    incognitas_termino.pop(i_IT)
                    continue
                elif not incognitas_termino:
                    incognitas_producto.append(
                        incognitas_self[0]
                    )
                    incognitas_self.pop(0)
                    continue

                if i_IT == len(incognitas_termino):
                    incognitas_producto.append(
                        incognitas_self[0]
                    )
                    incognitas_self.pop(0)
                    i_IT = 0
                    continue

                if incognitas_self[0].base == incognitas_termino[i_IT].base:
                    incognitas_producto.append(
                        (incognitas_self[0] * incognitas_termino[i_IT])[0]
                    )
                    incognitas_self.pop(0)
                    incognitas_termino.pop(i_IT)

                    i_IT = 0
                else:
                    i_IT += 1

            return Termino(
                self.__coeficiente * termino.coeficiente,
                incognitas_producto
            )
        else:
            return False

    def __truediv__(self, termino):
        if type(termino) is Termino:
            incognitas_cociente = []
            incognitas_self = list.copy(self.__incognitas)
            incognitas_termino = list.copy(termino.incognitas)
            i_IT = 0

            while incognitas_termino or incognitas_self:
                if not incognitas_self:
                    incognitas_cociente.append(
                        -incognitas_termino[i_IT]
                    )
                    incognitas_termino.pop(i_IT)
                    continue
                elif not incognitas_termino:
                    incognitas_cociente.append(
                        incognitas_self[0]
                    )
                    incognitas_self.pop(0)
                    continue

                if i_IT == len(incognitas_termino):
                    incognitas_cociente.append(
                        incognitas_self[0]
                    )
                    incognitas_self.pop(0)
                    i_IT = 0
                    continue

                if incognitas_self[0].base == incognitas_termino[i_IT].base:
                    incognitas_cociente.append(
                        (incognitas_self[0] / incognitas_termino[i_IT])[0]
                    )
                    incognitas_self.pop(0)
                    incognitas_termino.pop(i_IT)

                    i_IT = 0
                else:
                    i_IT += 1

            return Termino(
                self.__coeficiente / termino.coeficiente,
                incognitas_cociente
            )
        else:
            return False

    def copy(self, termino):
        if type(termino) is Termino:
            return Termino(
                termino.coeficiente,
                list.copy(termino.incognitas)
            )

    def __ObtenerCoeficiente(self):
        return self.__coeficiente

    def __ModificarCoefciente(self, coeficiente):
        self.__coeficiente = self.__AgregarCoeficiente(coeficiente)

    def __EliminarCoeficiente(self):
        del self.__coeficiente

    def __ObtenerIncognitas(self):
        return self.__incognitas

    def __ModificarIncognitas(self, incognitas):
        self.__incognitas = self.__AgregarIncognitas(incognitas)

    def __EliminarIncognitas(self):
        for incognita in self.__incognitas:
            del incognita
        del self.__incognitas

    coeficiente = property(
        __ObtenerCoeficiente,
        __ModificarCoefciente,
        __EliminarCoeficiente,
        "Coeficiente"
    )
    incognitas = property(
        __ObtenerIncognitas,
        __ModificarIncognitas,
        __EliminarIncognitas,
        "Incognitas"
    )


###############################################################
#funciones Polinomio

def Agregar_Terminos(terminos):
    if type(terminos) is list:
        terminos_finales = []

        for termino in terminos:
            if type(termino) is Termino:
                if len(termino.incognitas) > 1:
                    continue

                terminos_finales.append(termino)

        Ordenar_Terminos(terminos_finales)

        for termino in terminos_finales:
            if termino.coeficiente == 0:
                terminos_finales.remove(termino)

        terminos.clear()

        for termino in terminos_finales:
            terminos.append(termino)


def Ordenar_Terminos(terminos):
    i = 0

    while i < len(terminos):
        j = 0

        while j < (len(terminos) - 1):
            termino_actual = terminos[j]
            incognitas_TA = list.copy(termino_actual.incognitas)
            termino_siguiente = terminos[j + 1]
            incognitas_TS = list.copy(termino_siguiente.incognitas)

            if not incognitas_TA:
                if termino_actual == terminos[-1] and (not termino_actual is terminos[-1]):
                    terminos[-1] += termino_actual
                    terminos.remove(termino_actual)
                else:
                    termino_termporal = terminos[-1]
                    terminos[-1] = termino_actual
                    terminos[j] = termino_termporal
                    j += 1

                continue

            if not incognitas_TS:
                if termino_siguiente == terminos[-1] and (not termino_siguiente is terminos[-1]):
                    terminos[-1] += termino_siguiente
                    terminos.remove(termino_siguiente)
                else:
                    termino_termporal = terminos[-1]
                    terminos[-1] = termino_siguiente
                    terminos[j + 1] = termino_termporal
                    j += 1

                continue

            if incognitas_TA[0] < incognitas_TS[0]:
                terminos[j] = termino_siguiente
                terminos[j + 1] = termino_actual

            elif termino_actual == termino_siguiente:
                terminos[j] = termino_actual + termino_siguiente
                terminos.pop(j + 1)

            j += 1
        i += 1


def Sumar_Polinomios(polinomio1, polinomio2):
    if type(polinomio1) is list and type(polinomio2) is list:
        terminos_suma = []
        terminos_P1 = list.copy(polinomio1)
        terminos_P2 = list.copy(polinomio2)

        for termino in terminos_P1:
            terminos_suma.append(termino)

        for termino in terminos_P2:
            terminos_suma.append(termino)

        Agregar_Terminos(terminos_suma)

        return [terminos_suma, Imprimir_Polinomio(terminos_suma)]
    else:
        return []


def Restar_Polinomios(polinomio1, polinomio2):
    return Sumar_Polinomios(polinomio1, polinomio2)


def Multiplicar_Polinomios(polinomio1, polinomio2):
    if type(polinomio1) is list and type(polinomio2) is list:
        sumandos = []
        suma = []
        producto = []
        producto_str = ""
        terminos_P1 = list.copy(polinomio1)
        terminos_P2 = list.copy(polinomio2)
        pol_len = len(
            Imprimir_Polinomio(polinomio1)
        ) + len(
            Imprimir_Polinomio(polinomio2)
        )
        i = 0
        j = 0

        while terminos_P2:
            for termino_P1 in terminos_P1:
                producto.append(
                    termino_P1 * terminos_P2[0]
                )

            terminos_P2.pop(0)

            sumandos.append(
                list.copy(producto)
            )
            producto.clear()

        sumandos.reverse()

        while j < len(sumandos):
            producto_str += Imprimir_Polinomio(sumandos[j])
            if j >= 1:
                producto_str += " " * (i + 10)

            producto_str += "\n"

            j += 1
            i += 10

        while sumandos:
            suma = (Sumar_Polinomios(suma, sumandos[0]))[0]
            sumandos.pop(0)

        Agregar_Terminos(suma)

        if j > 1:
            producto_str += "-" * pol_len + "\n"
            producto_str += Imprimir_Polinomio(suma)

        return [suma, producto_str]

    else:
        return []


def Dividir_Polinomios(dividendo, divisor):
    if type(dividendo) is list and type(divisor) is list:
        if dividendo[0].incognitas:
            grado_dividendo = dividendo[0].incognitas[0].exponente
        else:
            grado_dividendo = 0

        if divisor[0].incognitas:
            grado_divisor = divisor[0].incognitas[0].exponente
        else:
            grado_divisor = 0

        dividendo_resta = list.copy(dividendo)
        grado_DR = grado_dividendo
        cociente = []
        resto = []
        resto_str = ""
        i = 0

        if grado_dividendo >= grado_divisor:
            while grado_DR >= grado_divisor:
                if dividendo_resta:
                    cociente.append(
                        dividendo_resta[0] / divisor[0]
                    )
                else:
                    break

                for divisor_termino in divisor:
                    resto.append(
                        -(cociente[-1] * divisor_termino)
                    )

                dividendo_resta = (
                    Restar_Polinomios(
                        dividendo_resta,
                        resto
                    )
                )[0]

                resto_str += " " * i
                resto_str += Imprimir_Polinomio(resto) + "\n"
                i += 10
                resto_str += "-" * (
                    len(
                        Imprimir_Polinomio(dividendo)
                    ) + len(
                        Imprimir_Polinomio(divisor)
                    )
                ) + "\n"
                resto_str += " " * i
                resto_str += Imprimir_Polinomio(dividendo_resta) + "\n"

                resto.clear()

                if dividendo_resta:
                    if dividendo_resta[0].incognitas:
                        grado_DR = dividendo_resta[0].incognitas[0].exponente
                        continue
                grado_DR = 0

        Agregar_Terminos(cociente)

        return [cociente, resto_str]
    else:
        return []


def Imprimir_Polinomio(polinomio):
    string = ""

    for termino in polinomio:
        string += "+ (" + str(termino) + ") "

    return string

###############################################################
#clase Polinomio

'''
class Polinomio:

    def __OrdenarTerminos(self, terminos):
        i = 0

        while i < len(terminos):
            j = 0

            while j < (len(terminos) - 1):
                if terminos[j].incognitas == terminos[j + 1].incognitas:
                    terminos[j] = terminos[j + 1] + terminos[j]
                    terminos.pop(j + 1)
                    continue

                n = 0

                if terminos[j].incognitas == []:
                    termino_actual = terminos[j]
                    terminos[j] = terminos[j + 1]
                    terminos[j + 1] = termino_actual
                    j += 1
                    continue
                elif terminos[j + 1].incognitas == []:
                    j += 1
                    continue

                while terminos[j].incognitas[n] == terminos[j + 1].incognitas[n]:
                    if n == (len(terminos[j].incognitas) - 1):
                        break
                    elif n == (len(terminos[j + 1].incognitas) - 1):
                        break
                    else:
                        n += 1

                if terminos[j].incognitas[n].base > terminos[j + 1].incognitas[n].base:
                    termino_actual = terminos[j]
                    terminos[j] = terminos[j + 1]
                    terminos[j + 1] = termino_actual
                elif terminos[j].incognitas[n] > terminos[j + 1].incognitas[n]:
                    termino_actual = terminos[j]
                    terminos[j] = terminos[j + 1]
                    terminos[j + 1] = termino_actual

                j += 1
            i += 1

    def __AgregarTerminos(self, terminos):
        if type(terminos) is list:
            terminos_finales = []

            for termino in terminos:
                if type(termino) is Termino:
                    terminos_finales.append(termino)

            self.__OrdenarTerminos(terminos_finales)

            for termino in terminos_finales:
                if termino.coeficiente <= 0:
                    terminos_finales.remove(termino)

            return list.copy(terminos_finales)
        else:
            return []

    def __init__(self, terminos=[]):
        self.__terminos = self.__AgregarTerminos(terminos)

    def __str__(self):
        polinomio = ""

        for termino in self.__terminos:
            polinomio += "+ (" + str(termino) + ") "

        return polinomio

    def __eq__(self, polinomio):
        if type(polinomio) is Polinomio:
            if len(self.__terminos) == len(polinomio):
                i = 0
                igual = []

                while i < len(self.__terminos):
                    termino_polinomio = polinomio.terminos[i]
                    termino_self = self.__terminos[i]

                    if termino_polinomio == termino_self and termino_polinomio.coeficiente == termino_self.cociente:
                        igual.append(True)

            return not (False in igual)
        else:
            False

    def __ne__(self, polinomio):
        if type(polinomio) is Polinomio:
            return not self == polinomio
        else:
            return False

    def __add__(self, polinomio):
        if type(polinomio) is Polinomio:
            terminos_suma = []
            terminos_self = list.copy(self.__terminos)
            terminos_polinomio = list.copy(polinomio.terminos)
            i_IT = 0

            while terminos_polinomio or terminos_self:
                if not terminos_self:
                    terminos_suma.append(
                        terminos_polinomio[i_IT]
                    )
                    terminos_polinomio.pop(i_IT)
                    continue
                elif not terminos_polinomio:
                    terminos_suma.append(
                        terminos_self[0]
                    )
                    terminos_self.pop(0)
                    continue

                if i_IT == len(terminos_polinomio):
                    terminos_suma.append(
                        terminos_self[0]
                    )
                    terminos_self.pop(0)
                    i_IT = 0
                    continue

                if terminos_self[0] == terminos_polinomio[i_IT]:
                    terminos_suma.append(
                        terminos_self[0] + terminos_polinomio[i_IT]
                    )
                    terminos_self.pop(0)
                    terminos_polinomio.pop(i_IT)

                    i_IT = 0
                else:
                    i_IT += 1

            return Polinomio(terminos_suma)
        else:
            return False

    def __sub__(self, polinomio):
        if type(polinomio) is Polinomio:
            return self + polinomio

    def __mul__(self, polinomio):
        if type(polinomio) is Polinomio:
            polinomios_suma = []
            suma = Polinomio()
            producto = []
            terminos_self = list.copy(self.__terminos)
            terminos_polinomio = list.copy(polinomio.terminos)

            while terminos_polinomio:
                for termino_self in terminos_self:
                    producto.append(
                        termino_self * terminos_polinomio[0]
                    )

                terminos_polinomio.pop(0)

                polinomios_suma.append(
                    Polinomio(list.copy(producto)),
                )
                producto.clear()

            while polinomios_suma:
                suma += polinomios_suma[0]
                polinomios_suma.pop(0)

            return suma
        else:
            return False

    def __truediv__(self, polinomio):
        if type(polinomio):
            resto_lista = []
            resto = Polinomio()
            cociente = []
            polinomio_self = Polinomio(list.copy(self.__terminos))
            terminos_polinomio = list.copy(polinomio.terminos)

            while (Polinomio(terminos_polinomio) * Polinomio(cociente)) != polinomio_self:
                cociente.append(
                    polinomio_self.terminos[0] / terminos_polinomio[0]
                )
                for termino in cociente:
                    print("TERMINO COCIENTE")
                    print(termino)

                for termino_polinomio in terminos_polinomio:
                    resto_lista.append(
                        -(cociente[-1] * termino_polinomio)
                    )
                resto.terminos = resto_lista
                polinomio_self -= resto

                resto.terminos.clear()
                resto_lista.clear()

            return Polinomio(cociente)
        else:
            return False

    def __len__(self):
        return len(self.__terminos)

    def __setitem__(self, indice, termino):
        if type(termino) is Termino:
            self.__terminos[indice] = termino

    def __delitem__(self, indice):
        del self.__terminos[indice]

    def __getitem__(self, indice):
        return self.__terminos[indice]

    def __ObtenerTerminos(self):
        return self.__terminos

    def __ModificarTerminos(self, terminos):
        if type(terminos) is list:
            self.__terminos = terminos

    def __EliminarTerminios(self):
        del self.__terminos

    terminos = property(
        __ObtenerTerminos,
        __ModificarTerminos,
        __EliminarTerminios,
        "terminos",
    )

###############################################################
#Pruebas: Polinomio

print("POLINOMIO")
print("---------------------------------------------------")

ab = Termino(
    2,
    [
        Incognita("a"),
        Incognita("b"),
    ]
)
ax = Termino(
    -3,
    [
        Incognita("x"),
        Incognita("a", 2),
    ]
)
bx = Termino(
    4,
    [
        Incognita("b"),
        Incognita("x"),
    ]
)
cd = Termino(
    -5,
    [
        Incognita("d"),
        Incognita("c"),
    ]
)
y = Termino(
    6,
    [
        Incognita("y"),
    ]
)
polABAXBXCDY = Polinomio(
    [
        ab,
        ax,
        #bx,
        #cd,
        y,
    ]
)
polABAX = Polinomio(
    [
        ab,
        ax,
    ]
)

print("MULTIPLICACION")
print(polABAXBXCDY * polABAX)

x5 = Termino(
    12,
    [
        Incognita("x", 5),
    ]
)
x3 = Termino(
    -3,
    [
        Incognita("x", 3),
    ]
)
x = Termino(
    10,
    [
        Incognita("x"),
    ]
)
x1 = Termino(
    1,
    [
        Incognita(),
    ]
)
independiente3 = Termino(
    -3
)
independiente = Termino(
    Fraction(10, 3)
)
polX5X3XINDEPENDIENTE = Polinomio(
    [
        x5,
        x3,
        x,
        independiente,
    ]
)
polX1INDEPENDIENTE3 = Polinomio(
    [
        x1,
        independiente3,
    ]
)

print("DIVISION")
print("POLINOMIO CON X5")
print(polX5X3XINDEPENDIENTE)
print("POLINOMIO CON X1")
print(polX1INDEPENDIENTE3)

print(polX5X3XINDEPENDIENTE / polX1INDEPENDIENTE3)
'''
