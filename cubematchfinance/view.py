import sys
import os

from PyQt6 import QtGui
from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QMessageBox, 
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QTabWidget, QRadioButton, QLabel, QListWidget,
                            QFileDialog,QListWidgetItem, QApplication, QPushButton, QGridLayout)

from PyQt6.QtGui import QPixmap, QDesktopServices
from pathlib import Path

from cubematchfinance.config.config import cfg_item

class View(QMainWindow):
     
    __title = cfg_item("app","title")
    __base_path = os.path.dirname(os.path.abspath(__file__))
    icons_path = os.path.join(__base_path, "icons")
    __app_icon_path = os.path.join(icons_path, "icon.png")
    __width, __height, __left, __top  = (720, 720, 680, 240)
    image_path = os.path.join(icons_path, "main_picture.png")

    def __init__(self):

        super().__init__()
        
        self.setWindowIcon(QtGui.QIcon(View.__app_icon_path))
        self.setWindowTitle(View.__title)

        self.setGeometry(View.__left, 
                         View.__top, 
                         View.__width, 
                         View.__height)
        self.__central_widget = QWidget(self)
        self.setCentralWidget(self.__central_widget)

 
        self.vlayout = QVBoxLayout()

        self.__central_widget.setLayout(self.vlayout)

        self.__create_and_add_tabs()

        self.__create_buttons()
        self.__create_box_buttons()
        #self.__create_list_widgets()
        self.test()
  

    
    def __create_and_add_tabs(self):

       
        self.__tabs = QTabWidget()
        self.vlayout.addWidget(self.__tabs)
        self.__tab_widgets = {}
        self.layout = QGridLayout()

        for tab in cfg_item("tabs"):
            self.__tab_widgets[tab] = QWidget()
            self.__tabs.addTab(self.__tab_widgets[tab], cfg_item("tabs", tab, "name"))
            self.__tab_widgets[tab].setLayout(self.layout)
            

    def __create_list_widgets(self):

        self.__list_widgets = {}
        for i in range(len(self.__tab_widgets)):
            list_name = 'list'+str(i)
            self.__list_widgets[list_name] = QListWidget(self)

    
    def __create_buttons(self):

       for tab in cfg_item("tabs"):
            layout = QHBoxLayout()
            button_names = cfg_item("tabs", tab, "push_buttons")
            for name in button_names:
                self.__buttons = {}
                self.__buttons[tab + name]= QPushButton(name)            
    
                

        
    def __create_box_buttons(self):
        
        names = ["Other Invoices", 
                 "Contractor Invoices", 
                 "Non-contractor Invoices"]

        self.__box__buttons = {}
        
        for name in names:
            self.__box__buttons[name]= QRadioButton(name)

    

    def test(self):
        pass #for tab in cfg_item("tabs"):
            #print(f'{tab},{cfg_item("tabs", tab, "push_buttons")}')

    




    

        
    


        
