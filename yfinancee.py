import yfinance as yf

tickers = yf.Tickers('msft aapl goog')
# ^ returns a named tuple of Ticker objects

# access each ticker using (example)
tickers.tickers.MSFT.info
print(tickers.tickers.MSFT.info)
tickers.tickers.AAPL.history(period="1mo")
tickers.tickers.GOOG.actions




