from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 351)
        MainWindow.setStyleSheet("background-color: rgb(254, 178, 150);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 350))
        self.tabWidget.setObjectName("tabWidget")
        self.description = QtWidgets.QWidget()
        self.description.setObjectName("description")
        self.tab_1_text = QtWidgets.QLabel(self.description)
        self.tab_1_text.setGeometry(QtCore.QRect(140, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tab_1_text.setFont(font)
        self.tab_1_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_1_text.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_text.setObjectName("tab_1_text")
        self.label_description = QtWidgets.QLabel(self.description)
        self.label_description.setGeometry(QtCore.QRect(0, 50, 491, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_description.setFont(font)
        self.label_description.setTextFormat(QtCore.Qt.PlainText)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.tabWidget.addTab(self.description, "")
        self.generate_password = QtWidgets.QWidget()
        self.generate_password.setObjectName("generate_password")
        self.main_label = QtWidgets.QLabel(self.generate_password)
        self.main_label.setGeometry(QtCore.QRect(250, 0, 251, 311))
        self.main_label.setStyleSheet("background-color: rgb(254, 203, 105);")
        self.main_label.setText("")
        self.main_label.setScaledContents(False)
        self.main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.main_label.setWordWrap(True)
        self.main_label.setIndent(1)
        self.main_label.setObjectName("main_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.generate_password)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 375))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.capital_letters_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.capital_letters_2.setObjectName("capital_letters_2")
        self.verticalLayout.addWidget(self.capital_letters_2)
        self.lower_case_letters_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.lower_case_letters_2.setObjectName("lower_case_letters_2")
        self.verticalLayout.addWidget(self.lower_case_letters_2)
        self.nums_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.nums_2.setObjectName("nums_2")
        self.verticalLayout.addWidget(self.nums_2)
        self.special_point_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.special_point_2.setObjectName("special_point_2")
        self.verticalLayout.addWidget(self.special_point_2)
        self.choose_amount_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.choose_amount_label.setObjectName("choose_amount_label")
        self.verticalLayout.addWidget(self.choose_amount_label)
        self.amount_password = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.amount_password.setFont(font)
        self.amount_password.setMinimum(1)
        self.amount_password.setMaximum(5)
        self.amount_password.setObjectName("amount_password")
        self.verticalLayout.addWidget(self.amount_password)
        self.choose_password_len_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.choose_password_len_label.setObjectName("choose_password_len_label")
        self.verticalLayout.addWidget(self.choose_password_len_label)
        self.len_password = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.len_password.setMinimum(1)
        self.len_password.setMaximum(20)
        self.len_password.setObjectName("len_password")
        self.verticalLayout.addWidget(self.len_password)
        self.copy_password = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copy_password.setFont(font)
        self.copy_password.setObjectName("copy_password")
        self.verticalLayout.addWidget(self.copy_password)
        self.generate_new_password = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.generate_new_password.setFont(font)
        self.generate_new_password.setObjectName("generate_new_password")
        self.verticalLayout.addWidget(self.generate_new_password)
        self.delete_password = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.delete_password.setFont(font)
        self.delete_password.setObjectName("delete_password")
        self.verticalLayout.addWidget(self.delete_password)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.generate_password, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functional()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab_1_text.setText(_translate("MainWindow", "Password generator"))
        self.label_description.setText(_translate("MainWindow", "In this program you can generate a password for yourself, please go to the 2nd tab of the application."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.description), _translate("MainWindow", "description"))
        self.capital_letters_2.setText(_translate("MainWindow", "Include capital letters."))
        self.lower_case_letters_2.setText(_translate("MainWindow", "Include lower case letters."))
        self.nums_2.setText(_translate("MainWindow", "Include numbers."))
        self.special_point_2.setText(_translate("MainWindow", "include \"*?!#$%()\""))
        self.choose_amount_label.setText(_translate("MainWindow", "choose number of passwords"))
        self.choose_password_len_label.setText(_translate("MainWindow", "choose password length"))
        self.copy_password.setText(_translate("MainWindow", "copy password"))
        self.generate_new_password.setText(_translate("MainWindow", "generate password"))
        self.delete_password.setText(_translate("MainWindow", "new password"))
        self.pushButton.setText(_translate("MainWindow", "generate password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generate_password), _translate("MainWindow", "generate password"))

    def add_functional(self):
        self.generate_new_password.clicked.connect(self.make_new_password)
        self.copy_password.clicked.connect(self.copy_password_funk)


    def make_new_password(self):
        a = []
        output = []
        if self.nums_2.isChecked() is False and self.capital_letters_2.isChecked() is False and self.lower_case_letters_2.isChecked() is False and self.special_point_2.isChecked() is False:
            self.main_label.setText('not enough characters to generate a password')
        else:
            if self.nums_2.isChecked():
                a.append('0123456789')
            if self.capital_letters_2.isChecked():
                a.append('QWERTYUIOPASDFGHJKLZXCVBNM')
            if self.lower_case_letters_2.isChecked():
                a.append('qwertyuiopasdfghjklzxcvbnm')
            if self.special_point_2.isChecked():
                a.append('*?!#$%()')
            kort = ''.join(a)
            len_password = self.len_password.value()
            amount_of_passwords = self.amount_password.value()

            for i in range(amount_of_passwords):
                c = ''.join(random.sample(kort,len_password))
                output.append(c)
            result = '   |   '.join(output)
            self.main_label.setText(result)

    def copy_password_funk(self):
        if len(self.main_label.text()) == 0:
            self.main_label.setText('not enough characters to copy')
        else:
            a = self.main_label.text()
            pyperclip.copy(a)
            self.main_label.setText('successfully copied')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
