import pytest
from pom.todo_elements import Elements


@pytest.fixture
def set_up(page):
    elements = Elements(page)
    yield page
