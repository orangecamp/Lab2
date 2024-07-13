from pathlib import Path
from . import run_command


def test_set_key():
    result = run_command(['set', 'test_key', 'test_value'])
    assert Path('./data/store.kv').exists()
    assert result.returncode == 0
        
def test_get_key():
    run_command(['set', 'test_key', 'test_value'])
    run_command(['del', 'test_key'])
    result = run_command(['get', 'test_key'])
    assert result.returncode == 0
    assert 'Key not found' in result.stdout
    assert Path('./data/store.kv').exists()
    
def test_del_key():
    result = run_command(['del', 'test_key'])
    assert result.returncode == 0
    assert 'Key not found' in result.stdout
    assert Path('./data/store.kv').exists()

