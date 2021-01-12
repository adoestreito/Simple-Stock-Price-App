import yfinance as yf
import streamlit as st

def allSelected(tickerSymbol): 
    if len(tickerSymbol)==0:
        st.write("Use the menu on the left to select the stocks that you want to compare")
        return
    elif len(tickerSymbol) == 1:
        tickerData = yf.Ticker(tickerSymbol[0])
        
    else:
        tickerData = yf.Tickers(tickerSymbol)
    tickerDf = tickerData.history('max')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.write("""
    ## Close price""")
    st.area_chart(tickerDf.Close)
    st.write("""
    ## Volume""")
    st.line_chart(tickerDf.Volume)
    st.write("""
    ## Dividends""")
    st.line_chart(tickerDf.Dividends)


st.write("""
# Simple Stock Price App
""")

#define the ticker symbol
tickersOptions= [
    {'stockName': 'APPLE',
     'ticker':'AAPL',
    },
    {'stockName': 'MICROSOFT',
     'ticker':'MSFT',
    },
    {'stockName': 'TESLA',
     'ticker':'TSLA',
    },
    {'stockName': 'FASTLY',
     'ticker':'FSLY',
    },
]
stockNames = []
selectedTicker = []

#Iterate to get all the tickerNames
for option in tickersOptions:
    stockNames.append(option['stockName'])

#Multiple selection of tickers
options = st.sidebar.multiselect(
   'Select your tickets',stockNames)
for choice in options:
   for stock in tickersOptions:
    if choice == stock['stockName']:
        selectedTicker.append(stock['ticker'])

allSelected(selectedTicker)











