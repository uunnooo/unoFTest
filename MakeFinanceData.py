# Stock data와 Financial data 합치기

import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import economicSignal

import matplotlib

from datetime import datetime

# pathF = 'D:\\정윤호\\FinanceData\\TestData\\'
pathF = 'D:\\uno\\unoFinance\\'
eList = economicSignal.reportList
eDataList = pd.DataFrame()

for ticker in eList :
    print(ticker)
    eData = fdr.DataReader(ticker, data_source='fred')
    eDataList = pd.concat([eDataList,eData],axis=1)


stocks = fdr.StockListing('NASDAQ') # 나스닥

ticker1 = 'AAPL'
fTicker = yf.Ticker(ticker1)

'''
# ticker 선언


sData = fdr.DataReader(ticker1, '2010-01-01', data_source='investing')
fTmpData = fTicker.get_financials(freq='quarterly')
fData = fTmpData.T

rData = pd.concat([sData,fData],axis=1)
rData.reset_index(inplace = True)

fTmpData = fTicker.get_financials(freq='quarterly')
fTmpData.to_csv(pathF+'FinanceData.csv')
'''




