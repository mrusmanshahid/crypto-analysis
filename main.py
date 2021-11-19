from config import Config
from historical_data import HistoricalData
from coingecko_client import CoinGeckoClient

if __name__ == "__main__":
    Config().load_configurations()
    x = HistoricalData().get_historical_data()
    print(x)