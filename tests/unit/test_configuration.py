import tempfile
from pathlib import Path

import pytest
import yaml

from k_butler.configuration import ConfigStorage


@pytest.fixture()
def mocked_platform_path(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        monkeypatch.setattr('k_butler.configuration.ConfigStorage._get_config_path', lambda _, strategy: Path(tmpdir) / strategy)
        yield Path(tmpdir)


def test_global_configuration_read_autocreate(mocked_platform_path):

    cfg = ConfigStorage().read()

    from k_butler import configuration
    with (Path(configuration.__file__).parent / '__global__.example.yaml').open('r') as f:
        expected = yaml.safe_load(f)

    assert cfg == expected


def test_strategy_configuration_read_autocreate(mocked_platform_path):

    from k_butler.strategies.files.sw_payroll.sw_payroll import SwPayrollStrategy
    cfg = ConfigStorage(SwPayrollStrategy).read()

    from k_butler.strategies.files.sw_payroll import configuration
    with (Path(configuration.__file__).parent / 'example.yaml').open('r') as f:
        expected = yaml.safe_load(f)

    assert cfg == expected
