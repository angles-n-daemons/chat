import pytest
import os
from ..lib.config import Config

def test_config_init():
    cfg = Config('config.db')
    with pytest.raises(Exception):
        cfg = Config('')

def test_config_check_create():
    cfg = Config('config.db')
    assert cfg.check_config_table() == True
    with pytest.raises(Exception):
        cfg.create_config_table()

def test_insert():
    cfg = Config('config.db')
    
    with pytest.raises(Exception):
        cfg.set('', '')
    with pytest.raises(Exception):
        cfg.set('', 'val')
    with pytest.raises(Exception):
        cfg.set('id', '')
    cfg.set('id', 'val')

def test_retrieve():
    cfg = Config('config.db')
    cfg.set('test_item', 'item_val')
    assert cfg.get('test_item') == 'item_val'