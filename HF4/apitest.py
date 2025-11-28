import yfinance as yf

# a = yf.download(['MSFT'], period='1mo')
# print(a)
dat = yf.Ticker('AAPL')
print(dat.history(period='1mo'))
