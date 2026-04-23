from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from load.load_venta_psp1 import VentanaPSP1
from load.load_venta_psp2 import VentanaPSP2
from load.load_venta_psp3 import VentanaPSP3


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)

        self.actionPSP1.triggered.connect(self.abrir_psp1)
        self.actionPSP2.triggered.connect(self.abrir_psp2)
        self.actionPSP3.triggered.connect(self.abrir_psp3)
        self.actionSalir.triggered.connect(self.close)

    def abrir_psp1(self):
        self.psp1 = VentanaPSP1()
        self.psp1.show()

    def abrir_psp2(self):
        self.psp2 = VentanaPSP2()
        self.psp2.show()
    
    def abrir_psp3(self):
        self.psp3 = VentanaPSP3()
        self.psp3.show()