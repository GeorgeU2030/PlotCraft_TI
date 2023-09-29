import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)


from controller.MainWindowController import MainWindowController
from views.Genres import Ui_GenresUI as Genres_Form
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def __init__(self):
        self.main_controller = MainWindowController(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(MainWindow.size())
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color:#107acc;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iconimg = QtWidgets.QLabel(self.centralwidget)
        self.iconimg.setGeometry(QtCore.QRect(150, 40, 61, 61))
        self.iconimg.setText("")
        self.iconimg.setPixmap(QtGui.QPixmap("images/libro.png"))
        self.iconimg.setScaledContents(True)
        self.iconimg.setObjectName("iconimg")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 40, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color:#ffffff;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 140, 311, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color:#289eee;\n"
"border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblwelcome = QtWidgets.QLabel(self.frame)
        self.lblwelcome.setGeometry(QtCore.QRect(80, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblwelcome.setFont(font)
        self.lblwelcome.setStyleSheet("color:#ffffff;")
        self.lblwelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblwelcome.setObjectName("lblwelcome")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(70, 110, 181, 139))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblwelcome_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblwelcome_2.setFont(font)
        self.lblwelcome_2.setStyleSheet("color:#ffffff;")
        self.lblwelcome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblwelcome_2.setObjectName("lblwelcome_2")
        self.verticalLayout_3.addWidget(self.lblwelcome_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color:#fff;\n"
"margin-top:20px;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#107acc;\n"
"color:white;\n"
"margin-top:20px;\n"
"padding-top:5px;\n"
"padding-bottom:5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#fff;\n"
"color:#107acc;\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ----------  Actions

        self.pushButton.clicked.connect(lambda:self.main_controller.lookgenres(Genres_Form,MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlotCraft"))
        self.title.setText(_translate("MainWindow", "PlotCraft"))
        self.lblwelcome.setText(_translate("MainWindow", "Welcome!"))
        self.lblwelcome_2.setText(_translate("MainWindow", "Enter your Name"))
        self.pushButton.setText(_translate("MainWindow", "Start"))


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app_icon = QtGui.QIcon("images/libro.png")  
    app.setWindowIcon(app_icon)
    MainWindow.show()
    sys.exit(app.exec_())
