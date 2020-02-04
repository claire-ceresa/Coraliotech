# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_fiche = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_fiche.setMinimumSize(QtCore.QSize(483, 0))
        self.edit_fiche.setObjectName("edit_fiche")
        self.horizontalLayout.addWidget(self.edit_fiche)
        self.edit_infos = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_infos.setObjectName("edit_infos")
        self.horizontalLayout.addWidget(self.edit_infos)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
