import pandas as pd
import numpy as np

xls = pd.ExcelFile('imiona.xlsx')
inform = pd.read_excel(xls)

# Display(using thePandas library function if possible)
# a)only those records where the number of given names was greater than 1000 in a given year
# print(inform[inform["Liczba"]>1000])

# b)only records where the given name is the same as yours
# print(inform[inform["Imie"]=="ANDRZEJ"])

# c)sum of all children born in all years
# print(inform["Liczba"].sum())

# d)sum of all children born in each year
sum_of_children = inform.groupby(["Rok"])["Liczba"].sum()
# print(sum_of_children)

# e)sum of children born in 2000 - 2005
# print(inform[(inform["Rok"] >= 2000) &
#              (inform["Rok"] <= 2005)]["Liczba"].sum())

# f)the sum of boys and girls born
boys = inform[inform["Plec"]=="M"]["Liczba"].sum()
girls = inform[inform["Plec"]=="K"]["Liczba"].sum()
# print(boys,girls)

# g)the most popular girl's and boy's name in all years
# print("Most popular boy's name:\n",
#       inform.loc[(inform["Plec"] == "M") &
#                  (inform["Liczba"] == inform[inform["Plec"] == "M"]["Liczba"].max())],
#       "\n\nMost popular girl's name:\n",
#       inform.loc[(inform["Plec"]=="K") &
#                  (inform["Liczba"] ==  inform[inform["Plec"]=="K"]["Liczba"].max()  )])

# h)the most popular girl's and boy's name in a given year
# h = inform.groupby(['Plec', 'Imie', 'Rok']).agg({'Liczba': ['sum']})
# print(h.groupby(['Plec', 'Rok']).idxmax())



inform2 = pd.read_csv('zamowienia.csv',sep=";")
# display:
# a)a list of unique vendor names(processing the returned single column fromDataFrame)
a = pd.DataFrame(inform2,columns=["Sprzedawca"])
# print(pd.concat([a, a]).drop_duplicates())

# b)the 5 highest order values
b = inform2["idZamowienia"][-5:]
# print(b)

# c)the number of orders placed by each vendor
c = inform2.groupby(["Sprzedawca"])["idZamowienia"].count()
# print(c)

# d)the total orders for each country
d = inform2.groupby(["Kraj"])["idZamowienia"].count()
# print(d)

# e)the total orders for 2005,for vendors from Poland
e = inform2[(inform2["Data zamowienia"] >= "2005-01-01") &
         (inform2["Data zamowienia"] <= "2005-12-31")]
result = e.groupby(["Sprzedawca"])["idZamowienia"].count()
# print(result)

# f)the average order amount in 2004
f = inform2[(inform2["Data zamowienia"] >= "2004-01-01") &
         (inform2["Data zamowienia"] <= "2004-12-31")]
#print(f["Utarg"].mean())

# g)save the data for 2004 to the file orders_2004.csv and the data for 2005 to the file orders_2005.csv
f.to_csv('orders_2004.csv')
e.to_csv('orders_2005.csv')

