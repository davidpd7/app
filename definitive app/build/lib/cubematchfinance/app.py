import sys
import os

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget 

class App():

    __window = QWidget()
    

    def __init__(self):
        pass

    def run(self):
        App.__window.setWindows('Hello World')

