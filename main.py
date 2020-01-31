import sys
from Bio import Entrez
from PyQt5.QtWidgets import QApplication
from graphic.Controller import Controller

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Controller()
form.show()
app.exec()