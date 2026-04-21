from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from psp.ejercicio1.psp1 import PSP1

class VentanaPSP1(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/PSP1.ui", self)

        self.btn_caso1.clicked.connect(self.caso1)
        self.btn_caso2.clicked.connect(self.caso2)
        self.btn_caso3.clicked.connect(self.caso3)
        self.btn_caso4.clicked.connect(self.caso4)

        self.btn_calcular.clicked.connect(self.calcular)

        self.x = None
        self.y = None
        
    def caso1(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        
    def caso2(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    def caso3(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]

    def caso4(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    def calcular(self):
        xk = float(self.input_xk.text())

        modelo = PSP1(self.x, self.y)
        modelo.calcular_todo()

        yk = modelo.predecir(xk)

        self.lbl_b0.setText(str(round(modelo.B0, 4)))
        self.lbl_b1.setText(str(round(modelo.B1, 4)))
        self.lbl_r.setText(str(round(modelo.r, 4)))
        self.lbl_r2.setText(str(round(modelo.r2, 4)))
        self.lbl_yk.setText(str(round(yk, 4)))