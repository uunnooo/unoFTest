# 여기서는 일단 주식 관련 정보들을 불러 올꺼야 주식 가격들 같은
import FinanceDataReader as fdr
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import cufflinks as cf
from datetime import datetime

tiker1 = 'AAPL'

NG = fdr.DataReader('NG', '2010-01-01', data_source='investing')
GLNG = fdr.DataReader('GLNG', '2010-01-01', data_source='investing')
AAPL = fdr.DataReader('AAPL', '2010-01-01', data_source='investing')

# Pandas 프레임을 바로 피규어로 만들기 위해서는 Date를 인데스에서 빼내야됨
NG.reset_index(inplace = True)
GLNG.reset_index(inplace = True)
AAPL.reset_index(inplace = True)




fig = NG.figure(kind = 'line', x = 'Date', y = 'Close', title = 'No Index')
# fig2 = GLNG.figure(kind = 'line', x = 'Date', y = 'Close', title = 'No Index')
# fig3 = AAPL.figure(kind = 'line', x = 'Date', y = 'Close', title = 'No Index')

# 데이터 길이가 달라서 오버 플랏이 안된다
# fig1.add_trace(fig2)


# plotly를 이용한 그래프 그리기


# fig = go.Figure()

# fig.add_trace(go.Scatter(x=NG['Date'], y=NG['Close'], name='NG'))
fig.add_trace(go.Scatter(x=GLNG['Date'], y=GLNG['Close'], name='GLNG'))
# fig.update_layout(hovermode='x unified')
fig.show()
#
# fig.show