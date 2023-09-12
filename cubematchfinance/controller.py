import functools

class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.buttons_connection()
        

    def buttons_connection(self):
        self.__pushbuttons = self.__view.get_pushbuttons()
        self.__checkbuttons = self.__view.get_checkbuttons()

        self.__connection_first_tab()
        self.__connection_second_tab()
        self.__connection_third_tab()
        self.__connection_fourth_tab()
        self.__connection_fifth_tab()
    
    def __connection_first_tab(self):
        tab_path = self.__pushbuttons['FirstTabApp']

        browse_button = tab_path['Browse']
        rename_button = tab_path['Rename']
        browse_button.clicked.connect(functools.partial(self.__model.tab1.browse, browse_button))
        rename_button.clicked.connect(self.__model.tab1.renaming_timesheets)
        

    def __connection_second_tab(self):
        tab_path = self.__pushbuttons['SecondTabApp']

        browse_button = tab_path['Browse']
        split_button = tab_path['Split']
        rename_button = tab_path['Rename']
        browse_button.clicked.connect(functools.partial(self.__model.tab2.browse, browse_button))
        split_button.clicked.connect(self.__model.tab2.split_pdf)
        rename_button.clicked.connect(self.__model.tab2.renaming_invoices)


    def __connection_third_tab(self):
        tab_path = self.__pushbuttons['ThirdTabApp']
        
        browsepb_button = tab_path['Browse Purchase Book']
        browseinvoices_button = tab_path['Browse Invoices']
        rename_button = tab_path['Rename']
        browsepb_button.clicked.connect(self.__model.tab3.extract_pb)
        browseinvoices_button.clicked.connect(functools.partial(self.__model.tab3.browse, browseinvoices_button))
        rename_button.clicked.connect(functools.partial(self.__execute_action, rename_button))

        
    def __execute_action(self, button):
        check_buttons_path = self.__checkbuttons['ThirdTabApp']
        check_button_contractor = check_buttons_path['Contractor Invoices']
        check_button_noncontractor = check_buttons_path['Non-contractor Invoices']
        check_button_other = check_buttons_path['Other Invoices']
   
        if check_button_contractor.isChecked():
            button.clicked.connect(self.__model.tab3.renaming_contractors)
            
        if check_button_noncontractor.isChecked() or check_button_other.isChecked():
            button.clicked.connect(self.__model.tab3.renaming_noncontractors_other)
           
    
    def __connection_fourth_tab(self):
        tab_path = self.__pushbuttons['FourthTabApp']
    
        browse_button = tab_path['Browse PDF Salaries File']
        excel_writter_button = tab_path['Extract Salaries']
        browse_button.clicked.connect(functools.partial(self.__model.tab4.browse, browse_button))
        excel_writter_button.clicked.connect(self.__model.tab4.write_excel)


    def __connection_fifth_tab(self):
        tab_path = self.__pushbuttons['FifthTabApp']
    
        browse_button = tab_path['Browse Clarity Extract']
        extract_clarity_button = tab_path['Extract Clarity Details']
        browse_button.clicked.connect(functools.partial(self.__model.tab5.browse, browse_button))
        extract_clarity_button.clicked.connect(self.__model.tab5.extract_clarity_details)

    
    

    
    

    
    
