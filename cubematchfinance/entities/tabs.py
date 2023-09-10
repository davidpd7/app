

from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QMessageBox, 
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QTabWidget, QRadioButton, QLabel, QListWidget,
                            QFileDialog,QListWidgetItem, QApplication, QPushButton, QGridLayout, QTableWidget)


from cubematchfinance.assets.config.config import cfg_item

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QHBoxLayout, QRadioButton, QGridLayout, QComboBox

class TabBase(QWidget):
    def __init__(self, config_path) :
        super().__init__()
        self.config_path = config_path
        self.__name = cfg_item(*self.config_path, "name")
        self.tab_layout = QVBoxLayout()
        self.setLayout(self.tab_layout)
        self.__tab_widgets()

    def __tab_widgets(self):
        self.__create_buttons()
        self.__create_table()
      

    def __create_buttons(self):
        button_names = cfg_item(*self.config_path, "push_buttons", "names")
        self.buttons_layout = QGridLayout()
        self.tab_layout.addLayout(self.buttons_layout)
        self.__buttons = {}

        for name in button_names:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(*cfg_item(*self.config_path, "push_buttons", "size"))
            self.buttons_layout.addWidget(self.__buttons[name])

    def __create_table(self):
        table_layout = QHBoxLayout()
        self.tab_layout.addLayout(table_layout)
        table = QTableWidget()
        table.setColumnCount(4)
        table_layout.addWidget(table)

    def get_name(self):

        return self.__name

    def get_buttons(self):
        return self.__buttons

class FirstTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab1'))
    

class SecondTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab2'))

class ThirdTabApp(TabBase):
    def __init__(self):
        super().__init__(config_path=("tabs", 'tab3')) 
        self.__create_check_buttons()
        
    def __create_check_buttons(self):
        names = cfg_item(*self.config_path, "check_buttons", "names")
        positions = cfg_item(*self.config_path, "check_buttons", "pos")
        self.__check_buttons = {}   
        for name, pos in zip(names, positions):
                self.__check_buttons[name] = QRadioButton(name)
                self.__check_buttons[name].setFixedSize(*cfg_item(*self.config_path, "check_buttons", "size"))
                self.buttons_layout.addWidget(self.__check_buttons[name], *pos)

class FourthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab4'))

class FifthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab5'))

