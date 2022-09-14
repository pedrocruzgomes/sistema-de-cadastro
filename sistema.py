from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from cadastro import Ui_MainWindow
import sys
from database import DataBase
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Pessoas/Clientes")
        appIcon = QIcon("iconeapp.png")
        self.setWindowIcon(appIcon)

        #########################
        #Botão Menu
        self.btn_menu.clicked.connect(self.leftContainer)
        #########################
        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_contatos.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contatos))
        #########################
        self.btn_cadastro.clicked.connect(self.cadastrar_pessoa)
        self.btn_alterar.clicked.connect(self.atualizar_pessoa)
        self.btn_excluir.clicked.connect(self.deletar_pessoa)
        self.btn_excel.clicked.connect(self.gerar_excel)

        self.buscar_pessoas()

    def leftContainer(self):
        width = self.left_container.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def cadastrar_pessoa(self):
        db = DataBase()
        db.connect()

        fullDataSet = (
            self.txt_nome.text(), self.txt_cpf.text(), self.txt_nasc.text(),
            self.txt_telefone.text(), self.txt_email.text(), self.txt_cidade.text(),
            self.txt_rua.text(), self.txt_bairro.text(), self.txt_numero.text()
        )

        #Cadastrar pessoa no banco de dados
        resp = db.registrar_pessoa(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com Sucesso")
            msg.exec()
            self.buscar_pessoas()
            self.txt_nome.setText("")
            self.txt_cpf.setText("")
            self.txt_nasc.setText("")
            self.txt_telefone.setText("")
            self.txt_email.setText("")
            self.txt_cidade.setText("")
            self.txt_rua.setText("")
            self.txt_bairro.setText("")
            self.txt_numero.setText("")
            db.closeConnection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.closeConnection()
            return

    def buscar_pessoas(self):
        db = DataBase()
        db.connect()
        result = db.select_all_pessoas()

        self.table_pessoas.clearContents()
        self.table_pessoas.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.table_pessoas.setItem(row, column, QTableWidgetItem(str(data)))

        db.closeConnection()

    def atualizar_pessoa(self):
        dados = []
        update_dados = []

        for row in range(self.table_pessoas.rowCount()):
            for column in range(self.table_pessoas.columnCount()):
                dados.append(self.table_pessoas.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #Atualizar banco de dados
        db = DataBase()
        db.connect()

        for pes in update_dados:
            db.update_pessoa(tuple(pes))

        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.table_pessoas.reset()
        self.buscar_pessoas()

    def deletar_pessoa(self):
        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Esta pessoa será excluída")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cpf = self.table_pessoas.selectionModel().currentIndex().siblingAtColumn(1).data()
            result = db.delete_pessoa(cpf)
            self.buscar_pessoas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Pessoas")
            msg.setText(result)
            msg.exec()

        db.closeConnection()

    def gerar_excel(self):
        dados = []
        todos_dados = []

        for row in range(self.table_pessoas.rowCount()):
            for column in range(self.table_pessoas.columnCount()):
                dados.append(self.table_pessoas.item(row, column).text())

            todos_dados.append(dados)
            dados = []

        columns = ["NOME", "CPF", "NASC", "TELEFONE", "EMAIL", "CIDADE", "RUA", "BAIRRO", "NUMERO"]

        pessoas = pd.DataFrame(todos_dados, columns=columns)
        pessoas.to_excel("Pessoas.xlsx", sheet_name="pessoas", index=False)

        msg = QMessageBox()
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

if __name__ == "__main__":

    db = DataBase()
    db.connect()
    db.create_table_pessoas()
    db.closeConnection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()