import functools

from PyQt6.QtWidgets import  QTableWidgetItem

class Controller:

    def __init__(self, view, model):

        self.__view = view
        self.__model = model
        self.buttons_connection()
        
    def buttons_connection(self):

        self.__pushbuttons = self.__view.get_pushbuttons()
        self.__checkbuttons = self.__view.get_checkbuttons()
        self.__tables = self.__view.get_tables()
        self.__connection_first_tab()
        self.__connection_fourth_tab()
        self.__connection_fifth_tab()
        self.__connection_sixth_tab()
        self.__connection_seventh_tab()
    
    def __connection_first_tab(self):

        tab_path = self.__pushbuttons["FirstTabApp"]

        browse_button = tab_path["Browse Timesheets"]
        rename_button = tab_path["Rename Timesheets"]
        browse_button.clicked.connect(functools.partial(self.__model.tab1.browse, browse_button))
        rename_button.clicked.connect(self.__model.tab1.renaming_timesheets)

        browse_button = tab_path["Browse Sales Invoices"]
        split_button = tab_path["Split"]
        rename_button = tab_path["Rename Invoices"]
        browse_button.clicked.connect(functools.partial(self.__model.tab2.browse, browse_button))
        split_button.clicked.connect(self.__model.tab2.split_pdf)
        rename_button.clicked.connect(self.__model.tab2.renaming_invoices)
       
        browsepb_button = tab_path["Browse Purchase Book"]
        browseinvoices_button = tab_path["Browse Invoices"]

        rename_button = tab_path["Rename"]
        browsepb_button.clicked.connect(self.__model.tab3.browse_pb)
        browseinvoices_button.clicked.connect(functools.partial(self.__model.tab3.browse, browseinvoices_button))
        rename_button.clicked.connect(functools.partial(self.__execute_action, rename_button))
    
    
        
    def __execute_action(self, button):

        check_buttons_path = self.__checkbuttons["FirstTabApp", "layout_purchases"]
        check_button_contractor = check_buttons_path["Contractor Invoices"]
        check_button_noncontractor = check_buttons_path["Non-contractor Invoices"]
        check_button_other = check_buttons_path["Other Invoices"]
   
        if check_button_contractor.isChecked():
            button.clicked.connect(self.__model.tab3.renaming_contractors)
            
        if check_button_noncontractor.isChecked() or check_button_other.isChecked():
            button.clicked.connect(self.__model.tab3.renaming_noncontractors_other)
    
    
    def __connection_fourth_tab(self):

        tab_path = self.__pushbuttons["SecondTabApp"]
    
        browse_button = tab_path["Browse PDF Salaries File"]
        extract_salaries_button = tab_path["Extract Salaries"]
        export_salaries_button = tab_path["Export Salaries"]

        browse_button.clicked.connect(functools.partial(self.__model.tab4.browse, browse_button))
        extract_salaries_button.clicked.connect(self.__get_list_fourth_tab)
        export_salaries_button.clicked.connect(self.__model.tab4.write_excel)
    
    def __get_list_fourth_tab(self):

        if self.__model.tab4.salaries_extract():
            data =  self.__model.tab4.salaries_extract()
            table = self.__tables["SecondTabApp"]["table4"]
            num_rows = len(data)
            num_columns = len(data[0]) if data else 0

            table.setRowCount(num_rows)
            table.setColumnCount(num_columns)
            table.setSortingEnabled(True)

            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    table.setItem(row_idx, col_idx, item)

    def __connection_fifth_tab(self):

        tab_path = self.__pushbuttons["ThirdTabApp"]
    
        browse_button = tab_path["Browse Clarity Extract"]
        extract_clarity_button = tab_path["Extract Clarity Details"]
        export_clarity_button = tab_path["Export Details"]
        browse_button.clicked.connect(functools.partial(self.__model.tab5.browse, browse_button))
        extract_clarity_button.clicked.connect(self.__get_dataframe_from_fifth_tab)
        export_clarity_button.clicked.connect(self.__model.tab5.export_clarity_to_excel)
        
    def __get_dataframe_from_fifth_tab(self):
        
        data = self.__model.tab5.extract_clarity_details()
        if data is not None:
            
            table = self.__tables["ThirdTabApp"]["table3"]
            columns_names = data.columns.to_list()
            rows, cols = data.shape
                
            table.setRowCount(rows)
            table.setColumnCount(cols)
            table.setHorizontalHeaderLabels(columns_names)
            table.setSortingEnabled(True)

            for row in range(rows):
                for col in range(cols):
                    item = QTableWidgetItem(str(data.iat[row, col]))
                    table.setItem(row, col, item)

    def __connection_sixth_tab(self):

        tab_path = self.__pushbuttons["FourthTabApp"]
    
        browse_button = tab_path["Browse Order Books"]
        extract_clarity_button = tab_path["Extract Order Book"]
        export_clarity_button = tab_path["Export Order Book"]
        browse_button.clicked.connect(functools.partial(self.__model.tab6.browse))
        extract_clarity_button.clicked.connect(self.__get_dataframe_from_sixth_tab)
        export_clarity_button.clicked.connect(self.__model.tab6.export_order_book)

    def __get_dataframe_from_sixth_tab(self):
        
        data = self.__model.tab6.order_book_cleaner()
        if data is not None:
            
            table = self.__tables["FourthTabApp"]["table4"]
            columns_names = data.columns.to_list()
            rows, cols = data.shape
                
            table.setRowCount(rows)
            table.setColumnCount(cols)
            table.setHorizontalHeaderLabels(columns_names)
            table.setSortingEnabled(True)

            for row in range(rows):
                for col in range(cols):
                    item = QTableWidgetItem(str(data.iat[row, col]))
                    table.setItem(row, col, item)
    

    def __connection_seventh_tab(self):

        tab_path = self.__pushbuttons["FifthTabApp"]
        browse_button = tab_path["Browse Database"]
        export_clarity_button = tab_path["Export Sales Lists"]
        browse_button.clicked.connect(functools.partial(self.__model.tab7.browse))
        export_clarity_button.clicked.connect(self.__model.tab7.export_sales_list)
            
    