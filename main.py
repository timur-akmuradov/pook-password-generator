import generators
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QGuiApplication


class Ui_MainWindow(object):
    passwordsXKCD = None
    passwordsStandart = None

    def setupUiStart(self, MainWindow):
        # Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 500)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 500))
        MainWindow.setMaximumSize(QtCore.QSize(350, 500))
        MainWindow.setWindowIcon(QtGui.QIcon('res/icon.png'))

        # Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(31, 31, 31);\n""")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Title text
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(0, 100, 350, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_start.setObjectName("label_start")

        # Standart generator button
        self.btn_standart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_standart.setGeometry(QtCore.QRect(20, 200, 310, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_standart.setFont(font)
        self.btn_standart.setStyleSheet("color: rgb(255, 217, 0);\n"
                                        "background-color: rgb(60, 60, 60);\n""")
        self.btn_standart.setObjectName("btn_standart")

        self.btn_standart.clicked.connect(self.setupUiStnd)

        # XKCD Button
        self.btn_xkcd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd.setGeometry(QtCore.QRect(20, 280, 310, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd.setFont(font)
        self.btn_xkcd.setStyleSheet("color: rgb(255, 217, 0);\n"
                                    "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd.setObjectName("btn_xkcd")

        self.btn_xkcd.clicked.connect(self.setupUiXKCD)

        # Dancing cat :3
        self.label_cat = QtWidgets.QLabel(self.centralwidget)
        self.label_cat.setGeometry(QtCore.QRect(0, 400, 120, 120))
        self.label_cat.setObjectName("label_cat")
        self.movie = QMovie('res/cat.gif')
        self.label_cat.setMovie(self.movie)
        self.movie.start()

        # Copyright
        self.label_thympook = QtWidgets.QLabel(self.centralwidget)
        self.label_thympook.setGeometry(QtCore.QRect(160, 483, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_thympook.setFont(font)
        self.label_thympook.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_thympook.setAlignment(QtCore.Qt.AlignRight)
        self.label_thympook.setObjectName("label_thympook")

        self.retranslateUiStart(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiStart(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PookPassword"))
        self.label_start.setText(_translate("MainWindow", "Choose generation type:"))
        self.btn_standart.setText(_translate("MainWindow", "Standart"))
        self.btn_xkcd.setText(_translate("MainWindow", "XKCD"))
        self.label_thympook.setText((_translate("MainWindow", "by Thympook")))

    # Standart
    def setupUiStnd(self):
        self.label_start.hide()
        self.label_cat.hide()
        self.btn_xkcd.hide()
        self.btn_standart.hide()

        # Labels
        # Standart title
        self.label_stnd_title = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_title.setGeometry(QtCore.QRect(0, 0, 350, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_title.setFont(font)
        self.label_stnd_title.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stnd_title.setObjectName("label_stnd_title")

        # Standart password length label
        self.label_stnd_plen = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_plen.setGeometry(QtCore.QRect(-40, 320, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_plen.setFont(font)
        self.label_stnd_plen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_plen.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_plen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_stnd_plen.setObjectName("label_stnd_plen")

        # Standart password count label
        self.label_stnd_pcount = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_pcount.setGeometry(QtCore.QRect(-40, 350, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_pcount.setFont(font)
        self.label_stnd_pcount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_pcount.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_pcount.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_stnd_pcount.setObjectName("label_stnd_pcount")

        # Standart add uppercase label
        self.label_stnd_uppercase = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_uppercase.setGeometry(QtCore.QRect(-40, 380, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_uppercase.setFont(font)
        self.label_stnd_uppercase.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_uppercase.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_uppercase.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_stnd_uppercase.setObjectName("label_stnd_uppercase")

        # Standart add numbers label
        self.label_stnd_numbers = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_numbers.setGeometry(QtCore.QRect(-40, 410, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_numbers.setFont(font)
        self.label_stnd_numbers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_numbers.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_numbers.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_stnd_numbers.setObjectName("label_stnd_numbers")

        # Standart remove duplicates label
        self.label_stnd_dupl = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_dupl.setGeometry(QtCore.QRect(230, 320, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_dupl.setFont(font)
        self.label_stnd_dupl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_dupl.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_dupl.setObjectName("label_stnd_dupl")

        # Standart add symbols label
        self.label_stnd_symbols = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_symbols.setGeometry(QtCore.QRect(205, 380, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_symbols.setFont(font)
        self.label_stnd_symbols.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_symbols.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_symbols.setObjectName("label_stnd_symbols")

        # Standart add alternative symbols label
        self.label_stnd_asymbols = QtWidgets.QLabel(self.centralwidget)
        self.label_stnd_asymbols.setGeometry(QtCore.QRect(175, 410, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stnd_asymbols.setFont(font)
        self.label_stnd_asymbols.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_stnd_asymbols.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_stnd_asymbols.setObjectName("label_stnd_asymbols")

        # Buttons
        # Standart Generate button
        self.btn_stnd_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stnd_generate.setGeometry(QtCore.QRect(10, 260, 330, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stnd_generate.setFont(font)
        self.btn_stnd_generate.setStyleSheet("color: rgb(255, 217, 0);\n"
                                             "background-color: rgb(60, 60, 60);\n""")
        self.btn_stnd_generate.setObjectName("btn_stnd_generate")

        self.btn_stnd_generate.clicked.connect(self.generateStandart)

        # Standart back button
        self.btn_stnd_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stnd_back.setGeometry(QtCore.QRect(10, 445, 330, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stnd_back.setFont(font)
        self.btn_stnd_back.setStyleSheet("color: rgb(255, 217, 0);\n"
                                         "background-color: rgb(60, 60, 60);\n""")
        self.btn_stnd_back.setObjectName("btn_stnd_back")

        self.btn_stnd_back.clicked.connect(self.goBackFromStandart)

        # Standart copy button
        self.btn_stnd_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stnd_copy.setGeometry(QtCore.QRect(10, 220, 160, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stnd_copy.setFont(font)
        self.btn_stnd_copy.setStyleSheet("color: rgb(255, 217, 0);\n"
                                         "background-color: rgb(60, 60, 60);\n""")
        self.btn_stnd_copy.setObjectName("btn_stnd_copy")

        self.btn_stnd_copy.clicked.connect(self.copyStandart)

        # Standart clear button
        self.btn_stnd_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stnd_clear.setGeometry(QtCore.QRect(180, 220, 160, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stnd_clear.setFont(font)
        self.btn_stnd_clear.setStyleSheet("color: rgb(255, 217, 0);\n"
                                          "background-color: rgb(60, 60, 60);\n""")
        self.btn_stnd_clear.setObjectName("btn_stnd_clear")

        self.btn_stnd_clear.clicked.connect(self.clearTextStandart)

        # Standart Text browser
        self.text_browser_stnd = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser_stnd.setGeometry(QtCore.QRect(10, 60, 330, 151))
        self.text_browser_stnd.setStyleSheet("color: rgb(255, 217, 0);")
        self.text_browser_stnd.setObjectName("text_browser_stnd")

        # Standart Spinner password length
        self.spinBox_stnd_plen = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_stnd_plen.setGeometry(QtCore.QRect(150, 320, 61, 22))
        self.spinBox_stnd_plen.setStyleSheet("color: rgb(255, 217, 0);\n"
                                             "font: 12pt \"MS Serif\";\n""")
        self.spinBox_stnd_plen.setMinimum(6)
        self.spinBox_stnd_plen.setMaximum(100)
        self.spinBox_stnd_plen.setObjectName("spinBox_stnd_plen")

        # Standart Spinner password count
        self.spinBox_stnd_pcount = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_stnd_pcount.setGeometry(QtCore.QRect(150, 350, 61, 22))
        self.spinBox_stnd_pcount.setStyleSheet("color: rgb(255, 217, 0);\n"
                                               "font: 12pt \"MS Serif\";")
        self.spinBox_stnd_pcount.setMinimum(1)
        self.spinBox_stnd_pcount.setMaximum(9999)
        self.spinBox_stnd_pcount.setObjectName("spinBox_stnd_pcount")

        # Standart Checkbox uppercase
        self.checkBox_uppercase = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_uppercase.setGeometry(QtCore.QRect(150, 385, 16, 16))
        self.checkBox_uppercase.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_uppercase.setObjectName("checkBox_uppercase")

        # Standart Checkbox numbers
        self.checkBox_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_numbers.setGeometry(QtCore.QRect(150, 415, 16, 16))
        self.checkBox_numbers.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_numbers.setObjectName("checkBox_numbers")

        # Standart Checkbox symbols
        self.checkBox_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_symbols.setGeometry(QtCore.QRect(330, 385, 16, 16))
        self.checkBox_symbols.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_symbols.setObjectName("checkBox_symbols")

        # Standart Checkbox alternative symbols
        self.checkBox_asymbols = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_asymbols.setGeometry(QtCore.QRect(330, 415, 16, 16))
        self.checkBox_asymbols.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_asymbols.setObjectName("checkBox_asymbols")

        # Standart Checkbox remove duplicates
        self.checkBox_duplicates = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_duplicates.setGeometry(QtCore.QRect(330, 350, 16, 16))
        self.checkBox_duplicates.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_duplicates.setObjectName("checkBox_duplicates")

        self.retranslateUiStandart(MainWindow)

    def retranslateUiStandart(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PookPassword"))
        self.label_stnd_title.setText(_translate("MainWindow", "STANDART GENERATOR"))
        self.btn_stnd_generate.setText(_translate("MainWindow", "GENERATE!"))
        self.label_stnd_plen.setText(_translate("MainWindow", "Password length:"))
        self.label_stnd_pcount.setText(_translate("MainWindow", "Password count:"))
        self.btn_stnd_back.setText(_translate("MainWindow", "Back"))
        self.label_stnd_uppercase.setText(_translate("MainWindow", "Add uppercase:"))
        self.btn_stnd_copy.setText(_translate("MainWindow", "COPY"))
        self.btn_stnd_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label_stnd_numbers.setText(_translate("MainWindow", "Add numbers:"))
        self.label_stnd_dupl.setText(_translate("MainWindow", "Remove\nduplicates:"))
        self.label_stnd_symbols.setText(_translate("MainWindow", "Add symbols:"))
        self.label_stnd_asymbols.setText(_translate("MainWindow", "Add alt. symbols:"))

        self.label_stnd_plen.show()
        self.label_stnd_dupl.show()
        self.label_stnd_pcount.show()
        self.label_stnd_asymbols.show()
        self.label_stnd_title.show()
        self.label_stnd_numbers.show()
        self.label_stnd_symbols.show()
        self.label_stnd_uppercase.show()
        self.btn_stnd_back.show()
        self.btn_stnd_copy.show()
        self.btn_stnd_clear.show()
        self.btn_stnd_generate.show()
        self.spinBox_stnd_plen.show()
        self.spinBox_stnd_pcount.show()
        self.checkBox_asymbols.show()
        self.checkBox_duplicates.show()
        self.checkBox_numbers.show()
        self.checkBox_uppercase.show()
        self.checkBox_symbols.show()
        self.text_browser_stnd.show()

    def goBackFromStandart(self):
        self.clearTextStandart()

        self.label_stnd_plen.hide()
        self.label_stnd_dupl.hide()
        self.label_stnd_pcount.hide()
        self.label_stnd_asymbols.hide()
        self.label_stnd_title.hide()
        self.label_stnd_numbers.hide()
        self.label_stnd_symbols.hide()
        self.label_stnd_uppercase.hide()
        self.btn_stnd_back.hide()
        self.btn_stnd_copy.hide()
        self.btn_stnd_clear.hide()
        self.btn_stnd_generate.hide()
        self.spinBox_stnd_plen.hide()
        self.spinBox_stnd_pcount.hide()
        self.checkBox_asymbols.hide()
        self.checkBox_duplicates.hide()
        self.checkBox_numbers.hide()
        self.checkBox_uppercase.hide()
        self.checkBox_symbols.hide()
        self.text_browser_stnd.hide()

        self.label_start.show()
        self.label_cat.show()
        self.btn_standart.show()
        self.btn_xkcd.show()

    def clearTextStandart(self):
        self.text_browser_stnd.clear()
        self.btn_stnd_copy.setText('COPY')
        self.passwordsStandart = None

    def copyStandart(self):
        clipboard = QGuiApplication.clipboard()
        if self.passwordsStandart != None:
            self.btn_stnd_copy.setText('COPIED!')
            clipboard.setText(self.passwordsStandart)

    def generateStandart(self):
        self.clearTextStandart()
        self.btn_stnd_copy.setText('COPY')

        plen = self.spinBox_stnd_plen.value()
        pcount = self.spinBox_stnd_pcount.value()
        add_uppercase = self.checkBox_uppercase.isChecked()
        add_numbers = self.checkBox_numbers.isChecked()
        add_symbols = self.checkBox_symbols.isChecked()
        add_asymbols = self.checkBox_asymbols.isChecked()
        remove_duplicates = self.checkBox_duplicates.isChecked()

        if (remove_duplicates == True) and plen > 24:
            plen = 24
            self.spinBox_stnd_plen.setValue(24)

        self.passwordsStandart = '\n'.join(
            generators.standart_password_generator(password_length=plen, password_count=pcount,
                                                   add_uppercase=add_uppercase, add_numbers=add_numbers,
                                                   add_symbols=add_symbols, add_specific_symbols=add_asymbols,
                                                   remove_duplicates=remove_duplicates))
        self.text_browser_stnd.setText(self.passwordsStandart)

    # XKCD
    def setupUiXKCD(self):
        self.label_start.hide()
        self.label_cat.hide()
        self.btn_xkcd.hide()
        self.btn_standart.hide()

        # Labels
        # XKCD Title label
        self.label_xkcd_title = QtWidgets.QLabel(self.centralwidget)
        self.label_xkcd_title.setGeometry(QtCore.QRect(0, 10, 350, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_xkcd_title.setFont(font)
        self.label_xkcd_title.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_xkcd_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xkcd_title.setObjectName("label_title")

        # XKCD Word count label
        self.label_xkcd_wcount = QtWidgets.QLabel(self.centralwidget)
        self.label_xkcd_wcount.setGeometry(QtCore.QRect(-30, 360, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_xkcd_wcount.setFont(font)
        self.label_xkcd_wcount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_xkcd_wcount.setAlignment(QtCore.Qt.AlignRight)
        self.label_xkcd_wcount.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_xkcd_wcount.setObjectName("label_xkcd_wcount")

        # XKCD Password count label
        self.label_xkcd_pcount = QtWidgets.QLabel(self.centralwidget)
        self.label_xkcd_pcount.setGeometry(QtCore.QRect(-30, 390, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_xkcd_pcount.setFont(font)
        self.label_xkcd_pcount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_xkcd_pcount.setAlignment(QtCore.Qt.AlignRight)
        self.label_xkcd_pcount.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_xkcd_pcount.setObjectName("label_xkcd_pcount")

        # XKCD Dictionary label
        self.label_xkcd_dictionary = QtWidgets.QLabel(self.centralwidget)
        self.label_xkcd_dictionary.setGeometry(QtCore.QRect(-30, 420, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_xkcd_dictionary.setFont(font)
        self.label_xkcd_dictionary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_xkcd_dictionary.setAlignment(QtCore.Qt.AlignRight)
        self.label_xkcd_dictionary.setStyleSheet("color: rgb(255, 217, 0);\n""")
        self.label_xkcd_dictionary.setObjectName("label_xkcd_dictionary")

        # Spinners and combobox
        # XKCD word count spin
        self.spinBox_xkcd_wcount = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_xkcd_wcount.setGeometry(QtCore.QRect(160, 360, 61, 22))
        self.spinBox_xkcd_wcount.setStyleSheet("color: rgb(255, 217, 0);\n"
                                               "font: 12pt \"MS Serif\";\n""")
        self.spinBox_xkcd_wcount.setMinimum(1)
        self.spinBox_xkcd_wcount.setMaximum(4)
        self.spinBox_xkcd_wcount.setObjectName("spinBox_xkcd_wcount")

        # XKCD password count spin
        self.spinBox_xkcd_pcount = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_xkcd_pcount.setGeometry(QtCore.QRect(160, 390, 61, 22))
        self.spinBox_xkcd_pcount.setStyleSheet("color: rgb(255, 217, 0);\n"
                                               "font: 12pt \"MS Serif\";")
        self.spinBox_xkcd_pcount.setMinimum(1)
        self.spinBox_xkcd_pcount.setMaximum(9999)
        self.spinBox_xkcd_pcount.setObjectName("spinBox_xkcd_pcount")

        # XKCD comboBox_xkcd
        self.comboBox_xkcd = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_xkcd.setGeometry(QtCore.QRect(160, 420, 181, 22))
        self.comboBox_xkcd.setStyleSheet("font: 12pt \"MS Serif\";\n"
                                         "color: rgb(255, 217, 0);")
        self.comboBox_xkcd.setObjectName("comboBox_xkcd")
        self.comboBox_xkcd.addItem("")
        self.comboBox_xkcd.addItem("")
        self.comboBox_xkcd.addItem("")
        self.comboBox_xkcd.addItem("")
        self.comboBox_xkcd.addItem("")

        # Buttons
        # XKCD Generation button
        self.btn_xkcd_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd_generate.setGeometry(QtCore.QRect(10, 300, 330, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd_generate.setFont(font)
        self.btn_xkcd_generate.setStyleSheet("color: rgb(255, 217, 0);\n"
                                             "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd_generate.setObjectName("btn_xkcd_generate")

        self.btn_xkcd_generate.clicked.connect(self.generateXKCD)

        # XKCD Info button
        self.btn_xkcd_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd_info.setGeometry(QtCore.QRect(230, 360, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd_info.setFont(font)
        self.btn_xkcd_info.setStyleSheet("color: rgb(255, 217, 0);\n"
                                         "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd_info.setObjectName("btn_xkcd_info")

        self.btn_xkcd_info.clicked.connect(self.showInfoXKCD)

        # XKCD Back button
        self.btn_xkcd_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd_back.setGeometry(QtCore.QRect(10, 450, 330, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd_back.setFont(font)
        self.btn_xkcd_back.setStyleSheet("color: rgb(255, 217, 0);\n"
                                         "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd_back.setObjectName("btn_xkcd_back")
        self.btn_xkcd_back.clicked.connect(self.goBackFromXKCD)

        # XKCD Copy button
        self.btn_xkcd_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd_copy.setGeometry(QtCore.QRect(10, 260, 160, 31))
        self.btn_xkcd_copy.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd_copy.setFont(font)
        self.btn_xkcd_copy.setStyleSheet("color: rgb(255, 217, 0);\n"
                                         "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd_copy.setObjectName("btn_xkcd_copy")

        self.btn_xkcd_copy.clicked.connect(self.copyXKCD)

        # XKCD Clear button
        self.btn_xkcd_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xkcd_clear.setGeometry(QtCore.QRect(180, 260, 160, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xkcd_clear.setFont(font)
        self.btn_xkcd_clear.setStyleSheet("color: rgb(255, 217, 0);\n"
                                          "background-color: rgb(60, 60, 60);\n""")
        self.btn_xkcd_clear.setObjectName("btn_xkcd_clear")

        self.btn_xkcd_clear.clicked.connect(self.clearTextXKCD)

        # XKCD Text browser
        self.text_browser_xkcd = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser_xkcd.setGeometry(QtCore.QRect(10, 80, 330, 171))
        self.text_browser_xkcd.setStyleSheet("color: rgb(255, 217, 0);")
        self.text_browser_xkcd.setObjectName("text_browser_xkcd")

        self.retranslateUiXKCD(MainWindow)

    def retranslateUiXKCD(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PookPassword"))
        self.label_xkcd_title.setText(_translate("MainWindow", "XKCD GENERATOR"))
        self.label_xkcd_wcount.setText(_translate("MainWindow", "Word count:"))
        self.label_xkcd_pcount.setText(_translate("MainWindow", "Password count:"))
        self.label_xkcd_dictionary.setText(_translate("MainWindow", "Dictionary:"))
        self.btn_xkcd_copy.setText(_translate("MainWindow", "COPY"))
        self.btn_xkcd_clear.setText(_translate("MainWindow", "CLEAR"))
        self.btn_xkcd_generate.setText(_translate("MainWindow", "GENERATE!"))
        self.btn_xkcd_back.setText(_translate("MainWindow", "Back"))
        self.btn_xkcd_info.setText(_translate("MainWindow", "INFO"))

        self.comboBox_xkcd.setItemText(0, _translate("MainWindow", "ENG 12dicts"))
        self.comboBox_xkcd.setItemData(0, '12dicts_eng.txt')
        self.comboBox_xkcd.setItemText(1, _translate("MainWindow", "RU Holy Bible"))
        self.comboBox_xkcd.setItemData(1, 'HolyBible_ru.txt')
        self.comboBox_xkcd.setItemText(2, _translate("MainWindow", "RU Koran"))
        self.comboBox_xkcd.setItemData(2, 'Koran_ru.txt')
        self.comboBox_xkcd.setItemText(3, _translate("MainWindow", "RU WarAndPeace"))
        self.comboBox_xkcd.setItemData(3, 'WarAndPeace_ru.txt')
        self.comboBox_xkcd.setItemText(4, _translate("MainWindow", "RU Slang XD"))
        self.comboBox_xkcd.setItemData(4, 'Slang_ru.txt')

        self.label_xkcd_title.show()
        self.label_xkcd_wcount.show()
        self.label_xkcd_pcount.show()
        self.label_xkcd_dictionary.show()
        self.btn_xkcd_clear.show()
        self.btn_xkcd_copy.show()
        self.btn_xkcd_generate.show()
        self.btn_xkcd_back.show()
        self.btn_xkcd_info.show()
        self.spinBox_xkcd_pcount.show()
        self.spinBox_xkcd_wcount.show()
        self.comboBox_xkcd.show()
        self.text_browser_xkcd.show()

    def goBackFromXKCD(self):
        self.clearTextXKCD()

        self.label_xkcd_title.hide()
        self.label_xkcd_wcount.hide()
        self.label_xkcd_pcount.hide()
        self.label_xkcd_dictionary.hide()
        self.btn_xkcd_clear.hide()
        self.btn_xkcd_copy.hide()
        self.btn_xkcd_generate.hide()
        self.btn_xkcd_back.hide()
        self.btn_xkcd_info.hide()
        self.spinBox_xkcd_pcount.hide()
        self.spinBox_xkcd_wcount.hide()
        self.comboBox_xkcd.hide()
        self.text_browser_xkcd.hide()

        self.label_start.show()
        self.label_cat.show()
        self.btn_standart.show()
        self.btn_xkcd.show()

    def showInfoXKCD(self):
        self.clearTextXKCD()
        self.btn_xkcd_copy.setText('COPY')
        self.text_browser_xkcd.setText("Over 20 years of effort, we have taught everyone to use passwords that are" +
                                       "difficult for humans to remember and easy for computers to guess." +
                                       "That's why we generate a password from a few random words. " +
                                       "What's the upside of that? A password made up of words is " +
                                       "easier to remember and harder for a computer to guess." +
                                       "\n\n https://xkcd.com/936/\n\n" +
                                       "За 20 лет стараний, мы научили всех использовать пароли, " +
                                       "которые человеку запомнить сложно, а компьютеру подобрать легко. " +
                                       "Вот почему мы генерируем пароль из нескольких случайных слов. " +
                                       "В чем плюс такого пароля? Человеку запомнить его легко, " +
                                       "а компьютеру подобрать - сложно." +
                                       "\n\n https://xkcd.ru/936/")

    def clearTextXKCD(self):
        self.text_browser_xkcd.clear()
        self.passwordsXKCD = None
        self.btn_xkcd_copy.setText('COPY')

    def copyXKCD(self):
        clipboard = QGuiApplication.clipboard()
        if self.passwordsXKCD != None:
            self.btn_xkcd_copy.setText('COPIED!')
            clipboard.setText(self.passwordsXKCD)

    def generateXKCD(self):
        self.clearTextXKCD()
        self.btn_xkcd_copy.setText('COPY')

        wcount = self.spinBox_xkcd_wcount.value()
        pcount = self.spinBox_xkcd_pcount.value()
        dict_ = self.comboBox_xkcd.currentData()

        self.passwordsXKCD = '\n'.join(
            generators.XKCD_password_generator(password_length=int(wcount), password_count=int(pcount),
                                               word_list=dict_))
        self.text_browser_xkcd.setText(self.passwordsXKCD)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiStart(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

