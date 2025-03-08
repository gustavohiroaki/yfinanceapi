import pytest
from ...get_ticker import get_ticker

def test_get_ticker(mocker):
    yf = mocker.Mock()
    yf.Ticker().info = {'result': 'value'}
    assert get_ticker(yf, 'test') == {'result': 'value'}
    assert yf.Ticker.called
    assert yf.Ticker.call_args[0][0] == 'test'