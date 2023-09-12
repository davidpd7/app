

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
        positions = cfg_item(*self.config_path, "push_buttons", "pos")
        self.buttons_layout = QGridLayout()
        self.tab_layout.addLayout(self.buttons_layout)
        self.__pushbuttons = {}

        for name, pos in zip(button_names, positions):
            self.__pushbuttons[name] = QPushButton(name)
            self.__pushbuttons[name].setFixedSize(*cfg_item(*self.config_path, "push_buttons", "size"))
            self.buttons_layout.addWidget(self.__pushbuttons[name], *pos)

    def __create_table(self):
        table_layout = QHBoxLayout()
        self.tab_layout.addLayout(table_layout)
        table = QTableWidget()
        table.setColumnCount(4)
        table_layout.addWidget(table)

    def get_name(self):

        return self.__name

    def get_pushbuttons(self):
        return self.__pushbuttons

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
        self.__checkbuttons = {}   
        for name, pos in zip(names, positions):
                self.__checkbuttons[name] = QRadioButton(name)
                self.__checkbuttons[name].setFixedSize(*cfg_item(*self.config_path, "check_buttons", "size"))
                self.buttons_layout.addWidget(self.__checkbuttons[name], *pos)
    
    def get_checkbuttons(self):
        return self.__checkbuttons

class FourthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab4'))

class FifthTabApp(TabBase):
    def __init__(self):
        super().__init__(("tabs", 'tab5'))

