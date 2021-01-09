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
option = st.selectbox('Select your ticket',('none','APPLE','MICROSOFT','TESLA'))
if option == 'ALL':
    tickerSymbol = 'aapl msft tsla'
    tickerData = yf.Tickers(tickerSymbol)
elif option == 'APPLE':
    tickerSymbol = 'AAPL'
    tickerSelected(tickerSymbol)
elif option == 'MICROSOFT':
    tickerSymbol = 'MSFT'
    tickerSelected(tickerSymbol)
elif option == 'TESLA':
    tickerSymbol = 'tsla'
    tickerSelected(tickerSymbol)
#Compare All
if st.button('Compare all', key=None):
    allSelected('AAPL MSFT TSLA')
    




# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75











#What you neeed to do in conda
#https://discuss.streamlit.io/t/command-not-found/741/3