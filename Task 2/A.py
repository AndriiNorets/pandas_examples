# a)a list of unique vendor names(processing the returned single column fromDataFrame)

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

a = pd.DataFrame(inform2,columns=["Sprzedawca"])

print(pd.concat([a, a]).drop_duplicates())