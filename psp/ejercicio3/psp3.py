from psp.ejercicio2.psp2 import PSP2

class PSP3(object):
    def __init__(self, p, dof):
        self.p = p
        self.dof = dof
        self.error = 0.00001

    def calcular(self):
        x = 1.0
        d = 0.5

        modelo = PSP2(x, self.dof)
        integral = modelo.calcular()

        error_actual = integral - self.p

        while abs(error_actual) > self.error:
            if error_actual < 0:
                x += d
            else:
                x -= d

            modelo = PSP2(x, self.dof)
            integral = modelo.calcular()

            nuevo_error = integral - self.p


            if (error_actual * nuevo_error) < 0:
                d = d / 2

            error_actual = nuevo_error

        return x