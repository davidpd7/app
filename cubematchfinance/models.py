from pathlib import Path



class Model:

    def __init__(self):
        pass

    def exec_expr(self, expr):
        try:
            result = str(eval(expr, {}, {}))
        except Exception:
            result = "OP NOT SUPPORTED"

        return result

    def browse_files(self):
            try:
                self.file_list1.clear()
                filenames, _ = QFileDialog.getOpenFileNames(self, "Select Files", r"C:\\")
                if filenames:
                    return [str(Path(filename)) for filename in filenames]
            except Exception as e:
                error_message = f"An error occurred while browsing files:\n{str(e)}"
                QMessageBox.critical(self, "Error", error_message)