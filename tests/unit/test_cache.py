from ...services.cache import Cache

def test_set_cache(mocker):
    r = mocker.Mock()
    cache = Cache(r)
    cache.set('key', {'result': 'value'})
    assert r.set.called
    assert r.set.call_args[0][0] == 'key'
    assert r.set.call_args[0][1] == "{'result': 'value'}"
    assert r.set.call_args[1]['ex'] == 14400
    
def test_get_cache_when_exists(mocker):
    r = mocker.Mock()
    cache = Cache(r)
    r.get.return_value = b"{'result': 'value'}"
    result = cache.get('key')
    assert r.get.called
    assert r.get.call_args[0][0] == 'key'
    assert result == {'result': 'value'}

def test_get_cache_when_not_exists(mocker):
    r = mocker.Mock()
    cache = Cache(r)
    r.get.return_value = None
    result = cache.get('key')
    assert r.get.called
    assert r.get.call_args[0][0] == 'key'
    assert result == None