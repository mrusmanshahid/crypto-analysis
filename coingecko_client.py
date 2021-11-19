from pycoingecko import CoinGeckoAPI

class CoinGeckoClient:

    def __init__(self):
        self.client = CoinGeckoAPI()

    def getPrice(self,coin_id):
        return self.client.get_price(ids=coin_id, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')