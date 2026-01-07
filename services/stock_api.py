import pandas as pd
import plotly.graph_objects as go
from services.rate_limiter import Safe_request

class StockAPI:

    def search_symbols(self, company: str) -> pd.DataFrame:
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": company,
            "apikey": API_KEY
        }

        data = Safe_request(BASE_URL, params)
        return pd.DataFrame(data.get("bestMatches", []))

    def get_daily_prices(self, symbol: str) -> pd.DataFrame:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
        }

        data = Safe_request(BASE_URL, params)

        if "Time Series (Daily)" not in data:
            return pd.DataFrame()

        df = pd.DataFrame(data["Time Series (Daily)"]).T

        df = df.rename(columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume"
        })

        df = df.astype(float)
        df.index = pd.to_datetime(df.index)

        return df.sort_index()

    def plot_candlestick(self, df: pd.DataFrame):
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=df.index,
                    open=df["open"],
                    high=df["high"],
                    low=df["low"],
                    close=df["close"]
                )
            ]
        )
        return fig
