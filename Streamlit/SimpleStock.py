import yfinance as yf
import streamlit as st
import datetime

def allSelected(tickerSymbol,date,close,volume,dividens): 
    if len(tickerSymbol)==0:
        st.info("Use the menu on the left to select the stocks that you want to compare")
        return
    elif len(tickerSymbol) == 1:
        tickerData = yf.Ticker(tickerSymbol[0])
        
    else:
        tickerData = yf.Tickers(tickerSymbol)
    st.write("Data range: "+date) 
    tickerDf = tickerData.history(date)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    if close:
        st.write("""
        ## Close price""")
        st.area_chart(tickerDf.Close)
    if volume:
        st.write("""
        ## Volume""")
        st.line_chart(tickerDf.Volume)
    if dividens:
        st.write("""
        ## Dividends""")
        st.line_chart(tickerDf.Dividends)
    if not close and not volume and not dividens:
        st.info("Select the data to be shown in the left bar")

#End function

#start app
st.set_page_config(page_title="Simple Stock Price App", page_icon=None, layout='wide', initial_sidebar_state='auto')


st.write("""
# Simple Stock Price App
""")
#teeest

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
    {'stockName': 'GOOGLE',
     'ticker':'GOOG',
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

userInput = st.sidebar.text_input("Input a ticker", value='', max_chars=None, key=None, type='default')
if userInput:
    selectedTicker.append(userInput)


date = st.sidebar.select_slider(
    'Select the date range',
    options=[ '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

st.sidebar.write("Select the data to be shown")
close = st.sidebar.checkbox('Close price')
volume = st.sidebar.checkbox('Volume')
dividens = st.sidebar.checkbox('Dividends')





    

allSelected(selectedTicker,date,close,volume,dividens)












