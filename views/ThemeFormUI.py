import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controller.ThemeController import ThemeController

class Ui_ThemeForm(object):
    def __init__(self, user,automaton):
        self.user = user
        self.automaton = automaton
        self.main_controller = ThemeController(self,user,automaton)

    def setupUi(self, ThemeForm):
        ThemeForm.setObjectName("ThemeForm")
        ThemeForm.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../images/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ThemeForm.setWindowIcon(icon)
        ThemeForm.setStyleSheet("background-color:#127acc;")
        self.backBtn = QtWidgets.QPushButton(ThemeForm)
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
        self.label_5 = QtWidgets.QLabel(ThemeForm)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(ThemeForm)
        self.frame_2.setGeometry(QtCore.QRect(180, 140, 241, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.genreBtn = QtWidgets.QPushButton(self.frame_2)
        self.genreBtn.setGeometry(QtCore.QRect(30, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.genreBtn.setFont(font)
        self.genreBtn.setStyleSheet("background-color:#289ccc;\n"
"color:white;\n"
"border-radius:5px;")
        self.genreBtn.setObjectName("genreBtn")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 121, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui\\../images/romance.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ThemeForm)
        QtCore.QMetaObject.connectSlotsByName(ThemeForm)

        # ------------ actions
        self.backBtn.clicked.connect(lambda:self.main_controller.backScreen(ThemeForm))
        self.genreBtn.clicked.connect(lambda:self.main_controller.themeDesc(ThemeForm))

    def retranslateUi(self, ThemeForm):
        _translate = QtCore.QCoreApplication.translate
        ThemeForm.setWindowTitle(_translate("ThemeForm", "StartStory"))
        self.label_5.setText(_translate("ThemeForm", "Drama"))
        self.genreBtn.setText(_translate("ThemeForm", "Drama Reunion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThemeForm = QtWidgets.QWidget()
    ui = Ui_ThemeForm()
    ui.setupUi(ThemeForm)
    ThemeForm.show()
    sys.exit(app.exec_())
