import sys

from PyQt6.QtWidgets import QApplication

from cubematchfinance.view import View


def main(args = None):

    app = QApplication(sys.argv)
    view = View()
    view.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    
    