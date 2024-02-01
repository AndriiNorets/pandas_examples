# e)the total orders for 2005,for vendors from Poland

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

e = inform2[(inform2["Data zamowienia"] >= "2005-01-01") &
         (inform2["Data zamowienia"] <= "2005-12-31")]

result = e.groupby(["Sprzedawca"])["idZamowienia"].count()

print(result,'\n',"Result: ", result.sum())