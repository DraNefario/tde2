# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(985, 564)
        
        # Aplicar estilo moderno (Fusion)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        
        # Definir cores de fundo e texto
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        Dialog.setPalette(palette)

        # Melhorando os botões
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton {background-color: #5a9; border-radius: 5px; color: white;} QPushButton:hover {background-color: #7cfc00;}")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton {background-color: #f90; border-radius: 5px; color: white;} QPushButton:hover {background-color: #ffa500;}")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 420, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton {background-color: #f44; border-radius: 5px; color: white;} QPushButton:hover {background-color: #ff6347;}")

        # Tabela de dados
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(210, 30, 481, 192))
        self.tableView.setObjectName("tableView")
        self.tableView.setStyleSheet("QTableView {background-color: #2b2b2b; color: white; gridline-color: gray;}")

        # Caixas de entrada de texto
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 250, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("QLineEdit {background-color: #2b2b2b; color: white; border-radius: 5px;}")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 290, 291, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("QLineEdit {background-color: #2b2b2b; color: white; border-radius: 5px;}")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 390, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("QLineEdit {background-color: #2b2b2b; color: white; border-radius: 5px;}")

        # Rótulos
        self.label_nome = QtWidgets.QLabel(Dialog)
        self.label_nome.setGeometry(QtCore.QRect(210, 250, 60, 20))
        self.label_nome.setText("Nome:")
        self.label_nome.setStyleSheet("QLabel {color: white; font-size: 12pt;}")

        self.label_email = QtWidgets.QLabel(Dialog)
        self.label_email.setGeometry(QtCore.QRect(210, 290, 60, 20))
        self.label_email.setText("Email:")
        self.label_email.setStyleSheet("QLabel {color: white; font-size: 12pt;}")

        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setGeometry(QtCore.QRect(210, 390, 60, 20))
        self.label_id.setText("ID:")
        self.label_id.setStyleSheet("QLabel {color: white; font-size: 12pt;}")

        # Instruções na interface
        self.instructions = QtWidgets.QLabel(Dialog)
        self.instructions.setGeometry(QtCore.QRect(290, 320, 300, 20))
        self.instructions.setStyleSheet("QLabel {color: #ccc; font-size: 10pt;}")
        self.instructions.setText("Preencha 'Nome' e 'Email' para adicionar ou atualizar.")

        self.instructions_delete = QtWidgets.QLabel(Dialog)
        self.instructions_delete.setGeometry(QtCore.QRect(290, 370, 300, 20))
        self.instructions_delete.setStyleSheet("QLabel {color: #ccc; font-size: 10pt;}")
        self.instructions_delete.setText("Preencha 'ID' para deletar um registro.")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestão de Pesquisadores"))
        self.pushButton.setText(_translate("Dialog", "Adicionar"))
        self.pushButton_2.setText(_translate("Dialog", "Atualizar"))
        self.pushButton_3.setText(_translate("Dialog", "Deletar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
