from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf


ticker = "TSLA"
filename = "tsla.csv"


def download_data():
    tsla = yf.Ticker(ticker)
    hist = tsla.history(period="max", interval="1d")
    hist.to_csv(filename)


def read_data():
    hist = None
    if Path(filename).exists():
        hist = pd.read_csv(filename, index_col=0, parse_dates=True)
    return hist


hist = read_data()


if __name__ == "__main__":
    download_data()
