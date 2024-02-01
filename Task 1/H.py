# h)the most popular girl's and boy's name in a given year

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

h = inform.groupby(['Plec', 'Imie', 'Rok']).agg({'Liczba': ['sum']})

print(h.groupby(['Plec', 'Rok']).idxmax())
