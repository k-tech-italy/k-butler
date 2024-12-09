from typing import Dict

from k_butler.filesbo import FileBo
from k_butler.strategies.base import Registry
from k_butler.windows.common import AnotherWindowBase


class Controller:
    windows: Dict[FileBo, AnotherWindowBase] = {}
    main_window = None

    def set_main(self, window):
        if not self.main_window:
            self.main_window = window

    def get_or_create_window(self, file_bo: FileBo):
        """If a matching strategy is found the it will create a window, add it to windows dict, and return True."""
        for name, StrategyKlass in Registry().strategies.items():
            StrategyKlass().match(file_bo) # if matches the strategy will add itself to the list file_bo.handlers

        if found := bool(file_bo.handlers):
            self.windows.setdefault(file_bo, AnotherWindowBase(file_bo)).show()

        # Return False if no strategies found
        return found



controller = Controller()
