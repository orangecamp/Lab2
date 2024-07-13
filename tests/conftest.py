
from pathlib import Path
import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    path = Path('./data/store.kv')
    if path.exists():
        path.unlink()
    yield
    if path.exists():
        path.unlink()