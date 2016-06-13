import pytest
from ..lib.config import Config

def test_config():
    cfg = Config('config.db')
    with pytest.raises(Exception):
        cfg = Config('')
    val = cfg.get('socket-key')

