import pytest
from api.get_resources import GetFoldersAndFiles

@pytest.fixture(scope="session")
def resources_api():
    resources = GetFoldersAndFiles().get_resources()
    yield resources