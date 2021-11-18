import pandas as pd
import tradingeconomics as te

te.login()

#without a client key only a small sample of data will be given.

# #Getting indicators data by country and indicator Output type will be pandas dataframe
# mydata = te.getIndicatorData(country = 'United States', indicators = 'Imports', output_type = 'df')
# print(mydata)
#
# print("===============================================================================================================")
#
# #Putting country name or indicator name in square brackets the result, by default, will be of the dictionary type. For several countries and indicators
# mydata = te.getIndicatorData(country = ['United States', 'Portugal'], indicators = ['Imports','Exports'], output_type = 'df')
# print(mydata)
#
# print("===============================================================================================================")
#
# #To get ypur data into a csv file
# mydata = te.getIndicatorData(country='United states',indicators=['Imports', 'Exports', 'gdp'], output_type = 'df')
#
# df = pd.DataFrame(mydata)
# df.to_csv('indicators.csv', index=False, header=True, sep='|')
#
# #If you want the code into an html table format you can use in your html projects
# print(mydata.to_html())

te.getIndicatorData(country=['united states', 'china'], output_type='df')

# te.getHistoricalData(country='united kingdom', indicator='pmi')
# te.getHistoricalData(country='united kingdom', indicator='gdp', initDate='2015-01-01')

# te.getHistoricalData(country=['united states', 'china'], indicator=['exports','imports'], initDate='1990-01-01', endDate='2015-01-01')