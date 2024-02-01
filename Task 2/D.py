# d)the total orders for each country

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

d = inform2.groupby(["Kraj"])["idZamowienia"].count()

print(d)