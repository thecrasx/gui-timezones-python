from PySide6.QtCore import QThread, QObject, Signal
from time import sleep


class CustomSignal(QObject):
    timeChanged = Signal()


class Timer(QThread):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.__customSignal = CustomSignal()
        self.timeChanged = self.__customSignal.timeChanged


    def run(self):
        while True:
            self.timeChanged.emit()
            sleep(1)