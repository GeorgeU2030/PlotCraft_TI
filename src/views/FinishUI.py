import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from src.controller.FinishController import FinishController

class Ui_FinishStory(object):
    def __init__(self, user):
        self.user = user
        self.main_controller = FinishController(self,user)

    def setupUi(self, FinishStory):
        FinishStory.setObjectName("FinishStory")
        FinishStory.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcimages/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        FinishStory.setWindowIcon(icon)
        FinishStory.setStyleSheet("background-color:#127acc;")
        self.label = QtWidgets.QLabel(FinishStory)
        self.label.setGeometry(QtCore.QRect(230, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FinishStory)
        self.label_2.setGeometry(QtCore.QRect(180, 90, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.storylabel = QtWidgets.QLabel(FinishStory)
        self.storylabel.setGeometry(QtCore.QRect(150, 160, 291, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.storylabel.setFont(font)
        self.storylabel.setStyleSheet("color:white;")
        self.storylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.storylabel.setWordWrap(True)
        self.storylabel.setObjectName("storylabel")
        self.label_4 = QtWidgets.QLabel(FinishStory)
        self.label_4.setGeometry(QtCore.QRect(180, 430, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.menuBtn = QtWidgets.QPushButton(FinishStory)
        self.menuBtn.setGeometry(QtCore.QRect(240, 480, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.menuBtn.setFont(font)
        self.menuBtn.setStyleSheet("color:white;\n"
"border:1px solid white;\n"
"border-radius:4px;")
        self.menuBtn.setObjectName("menuBtn")

        self.retranslateUi(FinishStory)
        QtCore.QMetaObject.connectSlotsByName(FinishStory)

        # ACTIONS
        
        self.menuBtn.clicked.connect(lambda:self.main_controller.backMenu(FinishStory))


    def retranslateUi(self, FinishStory):
        _translate = QtCore.QCoreApplication.translate
        FinishStory.setWindowTitle(_translate("FinishStory", "FinishStory"))
        self.label.setText(_translate("FinishStory", "Finish"))
        self.label_2.setText(_translate("FinishStory", "Your short story has finished"))
        self.storylabel.setText(_translate("FinishStory", "Your short story has finished thanks for use"))
        self.label_4.setText(_translate("FinishStory", "Thanks for use"))
        self.menuBtn.setText(_translate("FinishStory", "MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinishStory = QtWidgets.QWidget()
    ui = Ui_FinishStory()
    ui.setupUi(FinishStory)
    FinishStory.show()
    sys.exit(app.exec_())
