import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# -------------------------------------
# 1. Get S&P 100 constituents
# -------------------------------------

tickers = [
    "AAPL", "ABBV", "ABT", "ACN", "ADBE", "AIG", "AMD", "AMGN", "AMT", "AMZN",
    "AVGO", "AXP", "BA", "BAC", "BK", "BKNG", "BLK", "BMY", "BRK.B", "C",
    "CAT", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS", "CVX",
    "DE", "DHR", "DIS", "DUK", "EMR", "FDX", "GD", "GE", "GILD", "GM",
    "GOOG", "GS", "HD", "HON", "IBM", "INTC", "INTU", "ISRG", "JNJ",
    "JPM", "KO", "LIN", "LLY", "LMT", "LOW", "MA", "MCD", "MDLZ", "MDT",
    "MET", "META", "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE",
    "NOW", "NVDA", "ORCL", "PEP", "PFE", "PG", "PLTR", "PM", "PYPL", "QCOM",
    "RTX", "SBUX", "SCHW", "SO", "SPG", "T", "TGT", "TMO", "TMUS", "TSLA",
    "TXN", "UBER", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WFC", "WMT", "XOM"
]
# Ensure tickers are in Yahoo Finance format
tickers = [t.replace('.', '-') for t in tickers]

print(f"Found {len(tickers)} tickers:")
print(tickers)

# -------------------------------------
# 2. Define date range (last 25 years)
# -------------------------------------
end_date = datetime.today()
start_date = end_date - timedelta(days=25 * 365)

# -------------------------------------
# 3. Download S&P 100 index (^OEX)
# -------------------------------------
oex_close = yf.download(
    "^OEX",
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d")
)["Close"]

print("\nS&P 100 Index Close:")
print(oex_close.head())

# -------------------------------------
# 4. Download close prices for all S&P 100 members
# -------------------------------------
data = yf.download(
    tickers,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d")
)["Close"]

print("\nMember Close Prices:")
print(data.head())
data.to_csv('closing_prices.csv')
