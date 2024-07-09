import random
import string
from . import run_command

def random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def test_before_key():
    kvs = {}
    for _ in range(100):
        key = random_string()
        value = random_string()
        kvs[key] = value
        run_command(['set', key, value])
    
    for key,value in kvs.items(): 
        result = run_command(['get', key])
        assert value in result.stdout
    keys = random.choices(list(kvs.values()), k=50)
    for key in keys:
        result = run_command(['del', key])
    for key in keys:
        result = run_command(['get', key])
        assert 'Key not found' in result.stdout