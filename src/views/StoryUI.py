import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.controller.StoryController import StoryController
from src.controller.TreasureController import TreasureController
from src.controller.HimalayaController import HimalayaController
from src.controller.RaceController import RaceController
from src.controller.AlienController import AlienController
from src.controller.SpaceController import SpaceController
from src.controller.DramaController import DramaController
from src.controller.FantasyController import FantasyController
from src.controller.MysteryController import MysteryController
from src.controller.HorrorController import HorrorController
from src.controller.HistoricalController import HistoricalController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_storyWindow(object):
    def __init__(self, user,automaton,story,condition):
        self.user = user
        self.automaton = automaton
        self.story = story
        if condition == 1:
            self.main_controller = StoryController(self,user,automaton,story)
        if condition == 2:
            self.main_controller = TreasureController(self,user,automaton,story)
        if condition == 3:
            self.main_controller = HimalayaController(self,user,automaton,story)
        if condition == 4:
            self.main_controller = RaceController(self,user,automaton,story)
        if condition == 5:
            self.main_controller = AlienController(self,user,automaton,story)
        if condition == 6:
            self.main_controller = SpaceController(self,user,automaton,story)
        if condition == 7:
            self.main_controller = DramaController(self,user,automaton,story)
        if condition == 8:
            self.main_controller = FantasyController(self,user,automaton,story)
        if condition == 9:
            self.main_controller = MysteryController(self,user,automaton,story)
        if condition == 10:
            self.main_controller = HorrorController(self,user,automaton,story)
        if condition == 11:
            self.main_controller = HistoricalController(self,user,automaton,story)

    def setupUi(self, storyWindow):
        storyWindow.setObjectName("storyWindow")
        storyWindow.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/images/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        storyWindow.setWindowIcon(icon)
        storyWindow.setStyleSheet("background-color:#107acc;")
        self.phaseStory = QtWidgets.QLabel(storyWindow)
        self.phaseStory.setGeometry(QtCore.QRect(220, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.phaseStory.setFont(font)
        self.phaseStory.setStyleSheet("color:white;")
        self.phaseStory.setAlignment(QtCore.Qt.AlignCenter)
        self.phaseStory.setObjectName("phaseStory")
        self.option1label = QtWidgets.QLabel(storyWindow)
        self.option1label.setGeometry(QtCore.QRect(60, 100, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.option1label.setFont(font)
        self.option1label.setStyleSheet("color:white;\n"
"border: 1px solid white;\n"
"border-radius:4px;")
        self.option1label.setText("")
        self.option1label.setAlignment(QtCore.Qt.AlignCenter)
        self.option1label.setWordWrap(True)
        self.option1label.setObjectName("option1label")
        self.option2label = QtWidgets.QLabel(storyWindow)
        self.option2label.setGeometry(QtCore.QRect(340, 100, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.option2label.setFont(font)
        self.option2label.setStyleSheet("color:white;\n"
"border: 1px solid white;\n"
"border-radius:4px;")
        self.option2label.setText("")
        self.option2label.setAlignment(QtCore.Qt.AlignCenter)
        self.option2label.setWordWrap(True)
        self.option2label.setObjectName("option2label")
        self.textInp = QtWidgets.QTextEdit(storyWindow)
        self.textInp.setGeometry(QtCore.QRect(190, 320, 211, 121))
        self.textInp.setStyleSheet("background-color:white;\n"
"border-radius:5px;")
        self.textInp.setObjectName("textInp")
        self.goBtn = QtWidgets.QPushButton(storyWindow)
        self.goBtn.setGeometry(QtCore.QRect(240, 460, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.goBtn.setFont(font)
        self.goBtn.setStyleSheet("color:white;\n"
"border:1px solid white;\n"
"border-radius:4px;")
        self.goBtn.setObjectName("goBtn")
        self.nextBtn = QtWidgets.QPushButton(storyWindow)
        self.nextBtn.setEnabled(False)
        self.nextBtn.setGeometry(QtCore.QRect(470, 330, 61, 41))
        self.nextBtn.setStyleSheet("border:1px solid white;\n"
"border-radius:4px;")
        self.nextBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextBtn.setIcon(icon1)
        self.nextBtn.setIconSize(QtCore.QSize(32, 32))
        self.nextBtn.setObjectName("nextBtn")
        self.auxiliarlabel = QtWidgets.QLabel(storyWindow)
        self.auxiliarlabel.setGeometry(QtCore.QRect(60, 230, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.auxiliarlabel.setFont(font)
        self.auxiliarlabel.setStyleSheet("color:white;\n"
"border: 1px solid white;\n"
"border-radius:4px;")
        self.auxiliarlabel.setText("")
        self.auxiliarlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.auxiliarlabel.setWordWrap(True)
        self.auxiliarlabel.setObjectName("auxiliarlabel")
        self.exchangeBtn = QtWidgets.QPushButton(storyWindow)
        self.exchangeBtn.setEnabled(False)
        self.exchangeBtn.setGeometry(QtCore.QRect(60, 330, 61, 41))
        self.exchangeBtn.setStyleSheet("border:1px solid white;\n"
"border-radius:4px;")
        self.exchangeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("src/images/exchange.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exchangeBtn.setIcon(icon2)
        self.exchangeBtn.setIconSize(QtCore.QSize(32, 32))
        self.exchangeBtn.setObjectName("exchangeBtn")

        self.retranslateUi(storyWindow)
        QtCore.QMetaObject.connectSlotsByName(storyWindow)

        # ---------- ACTIONS
        self.goBtn.clicked.connect(lambda:self.main_controller.goDesc(storyWindow))
        self.nextBtn.clicked.connect(lambda:self.main_controller.nextDesc(storyWindow))
        self.exchangeBtn.clicked.connect(lambda:self.main_controller.exchange())

    def retranslateUi(self, storyWindow):
        _translate = QtCore.QCoreApplication.translate
        storyWindow.setWindowTitle(_translate("storyWindow", "Story"))
        self.phaseStory.setText(_translate("storyWindow", "Story"))
        self.goBtn.setText(_translate("storyWindow", "GO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    storyWindow = QtWidgets.QWidget()
    ui = Ui_storyWindow()
    ui.setupUi(storyWindow)
    storyWindow.show()
    sys.exit(app.exec_())
