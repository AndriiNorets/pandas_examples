# f)the sum of boys and girls born

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

boys = inform[inform["Plec"]=="M"]["Liczba"].sum()
girls = inform[inform["Plec"]=="K"]["Liczba"].sum()

print("Boys:",boys,", Girls:", girls)