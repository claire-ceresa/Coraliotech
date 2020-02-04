from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.principal_view import *
from graphic.NCBI import NCBI

class Principal(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.set_image()
        self.window_download = NCBI()

    def set_image(self):
        """set the logo on the"""
        picture = QPixmap("logo.png")
        self.label_image.setPixmap(picture)

    def button_complete_file_clicked(self):
        return

    def button_complete_product_clicked(self):
        return

    def button_search_clicked(self):
        return

    def button_download_clicked(self):
        self.window_download.show()