import yfinance as yf

GetFacebookInformation = yf.Ticker("FB")
print(GetFacebookInformation.info)
