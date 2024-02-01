# f)the average order amount in 2004

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

f = inform2[(inform2["Data zamowienia"] >= "2004-01-01") &
         (inform2["Data zamowienia"] <= "2004-12-31")]

print(f["Utarg"].mean())