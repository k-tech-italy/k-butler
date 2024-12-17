from pathlib import Path

import platformdirs
import yaml


class ConfigStorage:
    def __init__(self, strategy = None):
        if strategy is None:
            self.strategy = '__global.yaml__'
            self.example = Path(__file__).parent / '__global__.example.yaml'
        else:
            self.strategy = f'modules/{strategy.configurator.get_config_filename()}'
            self.example = strategy.configurator.get_example_file()  # TODO: check how to do

    def _get_config_path(self):
        return platformdirs.user_config_path(self.strategy)

    def _get_config_file(self) -> Path:

        config_file = self._get_config_path(self.strategy)
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
