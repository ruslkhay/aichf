import pandas as pd


def compute_indicators(prices: pd.DataFrame) -> pd.DataFrame:
    # Basic returns
    rets = prices.pct_change()

    # Rolling stats
    mom_5 = prices.pct_change(5)
    mom_20 = prices.pct_change(20)
    vol_20 = rets.rolling(20).std()
    vol_60 = rets.rolling(60).std()

    # RSI(14)
    delta = prices.diff()
    up = delta.clip(lower=0.0)
    down = -delta.clip(upper=0.0)
    roll_up = up.rolling(14).mean()
    roll_down = down.rolling(14).mean()
    rs = roll_up / (roll_down + 1e-12)
    rsi_14 = 100 - (100 / (1 + rs))

    # MACD(12,26,9)
    ema12 = prices.ewm(span=12, adjust=False).mean()
    ema26 = prices.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    macd_signal = macd.ewm(span=9, adjust=False).mean()
    macd_hist = macd - macd_signal

    # ATR-like true range proxy (using close only): rolling range of returns
    tr = (prices / prices.shift(1) - 1).abs()
    atr_14 = tr.rolling(14).mean()

    # Assemble feature panels with aligned indices
    features = {
        "returns": rets,
        "mom_5": mom_5,
        "mom_20": mom_20,
        "vol_20": vol_20,
        "vol_60": vol_60,
        "rsi_14": rsi_14,
        "macd": macd,
        "macd_signal": macd_signal,
        "macd_hist": macd_hist,
        "atr_14": atr_14,
    }
    return pd.DataFrame(features)
