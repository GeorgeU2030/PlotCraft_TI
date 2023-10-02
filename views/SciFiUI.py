import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from controller.SciFiController import SciFiController

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SciFi(object):
    def __init__(self, user,automaton):
        self.user = user
        self.automaton = automaton
        self.main_controller = SciFiController(self,user,automaton)

    def setupUi(self, SciFi):
        SciFi.setObjectName("SciFi")
        SciFi.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../../../Downloads/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        SciFi.setWindowIcon(icon)
        SciFi.setStyleSheet("background-color:#107acc\n"
";")
        self.label_5 = QtWidgets.QLabel(SciFi)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(SciFi)
        self.label_2.setGeometry(QtCore.QRect(240, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(SciFi)
        self.frame.setGeometry(QtCore.QRect(40, 150, 241, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.spaceBtn = QtWidgets.QPushButton(self.frame)
        self.spaceBtn.setGeometry(QtCore.QRect(30, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.spaceBtn.setFont(font)
        self.spaceBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.spaceBtn.setObjectName("spaceBtn")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 121, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../images/spacexploration.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(SciFi)
        self.frame_2.setGeometry(QtCore.QRect(310, 150, 241, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 80, 121, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("ui\\../images/alieninvasion.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.alienBtn = QtWidgets.QPushButton(self.frame_2)
        self.alienBtn.setGeometry(QtCore.QRect(30, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.alienBtn.setFont(font)
        self.alienBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.alienBtn.setObjectName("alienBtn")
        self.backBtn = QtWidgets.QPushButton(SciFi)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.backBtn.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#127bbc;\n"
"}")
        self.backBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../images/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.backBtn.setIcon(icon1)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(SciFi)
        QtCore.QMetaObject.connectSlotsByName(SciFi)

        # ---------- Actions

        self.backBtn.clicked.connect(lambda:self.main_controller.backScreen(SciFi))
        self.alienBtn.clicked.connect(lambda checked,text="alien":self.main_controller.scifiDesc(text,SciFi))
        self.spaceBtn.clicked.connect(lambda checked,text="space":self.main_controller.scifiDesc(text,SciFi))

    def retranslateUi(self, SciFi):
        _translate = QtCore.QCoreApplication.translate
        SciFi.setWindowTitle(_translate("SciFi", "Sci-Fi"))
        self.label_5.setText(_translate("SciFi", "Sci-Fi"))
        self.label_2.setText(_translate("SciFi", "Choose a Theme"))
        self.spaceBtn.setText(_translate("SciFi", "Space Exploration"))
        self.alienBtn.setText(_translate("SciFi", "Alien Invasion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SciFi = QtWidgets.QWidget()
    ui = Ui_SciFi()
    ui.setupUi(SciFi)
    SciFi.show()
    sys.exit(app.exec_())
