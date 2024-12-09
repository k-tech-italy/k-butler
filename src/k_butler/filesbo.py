from pathlib import Path


class FileBo:
    def __init__(self, fullpath: str):
        self.handlers = []  # The list of strategies that know how to handle this file
        self.fullpath = Path(fullpath)

    @property
    def name(self) -> str:
        return self.fullpath.name

    @property
    def stem(self) -> str:
        return self.fullpath.stem

    @property
    def extension(self) -> str:
        return self.fullpath.suffix[1:]

    @property
    def path(self) -> str:
        return str(self.fullpath.parent)

    @property
    def parts(self) -> tuple[str, str, str]:
        return self.path, self.stem, self.extension

    def add_handler(self, strategy):
        self.handlers.append(strategy)
