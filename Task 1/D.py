# d)sum of all children born in each year

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

sum_of_children = inform.groupby(["Rok"])["Liczba"].sum()

print(sum_of_children)