import twstock
import sqlite3
import pandas as pd

print(twstock.codes['2330'])
stock = twstock.Stock('2330')
#stockData = stock.fetch_from(2020,1)
stock_tw = pd.DataFrame(stock.fetch_from(2020,2))


stock_tw.to_csv('2330_utf.csv', encoding='utf_8_sig')
# 開啟一個名為”股票代號.db"的檔案，並與sqlite3的資料庫連結
#con = sqlite3.connect('Stock.db')
#把df寫入sqlite3裡，參數為(檔名, 資料庫, 取代原始資料)
#df.to_sql(sid, con, if_exists=’replace’)


#print(stockData)
