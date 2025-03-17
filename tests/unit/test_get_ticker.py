from ...services.get_ticker import get_ticker

    
def test_get_ticker_if_data_is_cached(mocker):
    yf = mocker.Mock()
    r = mocker.Mock()
    
    r.get.return_value = {"result": "value"}
    
    result = get_ticker(yf, r, 'test')
    assert result == {'result': 'value'}
    assert yf.Ticker.not_called
    assert r.get.called
    assert r.get.call_args[0][0] == 'test'
    assert r.set.not_called

def test_get_ticker_if_exists_cache_instance_and_data_is_not_cached(mocker):
    yf = mocker.Mock()
    r = mocker.Mock()
    
    r.get.return_value = None
    yf.Ticker().info = {"result": "value"}
    
    result = get_ticker(yf, r, 'test')
    assert result == {'result': 'value'}
    assert yf.Ticker.called
    assert r.get.called
    assert r.get.call_args[0][0] == 'test'
    assert r.set.called
    assert r.set.call_args[0][0] == 'test'
    assert r.set.call_args[0][1] == {'result': 'value'}