

from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QMessageBox, 
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QTabWidget, QRadioButton, QLabel, QListWidget,
                            QFileDialog,QListWidgetItem, QApplication, QPushButton, QGridLayout, QTableWidget)


from cubematchfinance.config.config import cfg_item

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QHBoxLayout, QRadioButton, QGridLayout, QComboBox

class TabBase(QWidget):
    def __init__(self, config_path):
        super().__init__()
        self.__config_path = config_path
        self.__name = cfg_item(*self.__config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__tab_widgets()

    def __tab_widgets(self):
        self.__create_buttons()
        self.__create_table()

    def __create_buttons(self):
        button_names = cfg_item(*self.__config_path, "push_buttons", "names")
        buttons_layout = QVBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*self.__config_path, "push_buttons", "size"))
            buttons_layout.addWidget(self.__buttons[name])

    def __create_table(self):
        table_layout = QHBoxLayout()
        self.__tab_layout.addLayout(table_layout)
        table = QTableWidget()
        table.setColumnCount(4)
        table_layout.addWidget(table)

    def get_name(self):

        return self.__name

class FirstTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab1'))

class SecondTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab2'))

class ThirdTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab3'))

      
    def __create_check_buttons(self):

        button_names = cfg_item(*ThirdTabApp.__config_path, "check_buttons", "names")
        buttons_layout = QHBoxLayout()
        self.__tab_layout.addLayout(buttons_layout)
        self.__check_buttons = {}

        for name in button_names:
            self.__check_buttons[name] = QRadioButton(name)
            self.__check_buttons[name].setFixedSize(*cfg_item(*ThirdTabApp.__config_path, "check_buttons", "size"))
            buttons_layout.addWidget(self.__check_buttons[name])


class FourthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab4'))

class FifthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab5'))

