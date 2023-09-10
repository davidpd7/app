from pathlib import Path
from PyQt6.QtWidgets  import QFileDialog


class Model:

    def __init__(self):
        pass

        
    def showFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File')
        print('File Selecte:', fileName)