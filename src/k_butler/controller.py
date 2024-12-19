from typing import Dict, List

from k_butler.filesbo import FileBo
from k_butler.strategies.base import Registry
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
        for name, StrategyKlass in Registry().strategies.items():  #TODO FIX LOAD METHOD FOR REGISTRY
            for f in files_bo:
                if not (StrategyKlass().match(f)):  # if matches the strategy will add itself to the list
                    # file_bo.handlers
                    files_bo.pop(files_bo.index(f))
                    GuiModal(f.fullpath, f'Actions not found for: {name}')
        if files_bo:
            self.windows.setdefault('test', AnotherWindowBase(files_bo)).show()


controller = Controller()
