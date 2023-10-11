from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                              QRadioButton,QPushButton, QGridLayout, 
                              QTableWidget)

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                             QTableWidget, QHBoxLayout, QRadioButton, 
                             QGridLayout, QFrame, QLabel, QSizePolicy)
from PyQt6.QtGui import QFont, QCursor

from PyQt6.QtCore import QSize, Qt, QCoreApplication

from cubematchfinance.assets.config.config import cfg_item

class TabBase(QWidget):

    def __init__(self, config_path) :

        super().__init__()
        self.config_path = config_path
        self.__name = cfg_item(*self.config_path, "name")
        self.__tab_layout = QVBoxLayout()
        self.setLayout(self.__tab_layout)
        self.__tab_widgets()

    def __tab_widgets(self):
        self.__create_buttons()
        self.__create_table()

    def __create_buttons(self):
        button_names = cfg_item(*self.config_path, "push_buttons", "names")
        positions = cfg_item(*self.config_path, "push_buttons", "pos")
        self.buttons_layout = QGridLayout()
        self.__tab_layout.addLayout(self.buttons_layout)
        self.__pushbuttons = {}

        for name, pos in zip(button_names, positions):
            self.__pushbuttons[name] = QPushButton(name, parent = self)
            self.__pushbuttons[name].setFixedSize(*cfg_item(*self.config_path, "push_buttons", "size"))
            self.__pushbuttons[name].setStyleSheet(self.__css_style(cfg_item('view','button_style')))
            self.buttons_layout.addWidget(self.__pushbuttons[name], *pos)

    def __create_table(self):
        if "tables" in cfg_item(*self.config_path):
            table_layout = QHBoxLayout()
            self.__tab_layout.addLayout(table_layout)
            self.__tables = {}
            table_name = cfg_item(*self.config_path, "tables", "names")
            self.__tables[table_name] = QTableWidget()
            self.__tab_layout.addWidget(self.__tables[table_name])
    
    def __css_style(self, styles_data):
        css_style = ""
        for key, value in styles_data.items():
            css_style += f"{key}: {value}; "
        return css_style

    def get_name(self):
        return self.__name

    def get_pushbuttons(self):
        return self.__pushbuttons
    
    def get_tables(self):
        return self.__tables

class FirstTabApp(QWidget):

    def __init__(self):

        super().__init__()
        self.config_path = ("tabs", 'tab1')
        self.__name = cfg_item(*self.config_path, "name")
        self.__main_gridLayout = QGridLayout(self)
  
        self.__tab_widgets()

    def __tab_widgets(self):
        self.__pushbuttons = {}
        self.__create_buttons_timesheets()
        self.__create_buttons_sales()
        self.__create_buttons_purchases()
        self.__create_lines()
        self.__create_labels()
        self.__create_check_buttons()

        
    def __create_buttons_timesheets(self):

        button_names = cfg_item(*self.config_path, "layout_timesheets","push_buttons", "names")
        positions = cfg_item(*self.config_path, "layout_timesheets","push_buttons", "pos")

        for name, pos in zip(button_names, positions):
            self.__pushbuttons[name] = QPushButton(name, parent=self)
            self.__pushbuttons[name].setFixedSize(*cfg_item(*self.config_path, "layout_timesheets",  "push_buttons", "size"))
            self.__pushbuttons[name].setStyleSheet(self.__css_style(cfg_item('view','button_style')))
            self.__main_gridLayout.addWidget(self.__pushbuttons[name], *pos)
    
    def __create_buttons_sales(self):
        
        button_names = cfg_item(*self.config_path, "layout_sales","push_buttons", "names")
        positions = cfg_item(*self.config_path, "layout_sales","push_buttons", "pos")

        for name, pos in zip(button_names, positions):
            self.__pushbuttons[name] = QPushButton(name, parent=self)
            self.__pushbuttons[name].setFixedSize(*cfg_item(*self.config_path, "layout_sales",  "push_buttons", "size"))
            self.__pushbuttons[name].setStyleSheet(self.__css_style(cfg_item('view','button_style')))
            self.__main_gridLayout.addWidget(self.__pushbuttons[name], *pos)
    
    def __create_buttons_purchases(self):
        
        button_names = cfg_item(*self.config_path, "layout_purchases","push_buttons", "names")
        positions = cfg_item(*self.config_path, "layout_purchases","push_buttons", "pos")

        for name, pos in zip(button_names, positions):
            self.__pushbuttons[name] = QPushButton(name, parent=self)
            self.__pushbuttons[name].setFixedSize(*cfg_item(*self.config_path, "layout_purchases",  "push_buttons", "size"))
            self.__pushbuttons[name].setStyleSheet(self.__css_style(cfg_item('view','button_style')))
            self.__main_gridLayout.addWidget(self.__pushbuttons[name], *pos)

    def __create_check_buttons(self):
        names = cfg_item(*self.config_path,"layout_purchases", "check_buttons", "names")
        positions = cfg_item(*self.config_path, "layout_purchases","check_buttons", "pos")
        self.__checkbuttons = {}   
        for name, pos in zip(names, positions):
                self.__checkbuttons[name] = QRadioButton(name, parent = self)
                self.__checkbuttons[name].setFixedSize(*cfg_item(*self.config_path, "layout_purchases","check_buttons", "size"))
                self.__main_gridLayout.addWidget(self.__checkbuttons[name], *pos)
   
    def __create_lines(self):
        self.line_2 = QFrame(self)
        self.line_2.setMaximumSize(QSize(50, 16777215))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.__main_gridLayout.addWidget(self.line_2, 3, 6, 6, 1)
        self.line_4 = QFrame(self)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.__main_gridLayout.addWidget(self.line_4, 0, 6, 1, 1)     
        self.line_5 = QFrame(self)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.__main_gridLayout.addWidget(self.line_5, 2, 0, 1, 10)
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(50, 16777215))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.__main_gridLayout.addWidget(self.line, 3, 2, 6, 1)
        self.line_3 = QFrame(self)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.__main_gridLayout.addWidget(self.line_3, 0, 2, 1, 1)
    
    def __create_labels(self):
        self.label_3 = QLabel(self)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(88)
        sizePolicy2.setVerticalStretch(88)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(0, 0)
        self.label_3.setMaximumSize(16777215, 50)
        font4 = QFont()
        font4.setFamily("Consolas")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.label_3.setFont(font4)
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Purchase Invoices", None))
        self.__main_gridLayout.addWidget(self.label_3, 0, 7, 1, 3)
        self.label_2 = QLabel(self)
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.label_2.setFont(font3)
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sales Invoices", None))
        self.__main_gridLayout.addWidget(self.label_2, 0, 3, 1, 3)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__main_gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timesheets", None))


    def __css_style(self, styles_data):
        css_style = ""
        for key, value in styles_data.items():
            css_style += f"{key}: {value}; "
        return css_style

    def get_name(self):
        return self.__name

    def get_pushbuttons(self):
        return self.__pushbuttons

    def get_checkbuttons(self):
        return self.__checkbuttons
    

class SecondTabApp(TabBase):

    def __init__(self):
        super().__init__(("tabs", 'tab2'))

class ThirdTabApp(TabBase):

    def __init__(self):
        super().__init__(("tabs", 'tab3'))

class FourthTabApp(TabBase):

    def __init__(self):
        super().__init__(("tabs", 'tab4'))

class FifthTabApp(TabBase):

    def __init__(self):
        super().__init__(("tabs", 'tab5'))
