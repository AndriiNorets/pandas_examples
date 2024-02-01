# c)the number of orders placed by each vendor

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

c = inform2.groupby(["Sprzedawca"])["idZamowienia"].count()

print(c)
