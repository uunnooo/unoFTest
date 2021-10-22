import plotly.graph_objects as go
import FinanceDataReader as fdr
from talib import abstract
from plotly.offline import plot


df = fdr.DataReader('lcid', '2020',data_source='investing')
df = df.reset_index()
df.columns = ['date', "close", "open", "high", "low", "volume", "change"]

Lma = abstract.MACDFIX(df, signalperiod = 9)
Lma['date'] = df['date']
Lma_na = Lma.dropna()

data = go.Bar(x = Lma_na['date'], y = Lma_na['macdhist'])

layout = dict(title='timeline meal orders',
              xaxis = dict(type='category',categoryorder='category ascending'))

fig = dict(data=data, layout=layout)

plot(fig)