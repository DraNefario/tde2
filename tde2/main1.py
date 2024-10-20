# main1.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from conexao import criar_sessao  # Importa a função para criar a sessão
from pagina import Ui_Dialog

# Definição do modelo Cliente
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome={self.nome}, email={self.email})>"

class MainApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.session = criar_sessao()
        self.pushButton.clicked.connect(self.adicionar_cliente)
        self.pushButton_2.clicked.connect(self.atualizar_cliente)
        self.pushButton_3.clicked.connect(self.deletar_cliente)
        self.load_clientes()

    def load_clientes(self):
        clientes = self.session.query(Cliente).all()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Nome", "Email"])
        
        for cliente in clientes:
            model.appendRow([
                QStandardItem(str(cliente.id)),
                QStandardItem(cliente.nome),
                QStandardItem(cliente.email)
            ])
        
        self.tableView.setModel(model)

    def adicionar_cliente(self):
        nome = self.lineEdit.text()
        email = self.lineEdit_2.text()
        novo_cliente = Cliente(nome=nome, email=email)
        self.session.add(novo_cliente)
        self.session.commit()
        self.load_clientes()  # Atualiza a lista

    def atualizar_cliente(self):
        id_cliente = self.lineEdit_3.text()
        cliente = self.session.query(Cliente).get(id_cliente)
        if cliente:
            cliente.nome = self.lineEdit.text()
            cliente.email = self.lineEdit_2.text()
            self.session.commit()
            self.load_clientes()  # Atualiza a lista

    def deletar_cliente(self):
        id_cliente = self.lineEdit_3.text()
        cliente = self.session.query(Cliente).get(id_cliente)
        if cliente:
            self.session.delete(cliente)
            self.session.commit()
            self.load_clientes()  # Atualiza a lista

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
