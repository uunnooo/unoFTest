# Stock data와 Financial data 합치기

import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
from datetime import datetime

# ticker 선언
ticker1 = 'AAPL'
fTicker = yf.Ticker(ticker1)

sData = fdr.DataReader(ticker1, '2010-01-01', data_source='investing')
fTmpData = fTicker.get_financials(freq='quarterly')
fData = fTmpData.T

rData = pd.concat([sData,fData],axis=1)

rData.reset_index(inplace = True)