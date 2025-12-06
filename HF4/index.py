import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

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
    start="2000-01-01",
    end=end_date.strftime("%Y-%m-%d")
)["Close"]

print("\nS&P 100 Index Close:")
print(oex_close.head())

# -------------------------------------
# 4. Download close prices for all S&P 100 members
# -------------------------------------

print("\nMember Close Prices:")
print(oex_close.head())
oex_close.to_csv('index.csv')
