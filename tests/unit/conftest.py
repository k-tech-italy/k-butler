import pytest


@pytest.fixture
def mock_file_bo(mock_strategy):
    class MockFileBo:
        def __init__(self, file_path):
            self.file_path = file_path
            self.handlers = [mock_strategy]
            self.name = 'Mock file bo'

    yield MockFileBo


@pytest.fixture
def mock_configurator():
    class MockConfigurator:
        name = 'Mock configurator'
        key = 'mock-configurator'

        def get_config(self, action):
            return {'test': 'test'}

    yield MockConfigurator


@pytest.fixture
def mock_strategy(mock_configurator):
    class MockStrategy:
        name = 'Mock strategy'
        key = 'mock'
        actions = {'test action': 'test action'}
        configurator = mock_configurator

        def match(self, file_bo):
            return True

        def get_action(self, action, file_bo):
            assert action == 'test'
            assert file_bo is not None

    yield MockStrategy
