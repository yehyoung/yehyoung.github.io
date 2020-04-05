import csv

with open('test.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)            # 取得寫CSV寫檔物件
    writer.writerow(['A', 'B', 'c'])        # 寫入資料



import csv
table = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3']
]

with open('test.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)              # 取得寫CSV寫檔物件
  writer.writerows(table)                   # 寫入資料


import csv
with open('test.csv', 'w') as csvfile:
    fieldnames = ['ColumnName1', 'ColumnName2', 'ColumnName3']      # 定義每一欄的名稱
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
    writer.writeheader()                                            # 寫入欄位名稱
    writer.writerow({'A1': 'A', 'A2': 2, 'A3': 3})
    writer.writerow({'B1': 'B', 'B2': 2, 'B3': 3})




import csv

with open('test.csv') as csvfile:  
  rows = csv.reader(csvfile)        # 讀取全部列

  for row in rows:
    print(row)


import csv
with open('test.csv') as csvfile:  
  rows = csv.reader(csvfile, delimiter=':')     # 指定分隔符號
  for row in rows:
    print(row)    


import csv
with open('iris.csv') as csvfile:
  rows = csv.DictReader(csvfile)    # 將每列讀成一個dict
  for row in rows:
    print(row[0], row[1])