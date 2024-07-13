from pathlib import Path
import pytest
from . import run_command

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    path = Path('./data/store.kv')
    if path.exists():
        path.unlink()
    yield
    if path.exists():
        path.unlink()

def test_set_key():
	result = run_command(['set', 'test_key', 'test_value'])
	assert result.returncode == 0

def test_get_key():
	run_command(['set', 'test_key', 'test_value'])  # 先设置一个键值对
	result = run_command(['get', 'test_key'])
	assert result.returncode == 0
	assert 'test_value' in result.stdout

def test_del_key():
	run_command(['set', 'test_key', 'test_value'])  # 先设置一个键值对
	result = run_command(['del', 'test_key'])
	assert result.returncode == 0
	assert 'Key not found' not in result.stdout

def test_get_nonexistent_key():
	result = run_command(['get', 'nonexistent_key'])
	assert result.returncode == 0
	assert 'Key not found' in result.stdout

def test_del_nonexistent_key():
	result = run_command(['del', 'nonexistent_key'])
	assert result.returncode == 0
	assert 'Key not found' in result.stdout