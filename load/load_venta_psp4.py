from PyQt5 import QtWidgets, uic
from psp.ejercicio4.psp4 import PSP4
import os


class VentanaPSP4(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        ruta_base = os.path.dirname(os.path.dirname(__file__))
        ruta_ui = os.path.join(ruta_base, "gui", "PSP4.ui")
        uic.loadUi(ruta_ui, self)


        self.listax = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.listay = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]



        self.boton_calcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        try:
            xk = float(self.xk_txt.text())

            cal = PSP4(self.listax, self.listay, xk)
            cal.calcularTodo()

            self.label_r2.setText(str(round(cal.r2, 4)))
            self.label_1.setText(str(round(cal.significancia, 4)))
            self.label_b0.setText(str(round(cal.b0, 4)))
            self.label_b1.setText(str(round(cal.b1, 5)))
            self.label_yk.setText(str(round(cal.yk, 4)))
            self.label_t.setText(str(round(cal.t, 5)))
            self.label_rango.setText(str(round(cal.rango, 4)))
            self.label_upi.setText(str(round(cal.upi, 4)))
            self.label_lpi.setText(str(round(cal.lpi, 4)))

        except Exception as e:
            print("Error en PSP4:", e)