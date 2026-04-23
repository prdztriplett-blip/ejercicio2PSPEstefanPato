from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from psp.ejercicio3.psp3 import PSP3

class VentanaPSP3(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("gui/PSP3.ui", self)

        self.btn_ejecutar.clicked.connect(self.calcular)

    def calcular(self):
        p = float(self.txt_p.text())
        dof = int(self.txt_dof.text())

        modelo = PSP3(p, dof)
        x = modelo.calcular()

        self.lbl_resultado.setText(str(round(x, 5)))