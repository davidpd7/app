import functools

class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.buttons_connection()
        

    def buttons_connection(self):
        self.__buttons = self.__view.get_buttons()

        self.__connection_first_tab()
        self.__connection_second_tab()
        self.__connection_fourth_tab()
        self.__connection_fifth_tab()
    
    def __connection_first_tab(self):
        browse_button = self.__buttons['FirstTabApp']['Browse']
        rename_button = self.__buttons['FirstTabApp']['Rename']
        browse_button.clicked.connect(functools.partial(self.__model.tab1.browse, browse_button))
        rename_button.clicked.connect(self.__model.tab1.renaming_timesheets)

    def __connection_second_tab(self):
        browse_button = self.__buttons['SecondTabApp']['Browse']
        split_button = self.__buttons['SecondTabApp']['Split']
        rename_button = self.__buttons['SecondTabApp']['Rename']
        browse_button.clicked.connect(functools.partial(self.__model.tab2.browse, browse_button))
        split_button.clicked.connect(self.__model.tab2.split_pdf)
        rename_button.clicked.connect(self.__model.tab2.renaming_invoices)
    
    def __connection_fourth_tab(self):
    
        browse_button = self.__buttons['FourthTabApp']['Browse PDF Salaries File']
        excel_writter_button = self.__buttons['FourthTabApp']['Extract Salaries']
        browse_button.clicked.connect(functools.partial(self.__model.tab4.browse, browse_button))
        excel_writter_button.clicked.connect(self.__model.tab4.write_excel)

    def __connection_fifth_tab(self):
    
        browse_button = self.__buttons['FifthTabApp']['Browse Clarity Extract']
        extract_clarity_button = self.__buttons['FifthTabApp']['Extract Clarity Details']
        browse_button.clicked.connect(functools.partial(self.__model.tab5.browse, browse_button))
        extract_clarity_button.clicked.connect(self.__model.tab5.extract_clarity_details)

    

    
    

    
    
