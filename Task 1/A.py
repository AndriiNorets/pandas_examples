# a)only those records where the number of given names was greater than 1000 in a given year

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

print(inform[inform["Liczba"]>1000])