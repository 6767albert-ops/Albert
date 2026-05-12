from sympy import *

k, T, C, L = symbols("k T C L")
# 1-й способ
C_ost = 100000
Am_lst = []
C_ost_lst = []
for i in range(5):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 100000, T: 5, L: 0})
    Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst: ", Am_lst)
print("C_ost_lst: ", C_ost_lst)
# 2-й способ 100000
Aj = 0
C_ost = 100000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 100000, T: 5, k: 2})
    Am_lst_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2: ", Am_lst_2)
print("C_ost_lst_2: ", C_ost_lst_2)
# 1-й способ 30000

C_ost = 30000
Am_lst = []
C_ost_lst = []
for i in range(8):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 30000, T: 8, L: 0})
    Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst: ", Am_lst)
print("C_ost_lst: ", C_ost_lst)
# 2-й способ
Aj = 0
C_ost = 30000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 30000, T: 8, k: 2})
    Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2: ", Am_lst_2)
print("C_ost_lst_2: ", C_ost_lst_2)
# Представление в таблице
import pandas as pd

Y = range(1, 9)
table1 = list(zip(Y, Am_lst, C_ost_lst))
table2 = list(zip(Y, Am_lst_2, C_ost_lst_2))
tframe = pd.DataFrame(table1, columns=["Y", "Am_lst", "C_ost_lst"])
tframe2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2", "C_ost_lst_2"])
print(tframe)
print(tframe2)

# контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tframe["Y"], tframe["C_ost_lst"], label="Am_lst")
plt.savefig("chart1.png")
plt.plot(tframe2["Y"], tframe2["C_ost_lst_2"], label="Am_lst_2")
plt.savefig("chart2.png")
# круговая диаграмма по 1 способу
vals = Am_lst
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart3.png")
# круговая диаграмма по 2 способу
vals = Am_lst_2
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart4.png")

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "Am_lst"])
tfame2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.figure()
plt.bar(tfame["Y"], tfame["Am_lst"])
plt.savefig("chart5.png")
plt.close()
plt.figure()
plt.bar(tfame2["Y"], tfame2["Am_lst_2"])
plt.savefig("chart6.png")
plt.close()


# 1-й способ
from sympy import *

C_ost = 40000
Am_lst = []
C_ost_lst = []
k, T, C, L = symbols("k T C L")
for i in range(10):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 40000, T: 10, L: 0})
    Am_lst.append(round(Am.subs({C: 40000, T: 10, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst: ", Am_lst)
print("C_ost_lst: ", C_ost_lst)

Aj = 0
C_ost = 40000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(10):
    Am = k * 1 / T * (C - Aj)
    Am_value = Am.subs({C: 40000, T: 5, k: 2})
    C_ost -= Am_value
    Am_lst_2.append(round(Am_value, 2))
    Aj += Am_value  # Исправлено: Aj должен накапливать значения амортизации
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2: ", Am_lst_2)
print("C_ost_lst_2: ", C_ost_lst_2)

# Представление в таблице
import pandas as pd

Y = range(1, 11)  # Изменено с 1,9 на 1,11 для 10 значений
table1 = list(zip(Y, Am_lst, C_ost_lst))
table2 = list(zip(Y, Am_lst_2, C_ost_lst_2))
tframe = pd.DataFrame(table1, columns=["Y", "Am_lst", "C_ost_lst"])
tframe2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2", "C_ost_lst_2"])
print(tframe)
print(tframe2)

# контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.figure()  # Добавлен новый figure
plt.plot(tframe["Y"], tframe["C_ost_lst"], label="Am_lst")
plt.savefig("chart1.png")
plt.close()  # Закрываем figure
plt.figure()  # Новый figure для второго графика
plt.plot(tframe2["Y"], tframe2["C_ost_lst_2"], label="Am_lst_2")
plt.savefig("chart2.png")
plt.close()  # Закрываем figure

# круговая диаграмма по 1 способу
vals = Am_lst
labels = [str(x) for x in range(1, 11)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart3.png")
plt.close()

# круговая диаграмма по 2 способу
vals = Am_lst_2
labels = [str(x) for x in range(1, 11)]  # Изменено с 1,9 на 1,11
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # Добавлен 10-й элемент
fig, ax = plt.subplots()
ax.pie(
    vals,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart4.png")
plt.close()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "Am_lst"])
tfame2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.figure()
plt.bar(tfame["Y"], tfame["Am_lst"])
plt.savefig("chart5.png")
plt.close()
plt.figure()
plt.bar(tfame2["Y"], tfame2["Am_lst_2"])
plt.savefig("chart6.png")
plt.close()
