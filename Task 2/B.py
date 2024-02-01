# b)the 5 highest order values

import pandas as pd

inform2 = pd.read_csv('zamowienia.csv',sep=";")

b = inform2["idZamowienia"][-5:]

print(b)