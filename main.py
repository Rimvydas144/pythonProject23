from calendar import Month
from functools import reduce
import random
from operator import index

import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3]
# y = [2, 3, 4]
# grafikas, asys = plt.subplots()
# asys.scatter(x ,y, color='red')
# asys.set_ylabel('Y ašies pavadinimas')
#
# plt.show()

# ---------------------------------------

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = int(input("Kokia a reiksmė?"))
# y1 = [i**2 for i in x]
# y2 = [i*3 for i in x]
# y3 = [i*a for i in x]
# grafikas, axis = plt.subplots()
# axis.plot(x, y1, color ="red", linestyle = "-", label = "Pakelta kvadratu")
# axis.plot(x, y2, color = "blue", linestyle = "--", label = "Padauginta is 3")
# axis.plot(x, y3, color = "green", linestyle = ":", label = "Padauginta is ivestos reiksmes")
# axis.legend()
# plt.show()

# --------------------------------------------

# x = [1, 2, 3, 4, 5]
# y1 = [2, 2, 0, 0, 2]
# y2 = [4, 3, 2, 1, -1]
# y3 = [2, 4, 9, 16, 25]
# y4 = [-1, 1, -1, 1, -1]
# grafikas, axis = plt.subplots()
# axis.plot(x, y1, color ="red", label = "y1")
# axis.scatter(x, y2, color = "blue", label = "y2")
# axis.plot(x, y3, color = "green", marker = "x", label = "y3")
# axis.plot(x, y4, color = "black", linestyle = "-", label = "y4")
# axis.legend()
# axis.set_xlabel("X asis")
# axis.set_ylabel("Y asis")
# plt.show()

# --------------------------------------

# x = list(range(101))
# x2 = [i**2 for i in x]
# x3 = [i* random.randint(1, 10) for i in x2]
# x4 = [random.randint(1, 100) for i in range(100)]
# grafikas, axis = plt.subplots()
# axis.plot(x, color ="red", label = "sugeneruota is eiles")
# axis.plot(x2, color = "blue", label = "pakelta kvadratu")
# axis.plot(x3, color = "green", marker = "x", label = "padauginta is dvieju")
# axis.plot(x4, color = "black", linestyle = "-", label = "sugeneruota atsitiktinai")
# axis.legend()
# axis.set_xlabel("X asis")
# axis.set_ylabel("Y asis")
# plt.show()

# ----------------------------------------
# Temp = [-3.2,-3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3, +7.2, +1.9,-1.9]
# Month = ['Sausis', 'Vasaris', 'Kovas', 'Balandis', 'Geguze', 'Birzelis', 'Liepa', 'Rugpjutis', 'Rugsejis', 'Spalis', 'Lapkritis', 'Gruodis']
# color = ['blue' if temp < 0 else 'green' for temp in Temp]
# plt.bar(Month, Temp, color = color)
# plt.xlabel("Menesiai")
# plt.ylabel("Temperatura")
# plt.title("Vidutines menesiu temperaturos")
# plt.xticks(rotation = 90)
# plt.tight_layout()
# plt.show()

# ---------------------------------------------

# Month = ['January', 'February', 'March', 'April', 'May']
# Sales = [1500, 2000, 1800, 2200, 2100]
# plt.bar(Month, Sales, color = "skyblue")
# plt.title("Menesiniai imones pardavimai")
# plt.xlabel("Menesiai")
# plt.ylabel("Pardavimai")
# plt.show()

# --------------------------------------------------

# categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Others']
# expences = [40, 25, 15, 10, 10]
# explode = [0.1 if i ==expences.index(max(expences)) else 0 for i in range(len(expences))]
# plt.figure(figsize=(7,7))
# plt.pie(expences, labels = categories, autopct='%1.1f%%', startangle = 140, explode=explode, colors=['blue', 'green', 'purple','black', 'red'])
# plt.title('Islaidos')
# plt.show()

# ----------------------------------------------------



