# e)sum of children born in 2000 - 2005

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

print(inform[(inform["Rok"] >= 2000) &
             (inform["Rok"] <= 2005)]["Liczba"].sum())
