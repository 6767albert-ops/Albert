import os
from sympy import *

key1 = os.environ['Papsueva1']
key2 = os.environ['Papsueva2']
key3 = os.environ['Papsueva3']


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

#Индивидуальная часть
import random
import time
import os
import subprocess
import sys
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

SECRET_LOGIN = "admin"
SECRET_PASSWORD = "12345"

print("=== СИСТЕМА АУТЕНТИФИКАЦИИ ===")
user_login = input("Логин: ")
user_password = input("Пароль: ")

if user_login == SECRET_LOGIN and user_password == SECRET_PASSWORD:
    print("Доступ предоставлен!\n")
else:
    print("Ошибка аутентификации. Программа завершена.")
    sys.exit()

hardware_mac = "AA:BB:CC:DD:EE:FF"
interval = 5
duration = 25
mac_switches = 0
log = []

connection_types = ["Wi-Fi", "Bluetooth", "Ethernet"]

def generate_mac():
    if random.random() < 0.1:
        return "FF:FF:FF:FF:FF:FF"
    return ":".join([f"{random.randint(0,255):02X}" for _ in range(6)])

def is_suspicious(mac):
    return mac == "FF:FF:FF:FF:FF:FF"

print("=== ЗАПУСК ЦИКЛА СИМУЛЯЦИИ (25 секунд) ===\n")
start_time = time.time()

while time.time() - start_time < duration:
    if time.time() - start_time >= mac_switches * interval:
        hardware_mac = generate_mac()
        mac_switches += 1
        print(f"MAC сменён на: {hardware_mac} (смена #{mac_switches})")

    if random.random() < 0.6:
        conn_type = random.choice(connection_types)
        source_mac = generate_mac()

        if is_suspicious(source_mac):
            status = "БЛОКИРОВКА (подозрительный MAC)"
            blocked = True
        else:
            status = "РАЗРЕШЁН (нормальный MAC)"
            blocked = False

        event = {
            "timestamp": datetime.now(),
            "source_mac": source_mac,
            "connection_type": conn_type,
            "status": status,
            "blocked": blocked
        }
        log.append(event)
        print(f"[{event['timestamp'].strftime('%H:%M:%S')}] {conn_type} | {source_mac} | {status}")
    else:
        print("Запросов нет...")

    time.sleep(1)

print("\n=== ЦИКЛ ЗАВЕРШЁН ===")

total_events = len(log)
suspicious_count = sum(1 for e in log if e["blocked"])
normal_count = total_events - suspicious_count
conn_counts = {t: 0 for t in connection_types}
for e in log:
    conn_counts[e["connection_type"]] += 1

print("\n=== ТАБЛИЦА СОБЫТИЙ ===")
print(f"{'Время':<10} {'Тип':<10} {'MAC':<20} {'Статус'}")
print("-" * 55)
for e in log[-10:]:
    print(f"{e['timestamp'].strftime('%H:%M:%S'):<10} {e['connection_type']:<10} {e['source_mac']:<20} {e['status']}")

print(f"\nВсего событий: {total_events}")
print(f"Нормальных: {normal_count}")
print(f"Подозрительных (заблокировано): {suspicious_count}")
print(f"Смен MAC: {mac_switches}")

def create_plots():
    plt.figure(figsize=(12,8))
    plt.subplot(2,2,1)
    plt.plot(range(mac_switches), [mac_switches]*mac_switches, 'b-')
    plt.title("Динамика смен MAC")
    plt.xlabel("Смена")
    plt.ylabel("Количество")

    plt.subplot(2,2,2)
    plt.bar(["Нормальные", "Подозрительные"], [normal_count, suspicious_count], color=["green", "red"])
    plt.title("Статусы подключений")

    plt.subplot(2,2,3)
    plt.pie(conn_counts.values(), labels=conn_counts.keys(), autopct='%1.1f%%')
    plt.title("Типы подключений")

    plt.subplot(2,2,4)
    plt.pie([suspicious_count, normal_count], labels=["Подозрительные", "Нормальные"], 
            colors=["red", "green"], autopct='%1.1f%%')
    plt.title("Анализ подозрительных MAC")

    plt.tight_layout()
    plt.savefig("results.png")
    plt.show()

create_plots()

with open("Stepanov2.sh", "w") as f:
    f.write("""#!/bin/bash
python3 main.py
echo "Программа выполнена"
""")
os.chmod("Stepanov2.sh", 0o755)
print("Скрипт Stepanov2.sh создан")

GITHUB_USERNAME = "ваш_логин"
GITHUB_TOKEN = "ваш_токен"
REPO_NAME = "LR3"

print("\n=== РАБОТА С GIT ===")
print("1. Создайте репозиторий LR3 на GitHub вручную")
print("2. Затем запустите следующие команды в терминале Replit:")
print(f"""
git init
git add .
git commit -m "Initial commit: LR3 implementation"
git remote add origin https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git
git branch -M main
git push -u origin main
""")

print("\n=== ЗАДАНИЕ ВЫПОЛНЕНО ===")
print("Все пункты 1-37 реализованы.")