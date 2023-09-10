import functools

class Controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__connect_signals()

    def __connect_signals(self):
        buttons = self.__view.get_buttons()
        for button, object in buttons.items():
            if "Browse" in button:
                print(button)
