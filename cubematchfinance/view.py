import sys
import os
import inspect

from PyQt6 import QtGui
from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QMessageBox, 
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QTabWidget, QRadioButton, QLabel, QListWidget,
                            QFileDialog,QListWidgetItem, QApplication, QPushButton, QGridLayout)

from PyQt6.QtGui import QPixmap, QDesktopServices
from pathlib import Path

from cubematchfinance.config.config import cfg_item
import cubematchfinance.entities.tabs as tabs



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

    
    def __create_and_add_tabs(self):

        __tabs = QTabWidget()
        self.vlayout.addWidget(__tabs)
        self.__layout = QHBoxLayout()
        
        tabs_list = inspect.getmembers(tabs)

        for name_object, object in tabs_list:
            if inspect.isclass(object) and "TabApp" in name_object:
                tab_instance = object()
                __tabs.addTab(tab_instance, tab_instance.get_name())
            
    def __create_list_widgets(self):

        self.__list_widgets = {}
        for i in range(len(self.__tab_widgets)):
            list_name = 'list'+str(i)
            self.__list_widgets[list_name] = QListWidget(self)

    
    def __create_buttons(self):

        for tab in cfg_item("tabs"):
            button_names = cfg_item("tabs", tab, "push_buttons")
            layout = QHBoxLayout()
            for name in button_names:
                button = QPushButton(name)
                self.__layout.addWidget(button) 
        
    def __create_box_buttons(self):
        
        for tab in cfg_item("tabs"):
            if 'check_buttons' in cfg_item("tabs", tab):
                button_names = cfg_item("tabs", tab, "check_buttons")
                layout_check_box = QHBoxLayout()
                self.__tab_widgets[tab].setLayout(layout_check_box)  
                for name in button_names:
                    button = QRadioButton(name)
                    layout_check_box.addWidget(button) 
            
    def test(self):
        pass 



        
    




    

        
    


        
