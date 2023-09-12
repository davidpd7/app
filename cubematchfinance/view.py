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

from cubematchfinance.assets.config.config import cfg_item
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

        self.__render()
        
    def __render(self):
         
        self.__create_and_add_tabs()
        self.__add_link_buttons()

    def __create_and_add_tabs(self):
        __tabs = QTabWidget()
        self.__vlayout.addWidget(__tabs)
        
        tabs_list = inspect.getmembers(tabs)
        self.tab_instances = {} 

        for name_object, object in tabs_list:
            if inspect.isclass(object) and "TabApp" in name_object:
                tab_instance = object()
                self.tab_instances[name_object] = tab_instance  
                __tabs.addTab(tab_instance, tab_instance.get_name())
    
                
    def create_link_buttons(self, button, description, url):
            
        button = QPushButton()
        label = QLabel(description)
      
        label.setStyleSheet("font-size: 14px")
        button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(url)))
        return button, label
    
    def __add_link_buttons(self):
            
            vbox = QVBoxLayout()
            button_names = cfg_item("main")
            self.__vlayout.addLayout(vbox)

            for name in button_names:
                icon_path = os.path.join(*cfg_item("main", name, "icon_path"))
                url = cfg_item("main", name, "url")
                description = cfg_item("main", name, "name")
                button, label = self.create_link_buttons(icon_path, description, url)
                vbox.addWidget(button)
                vbox.addWidget(label)
        
    def get_pushbuttons(self):
        pushbuttons = {}
        for name, tab_instance in self.tab_instances.items():
            pushbuttons[name] = tab_instance.get_pushbuttons()
        return pushbuttons


    def get_checkbuttons(self):
        checkbuttons = {}
        for name, tab_instance in self.tab_instances.items():
            try:
                tab_instance.get_checkbuttons()
                checkbuttons[name] = tab_instance.get_checkbuttons()
            except AttributeError:
                pass
        return checkbuttons



    


        



        
    




    

        
    


        
