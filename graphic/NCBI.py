from os import listdir
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.ncbi_view import *
from object.Search import Search


class NCBI(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(NCBI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telecharger")
        #     self.fill_box_type()

    def button_go_clicked(self):
        return

    def button_write_clicked(self):
        return

    # TODO : reprendre toute la classe avec nouvelle nomenclature

    # def fill_box_type(self):
    #     """fill the comboBox with the name of the created styles"""
    #     files = listdir('files_type')
    #     for file in files:
    #         list = file.split(".")[0].split("_")
    #         name = " ".join(list)
    #         self.box_type.addItem(name)
    #
    # def button_ok_pressed(self):
    #     """instructions when the button ok is pressed"""
    #     self._clean_labels()
    #
    # def button_ok_clicked(self):
    #     """instructions when button ok is clicked"""
    #
    #     try:
    #         infos = self.get_info()
    #         organism = infos[0]
    #         request = infos[1]
    #         type = infos[2]
    #         search = Search(organism=organism, request=request, type=type)
    #
    #     except Exception as e:
    #         self.label_error.setText("ERROR : " + str(e))
    #
    #     else:
    #         self.label_nb_result.setText(str(search.nb_result) + " results found.")
    #
    #         if len(search.errors) > 0:
    #             text_errors = "ERRORS :\n"
    #             for error in search.errors:
    #                 text_errors = text_errors + " - " + error + "\n"
    #             self.label_error.setText(text_errors)
    #
    #         if search.file_created is True:
    #             self.label_create.setText("File created !")
    #         else:
    #             self.label_create.setText("ERROR : File not created !")
    #
    #     self.button_ok.setEnabled(False)
    #
    # def button_request_clicked(self):
    #     """instruction when button request clicked"""
    #     self.button_ok.setEnabled(True)
    #     self.edit_request.setEnabled(True)
    #     self.set_request()
    #
    # def get_request(self):
    #     """export requests from the json file"""
    #     with open('types.json') as json_data:
    #         requests = json.load(json_data)
    #     return requests
    #
    # def set_request(self):
    #     """fill in the edit request"""
    #     organism = self.edit_organism.text()
    #     type = self.box_type.currentText()
    #
    #     if len(organism) == 0 or len(type) == 0:
    #         self._print_warning_message()
    #     else:
    #         requests = self.get_request()
    #         request_end = requests[type]
    #         request = organism + " AND " + request_end
    #         self.edit_request.setText(request)
    #
    # def get_info(self):
    #     """get the request from the LineEdit"""
    #     organism = self.edit_organism.text()
    #     request = self.edit_request.text()
    #     type = self.box_type.currentText()
    #
    #     if len(organism) == 0 or len(type) == 0 or self.box_type.currentIndex() == 0:
    #         self._print_warning_message()
    #     else:
    #         return [organism, request, type]
    #
    # def _print_warning_message(self):
    #     """open a warning message if the request's not complete"""
    #     message = QMessageBox()
    #     message.setText("Remplir les 3 champs !")
    #     message.setWindowTitle("Attention !")
    #     message.exec()
    #
    # def _clean_labels(self):
    #     """clean all the labels between 2 researches"""
    #     self.label_create.setText("")
    #     self.label_error.setText("")
    #     self.label_nb_result.setText("")