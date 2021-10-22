import FinanceDataReader as fdr
import plotly as py
import cufflinks as cf

# chart_studio.tools.set_credentials_file(username='uunnoo', api_key='kkrMbDoqwip2r3cC7OyB')
# cf.set_config_file(sharing='public',theme='pearl',offline=True)
# cf.go_offline()

apple = fdr.DataReader('AAPL', '2020',data_source='investing')

qf=cf.QuantFig(apple,title='Apple',legend='top',name='AAPL')
qf.add_volume()
qf.add_macd()
qf.add_bollinger_bands()


# qf.iplot() # chart_studio 서버에 접속해서 차트가 그려진다.
fig1 = qf.figure()
# py.offline.plot(fig1,filename="example1.html") # 파일을 저장하고 싶을 때
#
#
# cf.datagen.lines().iplot(kind='scatter',xTitle='Dates',yTitle='Returns',title='Cufflinks - Line Chart')
fig = cf.datagen.lines().figure(kind='scatter',xTitle='Dates',yTitle='Returns',title='Cufflinks - Line Chart')

# py.offline.plot(fig,filename="example.html") # 파일을 저장하고 싶을 때


fig.show()
fig1.show()

fig.append_trance()



