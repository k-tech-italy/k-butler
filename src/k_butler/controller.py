from typing import Dict, List

from k_butler.filesbo import FileBo
from k_butler.strategies import Registry
from k_butler.windows.file_handler import AnotherWindowBase
from k_butler.components.common import GuiModal


class Controller:
    windows: Dict[str, AnotherWindowBase] = {}
    main_window = None

    def set_main(self, window):
        if not self.main_window:
            self.main_window = window

    def get_or_create_window(self, files_bo: List[FileBo]):
        """If a matching strategy is found it will create a window, add it to windows dict, and return True."""
        for name, StrategyKlass in Registry().strategies.items():  # TODO FIX LOAD METHOD FOR REGISTRY
            for f in files_bo:
                if not (StrategyKlass().match(f)):  # if matches the strategy will add itself to the list
                    # file_bo.handlers
                    files_bo.pop(files_bo.index(f))
                    GuiModal(str(f.fullpath), f'No strategy configured for {f.name}, please configure it in config tab.').show()
        if files_bo:
            self.windows.setdefault('test', AnotherWindowBase(files_bo)).show()

    def set_main_in_front(self):
        self.main_window.tabs.tab.setCurrentIndex(2)
        self.main_window.raise_()
        self.main_window.activateWindow()


controller = Controller()
