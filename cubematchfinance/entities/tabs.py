

from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QMessageBox, 
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QTabWidget, QRadioButton, QLabel, QListWidget,
                            QFileDialog,QListWidgetItem, QApplication, QPushButton, QGridLayout)


from cubematchfinance.config.config import cfg_item

class FirstTabApp(QWidget):

    __config_path = ("tabs", 'tab1')
    
    def __init__(self):
        
        super().__init__()

        self.__name = cfg_item(*FirstTabApp.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)

        self.__create_buttons()


    def __create_buttons(self):

        button_names = cfg_item(*FirstTabApp.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*FirstTabApp.__config_path, "push_buttons", "size"))
            buttons_layout.addWidget(self.__buttons[name])

    def get_name(self):
        return self.__name
    
class SecondTabApp(QWidget):

    __config_path = ("tabs", 'tab2')
    
    def __init__(self):
        super().__init__()

        self.__name = cfg_item(*SecondTabApp.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__create_buttons()

    def __create_buttons(self):

        button_names = cfg_item(*SecondTabApp.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*SecondTabApp.__config_path, "push_buttons", "size"))
            buttons_layout.addWidget(self.__buttons[name])


    def get_name(self):
        return self.__name

class ThirdTabApp(QWidget):
    
    __config_path = ("tabs", 'tab3')

    def __init__(self):
        super().__init__()

        self.__name = cfg_item(*ThirdTabApp.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__create_buttons()
        self.__create_check_buttons()

    def __create_buttons(self):

        button_names = cfg_item(*ThirdTabApp.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*ThirdTabApp.__config_path, "push_buttons","size"))
            buttons_layout.addWidget(self.__buttons[name])

    def __create_check_buttons(self):

        button_names = cfg_item(*ThirdTabApp.__config_path, "check_buttons", "names")
        buttons_layout = QHBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__check_buttons = {}

        for name in button_names:
            self.__check_buttons[name] = QRadioButton(name)
            self.__check_buttons[name].setFixedSize(*cfg_item(*ThirdTabApp.__config_path, "check_buttons", "size"))
            buttons_layout.addWidget(self.__check_buttons[name])



    def get_name(self):
        return self.__name

class FourthTabApp(QWidget):

    __config_path = ("tabs", 'tab4')
    
    def __init__(self):
        super().__init__()

        self.__name = cfg_item(*FourthTabApp.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__create_buttons()

    def __create_buttons(self):

        button_names = cfg_item(*FourthTabApp.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*FourthTabApp.__config_path, "push_buttons","size"))
            buttons_layout.addWidget(self.__buttons[name])


    def get_name(self):
        return self.__name

class FifthTabApp(QWidget):

    __config_path = ("tabs", 'tab5')
    
    def __init__(self):
        super().__init__()

        self.__name = cfg_item(*FifthTabApp.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__create_buttons()

    def __create_buttons(self):

        button_names = cfg_item(*FifthTabApp.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*FifthTabApp.__config_path, "push_buttons","size"))
            buttons_layout.addWidget(self.__buttons[name])


    def get_name(self):
        return self.__name






    