# g)the most popular girl's and boy's name in all years

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

boys_name = inform.loc[(inform["Plec"] == "M") &
                 (inform["Liczba"] == inform[inform["Plec"] == "M"]["Liczba"].max())]

girls_name = inform.loc[(inform["Plec"]=="K") &
                 (inform["Liczba"] ==  inform[inform["Plec"]=="K"]["Liczba"].max()  )]

print("Most popular boy's name:\n",
      boys_name,
      "\n\nMost popular girl's name:\n",
      girls_name)