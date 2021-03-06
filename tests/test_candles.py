import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_aggregated_candles(nomics):
    data = nomics.Candles.get_candles(interval = "1d", base = "BTC")
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_exchange_candles(nomics):
    data = nomics.Candles.get_candles(interval = "1d", base = "BTC", quote = 'USDT', exchange = 'binance')
    assert isinstance(data, list)
    assert len(data) > 0

# Add back in when I get access to this API
'''def test_get_aggregated_candles_pair(nomics):
    data = nomics.Candles.get_candles(interval = "1d", base = "BTC", quote = "USDT")
    assert isinstance(data, list)
    assert len(data) > 0'''