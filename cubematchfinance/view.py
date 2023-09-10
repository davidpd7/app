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

        self.__vlayout = QHBoxLayout()
        self.__central_widget.setLayout(self.__vlayout)
        self.__create_and_add_tabs()
        self.add_link_buttons()

    

    
    def __create_and_add_tabs(self):

        __tabs = QTabWidget()
        self.__vlayout.addWidget(__tabs)
        self.__layout = QHBoxLayout()
        
        tabs_list = inspect.getmembers(tabs)

        for name_object, object in tabs_list:
            if inspect.isclass(object) and "TabApp" in name_object:
                tab_instance = object()
                __tabs.addTab(tab_instance, tab_instance.get_name())
    

    def create_link_buttons(self, button, description):
            
        button = QPushButton()
        label = QLabel(description)
        label.setAligment(Qt.AignCenter)
        label.setStyleSheet("font-size:")
        return button, label
    
    def add_link_buttons(self):
            
            vbox = QVBoxLayout()
            button_names = cfg_item("main", "push_buttons", "names")
            self.__buttons_links = {}
            self.__vlayout.addLayout(vbox)

            for name in button_names:
                self.__buttons_links[name] = QPushButton(name)
                self.__buttons_links[name].setFixedSize(100,20)
                vbox.addWidget(self.__buttons_links[name])

        



        
    




    

        
    


        
