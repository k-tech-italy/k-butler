from pathlib import Path

import platformdirs
import yaml

from k_butler.strategies.base import Registry


class ConfigStorage:
    def __init__(self, strategy_key=None):
        if strategy_key is None:
            self.strategy_filename = '__global.yaml__'
            self.example = Path(__file__).parent / '__global__.example.yaml'
        else:
            strategy = Registry().strategies[strategy_key]
            self.strategy_filename = f'modules/{strategy.configurator.get_config_filename()}'
            self.example = strategy.configurator.get_example_file()

    def _get_config_path(self):
        '''FOR TESTING use local path like this: /k-butler/.dc/example.yaml'''

        return platformdirs.user_config_path(self.strategy_filename)

    def _get_config_file(self) -> Path:
        config_file = self._get_config_path()
        if not config_file.parent.exists():
            config_file.parent.mkdir(parents=True)

        if not config_file.exists():  # autocreate with example
            import shutil
            shutil.copy(self.example, config_file)

        return config_file

    def read(self) -> dict:
        with self._get_config_file().open('r') as config_stream:
            return yaml.safe_load(config_stream)

    def write(self, config: dict):
        with self._get_config_file().open('w') as config_stream:
            config_stream.write(yaml.dump(config, default_flow_style=False))
