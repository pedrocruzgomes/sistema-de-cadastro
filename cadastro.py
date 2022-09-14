# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import icones_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 634)
        MainWindow.setStyleSheet(u"background-color: rgb(82, 166, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255,255,255);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_container = QWidget(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(9, 0))
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 0, 9)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 9, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(70,130,180);\n"
"}\n"
"QToolBox{\n"
"text-align:left;\n"
"	background-color:rgb(228,254,255);\n"
"}\n"
"QToolBox::tab{\n"
"border-radus: 5px;\n"
"background-color:rgb(194,232,255);\n"
"text-align:left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(100,149,237);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px\n"
"\n"
"}\n"
"QPushButton{\n"
"color:rgb(255,255,255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 138, 496))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.page.setFont(font)
        self.page.setCursor(QCursor(Qt.ArrowCursor))
        self.page.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.page.setLayoutDirection(Qt.LeftToRight)
        self.page.setStyleSheet(u"")
        self._2 = QVBoxLayout(self.page)
        self._2.setSpacing(6)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self._2.setContentsMargins(9, 9, 9, 9)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(120, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"")

        self._2.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(120, 30))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self._2.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(120, 30))
        self.btn_contatos.setFont(font1)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self._2.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(120, 30))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self._2.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self._2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 93, 496))
        self.page_2.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_6 = QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 9, 0)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy1)
        self.top_frame.setMinimumSize(QSize(0, 0))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.btn_menu = QPushButton(self.top_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy2)
        self.btn_menu.setMinimumSize(QSize(0, 0))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icones/\u00cdcones/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(37, 37))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy3)
        self.main_frame.setStyleSheet(u"background-color:rgb(70,130,180);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.logo)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255,255,255);\n"
"font: 10pt \"Ms Shell Dig 2\";\n"
"}\n"
"QFrame{\n"
"background-color:rgb(176,196,222);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 0, 1, 3)

        self.txt_cpf = QLineEdit(self.frame_3)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpf, 2, 0, 1, 1)

        self.txt_nasc = QLineEdit(self.frame_3)
        self.txt_nasc.setObjectName(u"txt_nasc")
        self.txt_nasc.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nasc, 2, 1, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_3)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 2, 2, 1, 1)

        self.txt_email = QLineEdit(self.frame_3)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 3, 0, 1, 1)

        self.txt_cidade = QLineEdit(self.frame_3)
        self.txt_cidade.setObjectName(u"txt_cidade")
        self.txt_cidade.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cidade, 3, 1, 1, 1)

        self.txt_rua = QLineEdit(self.frame_3)
        self.txt_rua.setObjectName(u"txt_rua")
        self.txt_rua.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_rua, 4, 0, 1, 2)

        self.txt_bairro = QLineEdit(self.frame_3)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 5, 0, 1, 2)

        self.txt_numero = QLineEdit(self.frame_3)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 5, 2, 1, 1)

        self.lbl_cadastro = QLabel(self.frame_3)
        self.lbl_cadastro.setObjectName(u"lbl_cadastro")
        sizePolicy1.setHeightForWidth(self.lbl_cadastro.sizePolicy().hasHeightForWidth())
        self.lbl_cadastro.setSizePolicy(sizePolicy1)
        self.lbl_cadastro.setMinimumSize(QSize(0, 0))
        self.lbl_cadastro.setStyleSheet(u"color:rgb(0,99,148);\n"
"background-color:rgb(249,249,249);")

        self.gridLayout.addWidget(self.lbl_cadastro, 0, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.btn_cadastro = QPushButton(self.tab)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(160, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_cadastro.setFont(font2)
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(0,170,255);\n"
"border-radius:15px;\n"
"color:#fff\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(243,243,243);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_cadastro, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_4.setFont(font3)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background-color:rgb(100,149,237);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_pessoas = QTableWidget(self.tab_2)
        if (self.table_pessoas.columnCount() < 9):
            self.table_pessoas.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_pessoas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_pessoas.setObjectName(u"table_pessoas")
        self.table_pessoas.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(100,149,237);\n"
"color:rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"QTableWidget{\n"
"background-color:rgb(135,206,250);\n"
"}")

        self.horizontalLayout_5.addWidget(self.table_pessoas)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(255,255,255);\n"
"font:11pt \"Ms Shell Dig 2\";\n"
"color:rgb(0,24,74);\n"
"}\n"
"QFrame{\n"
"background-color:rgb(135,206,250);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_4)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(49,147,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_4)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(255,170,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_4)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(255,0,0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.pg_contatos)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_10)

        self.label_6 = QLabel(self.pg_contatos)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.rodape_frame = QFrame(self.main_container)
        self.rodape_frame.setObjectName(u"rodape_frame")
        self.rodape_frame.setFrameShape(QFrame.StyledPanel)
        self.rodape_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rodape_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.rodape_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.rodape_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pedro Cruz</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.page.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio:</span><span style=\" font-size:12pt;\"> Teste</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sistema:</span><span style=\" font-size:12pt;\"> Cadastro</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Status:</span><span style=\" font-size:12pt;\"> Ativo</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Venc:</span><span style=\" font-size:12pt;\"> 00/00/0000</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informações", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sistema de Cadastro</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/\u00cdcones/pessoas.png\"/></p></body></html>", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_nasc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_rua.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rua", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.lbl_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CADASTRO</span></p></body></html>", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">PESSOAS</p></body></html>", None))
        ___qtablewidgetitem = self.table_pessoas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.table_pessoas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem2 = self.table_pessoas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NASCIMENTO", None));
        ___qtablewidgetitem3 = self.table_pessoas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem4 = self.table_pessoas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem5 = self.table_pessoas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem6 = self.table_pessoas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"RUA", None));
        ___qtablewidgetitem7 = self.table_pessoas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem8 = self.table_pessoas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pessoas", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">CONTATOS</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/\u00cdcones/zap.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(014)99666-6418</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/\u00cdcones/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">pedrodellacruz@hotmail.com</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">SOBRE</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Este sistema foi feito para realizar o cadastro de pessoas de sua empresa ou tamb\u00e9m para o cadastro de clientes que realizam compras em sua empresa.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pedro Cruz", None))
    # retranslateUi

