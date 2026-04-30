from psp.ejercicio1.psp1 import PSP1
from psp.ejercicio2.psp2 import PSP2
from psp.ejercicio3.psp3 import PSP3


class PSP4(object):
    def __init__(self, listax, listay, xk):
        self.listax = listax
        self.listay = listay
        self.xk = xk

        self.n = len(listax)
        self.dof = self.n - 2

        self.r2 = 0
        self.significancia = 0
        self.b0 = 0
        self.b1 = 0
        self.yk = 0
        self.t = 0
        self.sigma = 0
        self.rango = 0
        self.upi = 0
        self.lpi = 0

    def calcularSigma(self, b0, b1):
        suma = 0
        for i in range(self.n):
            suma += (self.listay[i] - b0 - (b1 * self.listax[i])) ** 2

        self.sigma = (suma / (self.n - 2)) ** 0.5

    def calcularRango(self, xavg):
        suma = 0
        for i in range(self.n):
            suma += (self.listax[i] - xavg) ** 2

        parte = 1 + (1 / self.n) + (((self.xk - xavg) ** 2) / suma)
        self.rango = self.t * self.sigma * (parte ** 0.5)

    def calcularTodo(self):

        cal1 = PSP1(self.listax, self.listay)
        cal1.calcular_todo()

        self.b0 = cal1.B0
        self.b1 = cal1.B1
        self.r2 = cal1.r2
        self.yk = cal1.predecir(self.xk)

        x = (abs(cal1.r) * ((self.n - 2) ** 0.5)) / ((1 - cal1.r2) ** 0.5)

        cal2 = PSP2(x, self.dof)
        p = cal2.calcular()
        self.significancia = 1 - (2 * p)

        cal3 = PSP3(0.35, self.dof)
        self.t = cal3.calcular()

        self.calcularSigma(self.b0, self.b1)
        self.calcularRango(cal1.xavg)

        self.upi = self.yk + self.rango
        self.lpi = self.yk - self.rango