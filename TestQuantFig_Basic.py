import FinanceDataReader as fdr
import cufflinks as cf

 '''
 
 # 쥬피터에서밖에 실행이 안됨
 
cf.set_config_file(sharing='public',theme='pearl',offline=False)
cf.go_offline()
cf.go_offline(connected=True)
apple = fdr.DataReader('AAPL', '2020',data_source='investing')
qf=cf.QuantFig(apple,title='Apple',legend='top',name='AAPL')
qf.add_volume()
qf.add_macd()
qf.add_bollinger_bands()

qf.iplot()

'''




