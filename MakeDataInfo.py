import yfinance as yf
import pandas as pd

msft = yf.Ticker("MSFT")

pathF = 'F:\\정윤호\\FinanceData\\TestData\\'

# get stock info
# msft.info
pd.DataFrame.from_dict(msft.info, orient = 'index').to_csv(pathF+'infoData.csv')

# get historical market data
#hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions
msft.actions.to_csv(pathF+'actionData.csv')
# show dividends
msft.dividends
msft.dividends.to_csv(pathF+'dividendsData.csv')
# show splits
msft.splits
msft.splits.to_csv(pathF+'splitsData.csv')
# show financials
msft.financials
msft.financials.to_csv(pathF+'financialsData.csv')
#msft.quarterly_financials

# show major holders
#msft.major_holders

# show institutional holders
#msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.balance_sheet.to_csv(pathF+'balance_sheetData.csv')
#msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.cashflow.to_csv(pathF+'cashflowData.csv')
#msft.quarterly_cashflow

# show earnings
msft.earnings
msft.earnings.to_csv(pathF+'earningsData.csv')
#msft.quarterly_earnings

# show sustainability
#msft.sustainability

# show analysts recommendations
#msft.recommendations

# show next event (earnings, etc)
#msft.calendar
msft.calendar.to_csv(pathF+'calendarData.csv')

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
#msft.isin

# show options expirations
msft.options
# msft.options.to_csv(pathF+'optionsData.csv') # 값이 없음
# show news
msft.news
pd.DataFrame.from_dict(msft.news).to_csv(pathF+'news.csv')