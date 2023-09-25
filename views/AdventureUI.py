import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from controller.AdventureController import AdventureController
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adventureUI(object):
    def __init__(self, user):
        self.user = user
        self.main_controller = AdventureController(self,user)

    def setupUi(self, adventureUI):
        adventureUI.setObjectName("adventureUI")
        adventureUI.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        adventureUI.setWindowIcon(icon)
        adventureUI.setStyleSheet("background-color:#107acc;")
        self.label = QtWidgets.QLabel(adventureUI)
        self.label.setGeometry(QtCore.QRect(210, 20, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(adventureUI)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(adventureUI)
        self.frame.setGeometry(QtCore.QRect(40, 160, 241, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.jungleBtn = QtWidgets.QPushButton(self.frame)
        self.jungleBtn.setGeometry(QtCore.QRect(30, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.jungleBtn.setFont(font)
        self.jungleBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.jungleBtn.setObjectName("jungleBtn")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 121, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/amazonas.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 121, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/himalaya.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.himalayaBtn = QtWidgets.QPushButton(self.frame)
        self.himalayaBtn.setGeometry(QtCore.QRect(30, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.himalayaBtn.setFont(font)
        self.himalayaBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.himalayaBtn.setObjectName("himalayaBtn")
        self.frame_2 = QtWidgets.QFrame(adventureUI)
        self.frame_2.setGeometry(QtCore.QRect(320, 160, 241, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.treasureBtn = QtWidgets.QPushButton(self.frame_2)
        self.treasureBtn.setGeometry(QtCore.QRect(30, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.treasureBtn.setFont(font)
        self.treasureBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.treasureBtn.setObjectName("treasureBtn")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 30, 121, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/piratas.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(60, 170, 121, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/sahara.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.raceBtn = QtWidgets.QPushButton(self.frame_2)
        self.raceBtn.setGeometry(QtCore.QRect(30, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.raceBtn.setFont(font)
        self.raceBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.raceBtn.setObjectName("raceBtn")
        self.backBtn = QtWidgets.QPushButton(adventureUI)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.backBtn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#127bbc;\n"
"}")
        self.backBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backBtn.setIcon(icon1)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(adventureUI)
        QtCore.QMetaObject.connectSlotsByName(adventureUI)


        # ----------- ACTIONS

        self.backBtn.clicked.connect(lambda:self.main_controller.backScreen(adventureUI))
        self.jungleBtn.clicked.connect(lambda checked,text="jungle":self.main_controller.jungleDesc(text))
        self.treasureBtn.clicked.connect(lambda checked,text="treasure":self.main_controller.jungleDesc(text))
        self.raceBtn.clicked.connect(lambda checked,text="race":self.main_controller.jungleDesc(text))
        self.himalayaBtn.clicked.connect(lambda checked,text="himalaya":self.main_controller.jungleDesc(text))

    def retranslateUi(self, adventureUI):
        _translate = QtCore.QCoreApplication.translate
        adventureUI.setWindowTitle(_translate("adventureUI", "Adventure"))
        self.label.setText(_translate("adventureUI", "Adventure"))
        self.label_2.setText(_translate("adventureUI", "Choose a Theme"))
        self.jungleBtn.setText(_translate("adventureUI", "Jungle Exploration"))
        self.himalayaBtn.setText(_translate("adventureUI", "HIMALAYAS"))
        self.treasureBtn.setText(_translate("adventureUI", "Treasure Hunt"))
        self.raceBtn.setText(_translate("adventureUI", "Sahara Race"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adventureUI = QtWidgets.QWidget()
    ui = Ui_adventureUI()
    ui.setupUi(adventureUI)
    adventureUI.show()
    sys.exit(app.exec_())
