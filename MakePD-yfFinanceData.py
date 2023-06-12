import pandas as pd
import datetime as date
from plotly.subplots import make_subplots
from pyparsing import col
from plotly import tools
import plotly.offline as offline
import plotly.graph_objs as go
import yfinance as yf

end_date = date.date.today().isoformat()
start_date = (date.date.today() - date.timedelta(days =365)).isoformat() #불러올 기간 설정

msft = yf.Ticker("MSFT")

# path = 'C:/python/plotly.ipynb/'
# ticker_df = pd.read_csv(path+"Yahoo Ticker Symbols_stock.csv", engine='python', encoding='utf-8')
ticker_list = ["soxl","soxs","labu","labd"]

df = yf.download(ticker_list, start = start_date , end = end_date)

df_test = df

df_test = pd.DataFrame(df.unstack()).reset_index() #unstack을 통해 multi columns 풀어주기
df_test.rename(columns={'level_0':'item',0:'value','level_1':'Ticker'},inplace=True) #자동 지정된 컬럼명 변경

df_test_re = pd.pivot_table(df_test,index=[df_test.Date,df_test.Ticker] ,columns='item',values='value') # Pivot_table 구성
df_test_re.sort_values(by=['Ticker','Date'],inplace=True)
df_test_re.reset_index(inplace=True)
df_test_re.drop_duplicates(subset=['Ticker','Date'],inplace = True)

tmpDF = df_test_re[df_test_re['Ticker'] == 'SOXL']

fig = go.Figure(data=[go.Candlestick(x=tmpDF['Date'],
                open=tmpDF['Open'], high=tmpDF['High'],
                low=tmpDF['Low'], close=tmpDF['Close'])
                      ])
fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])

fig.show()






