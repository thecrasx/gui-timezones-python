from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui import Ui_MainWindow
import sys

from timezones import TimeZone
from timer import Timer


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timezone = TimeZone()

        for i in self.timezone.all_timezones:
            self.ui.comboBox.addItem(i)

        self.ui.comboBox.currentIndexChanged.connect(self.__onCurrentIndexChanged)

        self.timer = Timer(self)
        self.timer.timeChanged.connect(self.__showTime)
        self.timer.start()
        
        self.show()

    
    def __onCurrentIndexChanged(self):
        self.timezone.changeTimeZone(self.ui.comboBox.currentText())
        self.ui.label.setText(self.timezone.getTime())

    

    def __showTime(self):
        self.ui.label.setText(self.timezone.getTime())






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec())