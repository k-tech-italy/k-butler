import inspect
from pathlib import Path

from k_butler.configuration import ConfigStorage


class StrategyBaseConfigurator:
    page = None

    @classmethod
    def get_config_filename(cls) -> str:
        strategy_type = Path(cls.__module__).suffixes[1][1:]
        return f'{strategy_type}/{cls.__name__.lower()}.yaml'

    @classmethod
    def get_example_file(cls) -> Path:
        """Recursively find parent 'configuration' folder and return example file."""
        cursor = Path(inspect.getfile(cls)).parent
        while cursor.name != 'configuration':
            cursor = cursor.parent
        return cursor / 'example.yaml'

    @classmethod
    def get_storage(cls):
        return ConfigStorage()

    @classmethod
    def configure(cls):
        return cls.get_storage().read()

    @classmethod
    def write_config(cls, config: dict, *args, **kwargs):
        cls.get_storage().write(config)
