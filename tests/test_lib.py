from YanShareCode.lib import try_me
from YanShareCode.lib import sqr

def test_try_me():
    assert len(try_me())>0

def test_sqr():
    assert sqr(2) == 4