import pandas as pd

def add_ema(df: pd.DataFrame, period: int = 20):
    df[f"EMA_{period}"] = df["close"].ewm(span=period).mean()
    return df

def add_sma(df: pd.DataFrame, period: int = 20):
    df[f"SMA_{period}"] = df["close"].rolling(period).mean()
    return df

def add_rsi(df: pd.DataFrame, period: int = 14):
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df
