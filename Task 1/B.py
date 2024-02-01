# b)only records where the given name is the same as yours

import pandas as pd

inform = pd.read_excel('imiona.xlsx')

print(inform[inform["Imie"]=="ANDRZEJ"])