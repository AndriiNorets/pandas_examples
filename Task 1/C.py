# c)sum of all children born in all years

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

print(inform["Liczba"].sum())