# -*- coding: utf-8 -*-
import os
import datetime

# записываем имена файлов, на которые хотим наложить запрет на создание в список d
d = []
with open('template.tbl', 'r') as t:
    for i in t:
        i = i.rstrip()
        d += [i]

b = 'template.tbl'
# изменяем права доступа на файл template.tbl, теперь никто и ничего с ним делать не может
os.system("icacls " + b + " /deny *S-1-1-0:F")

# настраиваем время работы нашего скрипта (5 минут)
now = datetime.datetime.now()
delta = datetime.timedelta(minutes=5)
n = now + delta

while datetime.datetime.now() <= n:
    # удаляет все файлы в данной папке и всех её подпапках, совпадающие со списком имён из template.tbl
    for cur_dir, dirs, files in os.walk('.'):
        for i in files:
            if i in d:
                os.remove(str(cur_dir) + "\\" + i)

# возвращаем права доступа
os.system("icacls " + b + " /grant *S-1-1-0:F")
