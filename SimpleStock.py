import yfinance as yf
import streamlit as st

def tickerSelected(tickerSymbol):
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    with st.beta_expander("Company Summary"):
        col1, col2, = st.beta_columns([1,4])
        with col1:
            st.image(tickerData.info['logo_url'], use_column_width=True)
        with col2:
            st.write(tickerData.info['longBusinessSummary'])
    #get the historical prices for this ticker

    tickerDf = tickerData.history('max')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.area_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
    st.line_chart(tickerDf.Dividends)

def allSelected(tickerSymbol): 
        #get data on this ticker
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
#Iterate to get all the tickerNames
for option in tickersOptions:
    stockNames.append(option['stockName'])

option = st.sidebar.selectbox('Select your ticket',stockNames)
for stock in tickersOptions:
    if option == stock['stockName']:
        tickerSelected(stock['ticker'])









