# g)save the data for 2004 to the file orders_2004.csv and the data for 2005 to the file orders_2005.csv

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

orders_2005 = inform2[(inform2["Data zamowienia"] >= "2005-01-01") &
         (inform2["Data zamowienia"] <= "2005-12-31")]

orders_2004 = inform2[(inform2["Data zamowienia"] >= "2004-01-01") &
         (inform2["Data zamowienia"] <= "2004-12-31")]


orders_2004.to_csv('orders_2004.csv')
orders_2005.to_csv('orders_2005.csv')