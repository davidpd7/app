import os
import inspect

from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtWidgets import (QMainWindow,QWidget, 
                             QVBoxLayout, QTabWidget, QLabel,
                             QPushButton, QGridLayout)

from PyQt6.QtGui import QDesktopServices, QPixmap

from cubematchfinance.assets.config.config import cfg_item
import cubematchfinance.entities.tabs as tabs

class View(QMainWindow):
     
    def __init__(self):

        super().__init__()
        
        self.setWindowIcon(QIcon(os.path.join(*cfg_item("app","icon_path"))))
        self.setWindowTitle(cfg_item("app","title"))
        self.setGeometry(*cfg_item("app", "geometry"))
        
        self.__central_widget = QWidget(self)
        
        self.__main_layout = QGridLayout(self.__central_widget)
        self.setCentralWidget(self.__central_widget)


        self.__render()
        
    def __render(self):

        self.__create_and_add_tabs()
        self.__add_link_buttons()
        #self.__main_picture()
    

    def __main_picture(self):

        self.label = QLabel(self.__central_widget)
        pixmap = QPixmap(os.path.join(*cfg_item("app", "main_picture")))
        self.label.setPixmap(pixmap.scaled(self.__central_widget.size()))
        self.__main_layout.addWidget(self.label, *cfg_item('app','main_picture_pos'))


    def __create_and_add_tabs(self):
        
        tabs_list = inspect.getmembers(tabs)
        self.tab_instances = {} 
        __tabs = QTabWidget(parent = self.__central_widget)
        self.__main_layout.addWidget(__tabs,*cfg_item('app','tab_layout_pos'))
        
        for name_object, object in tabs_list:
           if inspect.isclass(object) and "TabApp" in name_object:
                tab_instance = object()
                self.tab_instances[name_object] = tab_instance  
                __tabs.addTab(tab_instance, tab_instance.get_name())
                
    def __create_link_buttons(self, button, description, url):
            
        button = QPushButton(parent = self.__central_widget)
        label = QLabel(description,parent = self.__central_widget)
        icon_size = QSize(*cfg_item("view", "icon_size"))
        button_size = QSize(*cfg_item("view", "button_size"))
        style = self.__css_style(cfg_item('view','button_style'))
        label.setStyleSheet(self.__css_style(cfg_item("view","label_style")))
        button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(url)))
        button.setIconSize(icon_size)
        button.setFixedSize(button_size)
        button.setStyleSheet(style)
        
        return button, label
    
    def __add_link_buttons(self):
            
            button_names = cfg_item("view","push_buttons")
            verticalLayout_links = QVBoxLayout()
            self.__main_layout.addLayout(verticalLayout_links, *cfg_item('app','links_layout'))

            for name in button_names:
                icon_path = os.path.join(*cfg_item("view","push_buttons", name, "icon_path"))
                url = cfg_item("view","push_buttons", name, "url")
                description = cfg_item("view","push_buttons", name, "name")
                button, label = self.__create_link_buttons(icon_path, description, url)
                button.setIcon(QIcon(icon_path))
                verticalLayout_links.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
                verticalLayout_links.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
    
    def __css_style(self, styles_data):
        css_style = ""
        for key, value in styles_data.items():
            css_style += f"{key}: {value}; "
        return css_style
        
    def get_pushbuttons(self):
        pushbuttons = {}
        for name, tab_instance in self.tab_instances.items():
            try:
                pushbuttons[name] = tab_instance.get_pushbuttons()
            except AttributeError:
                pass
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
    
    def get_tables(self):
        tables = {}
        for name, tab_instance in self.tab_instances.items():
            try:
                tab_instance.get_tables()
                tables[name] = tab_instance.get_tables()
            except AttributeError:
                pass
        return tables
    




    


        



        
    




    

        
    


        
