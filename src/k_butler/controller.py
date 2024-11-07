from k_butler.windows.common import AnotherWindowBase


class Controller:
    windows = {}
    main_window = None

    def set_main(self, window):
        if not self.main_window:
            self.main_window = window

    def get_or_create_window(self, title):
        return self.windows.setdefault(title, AnotherWindowBase(title))


controller = Controller()
