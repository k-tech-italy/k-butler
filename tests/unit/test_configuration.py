import tempfile
from pathlib import Path

import pytest
import yaml

from k_butler.configuration import ConfigStorage


@pytest.fixture(scope="module", autouse=True)
def load_registry():
    from k_butler.strategies.base import Registry
    Registry().load()


@pytest.fixture()
def mocker_platform_path(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        def fx(strategy = '__global__.yaml'):
            monkeypatch.setattr('k_butler.configuration.ConfigStorage._get_config_path', lambda _: Path(tmpdir) / strategy)
            return Path(tmpdir)
        yield fx


def test_global_configuration_read_autocreate(mocker_platform_path):
    mocker_platform_path()

    cfg = ConfigStorage().read()

    from k_butler import configuration
    with (Path(configuration.__file__).parent / '__global__.example.yaml').open('r') as f:
        expected = yaml.safe_load(f)

    assert cfg == expected


def test_strategy_configuration_read_autocreate(mocker_platform_path):
    mocker_platform_path('sw_payroll')

    cfg = ConfigStorage('sw_payroll').read()

    from k_butler.strategies.files.sw_payroll import configuration
    with (Path(configuration.__file__).parent / 'example.yaml').open('r') as f:
        expected = yaml.safe_load(f)

    assert cfg == expected
