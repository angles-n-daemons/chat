import pytest
import os
from ..lib.config import Config

def test_config():
    cfg = Config('config.db')
    with pytest.raises(Exception):
        cfg = Config('')
    val = cfg.get('socket-key')

def test_config_check_create():
    cfg = Config('config.db')
    os.remove('config.db')
    assert cfg.check_config_table() == False
    cfg.create_config_table()
    assert cfg.check_config_table() == True