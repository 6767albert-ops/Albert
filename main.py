import os
from sympy import *



#Общая часть
#1-й способ 
C_ost = 50000 #Изменения успешно выполнены - 5 баллов
Am_lst=[]
C_ost_lst=[]
k,T,C,L = symbols('k T C L') # Что это означает?
for i in range (10):
  Am=(C-L)/T
  C_ost -= Am.subs({C:50000, T:10, L:0}) #Эта строка вычитает из переменной C_ost результат подстановки значений в символьное выражение.
  Am_lst.append(round(Am.subs({C:50000, T:10, L:0}),2))
  C_ost_lst.append(round(C_ost,2))
print('Am_lst: ', Am_lst) 
print('C_ost_lst: ',C_ost_lst)

Aj=0
C_ost=50000 
Am_lst_2=[]
C_ost_lst_2=[]
for i in range (10):
  Am= k*1/T*(C-Aj)
  Am_value = Am.subs({C:50000, T:5, k:2})
  C_ost -= Am_value
  Am_lst_2.append(round(Am_value,2))
  Aj += Am_value  
  C_ost_lst_2.append(round(C_ost,2))
print ('Am_lst_2: ', Am_lst_2)
print ('C_ost_lst_2: ', C_ost_lst_2)

#Представление в таблице
import pandas as pd
Y= range(1,11) #создаёт последовательность целых чисел от 1 до 10.
table1=list(zip(Y,Am_lst,C_ost_lst)) #Что это означает?
table2=list(zip(Y,Am_lst_2,C_ost_lst_2))
tframe=pd.DataFrame(table1,columns=['Y','Am_lst','C_ost_lst'])
tframe2=pd.DataFrame(table2,columns=['Y','Am_lst_2','C_ost_lst_2'])
print(tframe)
print(tframe2)

#контейнер визуализации 
import numpy as np
import matplotlib.pyplot as plt
plt.figure()  # Добавляет новый figure
plt.plot(tframe['Y'],tframe['C_ost_lst'],label='Am_lst')
plt.savefig('chart1.png')
plt.close()  
plt.figure()  
plt.plot(tframe2['Y'],tframe2['C_ost_lst_2'],label='Am_lst_2') #Что это означает?
plt.savefig('chart2.png')
plt.close()  

#круговая диаграмма по 1 способу
vals=Am_lst
labels=[str(x) for x in range(1,11)]  
explode =(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)  
fig,ax=plt.subplots()
ax.pie(vals,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,wedgeprops={'lw':1,'ls':'--','edgecolor': "k"},rotatelabels=True)
ax.axis("equal")
plt.savefig('chart3.png')
plt.close()

#круговая диаграмма по 2 способу
vals=Am_lst_2
labels=[str(x) for x in range(1,11)]  # Изменено с 1,9 на 1,11
explode =(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)  # Добавлен 10-й элемент
fig,ax=plt.subplots()
ax.pie(vals,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,wedgeprops={'lw':1,'ls':'--','edgecolor': "k"},rotatelabels=True)
ax.axis("equal")
plt.savefig('chart4.png')
plt.close()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
plt.figure()
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart5.png')
plt.close()
plt.figure()
plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.savefig('chart6.png')
plt.close()

#Индивидуальное задание
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def simulate_requests(num_requests=20):
    data = []
    connection_types = ["Wi-Fi", "Bluetooth", "Ethernet"]
    for i in range(num_requests):
        conn_type = random.choice(connection_types)
        mac = ":".join([f"{random.randint(0,255):02X}" for _ in range(6)])
        if random.random() < 0.15:
            mac = "FF:FF:FF:FF:FF:FF"
        is_suspicious = (mac == "FF:FF:FF:FF:FF:FF")
        status = "Блокировка" if is_suspicious else "Разрешён"
        data.append({
            "ID": i+1,
            "Время": datetime.now().strftime("%H:%M:%S"),
            "Тип": conn_type,
            "MAC источника": mac,
            "Статус": status
        })
    return pd.DataFrame(data)

df = simulate_requests(15)

print("=== ТАБЛИЦА РЕЗУЛЬТАТОВ ===")
print(df.to_string(index=False))


plt.figure(figsize=(8, 6))
status_counts = df["Статус"].value_counts()
plt.bar(status_counts.index, status_counts.values, color=["green", "red"])
plt.title("Статусы подключений")
plt.xlabel("Статус")
plt.ylabel("Количество")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("status.png")
plt.show()
print("График 1 сохранён: status.png")


plt.figure(figsize=(8, 6))
type_counts = df["Тип"].value_counts()
plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Типы подключений")
plt.savefig("types.png")
plt.show()
print("График 2 сохранён: types.png")


plt.figure(figsize=(10, 6))


import random
response_times = [random.uniform(0.1, 2.0) for _ in range(len(df))]
df['Время_обработки'] = response_times

plt.plot(df['ID'], df['Время_обработки'], 'b-o', linewidth=2, markersize=6)
plt.title("Динамика времени обработки запросов")
plt.xlabel("Номер запроса")
plt.ylabel("Время обработки (сек)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("dynamics.png")
plt.show()
print("График 3 сохранён: dynamics.png")


plt.figure(figsize=(8, 6))
suspicious = df[df["MAC источника"] == "FF:FF:FF:FF:FF:FF"].shape[0]
normal = len(df) - suspicious
plt.pie([suspicious, normal], labels=["Подозрительные", "Нормальные"], 
        colors=["red", "green"], autopct='%1.1f%%', startangle=90)
plt.title("Анализ подозрительных MAC")
plt.savefig("analysis.png")
plt.show()
print("График 4 сохранён: analysis.png")

print("\n=== ВСЕ ГРАФИКИ СОХРАНЕНЫ В ОТДЕЛЬНЫХ ФАЙЛАХ ===")
print("1. status.png  — статусы подключений")
print("2. types.png   — типы подключений")
print("3. dynamics.png — динамика запросов")
print("4. analysis.png — анализ подозрительных MAC")