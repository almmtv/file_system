# -*-coding:utf-8 -*-
import socket
import uuid
import json
import winreg
import os
from cryptography.fernet import Fernet
import platform
from tkinter import *
from tkinter import filedialog as fd
import shutil


# функция, шифрующая информацию о компьютере пользователя
def get_info(key):
    cipher = Fernet(key)
    # получение информации о компьютере пользователя
    info = {}
    for i in os.environ:
        info[i] = os.environ[i]
    info['platform'] = platform.system()
    info['platform-release'] = platform.release()
    info['platform-version'] = platform.version()
    info['architecture'] = platform.machine()
    info['hostname'] = socket.gethostname()
    info['ip-address'] = socket.gethostbyname(socket.gethostname())
    info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['processor'] = platform.processor()
    info = json.dumps(info)
    info = info.encode('utf-8')
    # шифрование полученной информации
    encrypted_text = cipher.encrypt(info)
    return encrypted_text


def secure():
    a = "sys.tat"
    os.system("icacls " + a + " /deny *S-1-1-0:F")

    # функция, которая запрашивает ключ пользователя и при его совпадении показывает информацию из sys.tat
    def check():
        if e1.get() == 'Alibutaev':
            a = "sys.tat"
            os.system("icacls " + a + " /grant *S-1-1-0:F")
            d = []
            with open('sys.tat', 'r') as sy:
                for i in sy:
                    i = i.rstrip()
                    d += [i]
            os.system("icacls " + a + " /deny *S-1-1-0:F")
            t1.insert(1.0, str(d[0]))
        else:
            root1.destroy()
    root1 = Tk()
    f1 = Frame()
    f2 = Frame()
    e1 = Entry(f1)
    l1 = Label(f1, text='Введите ключ')
    t1 = Text(f2)
    b1 = Button(f1, text='Подтвердить', command=check)
    f1.pack(side=LEFT)
    f2.pack(side=LEFT)
    l1.pack(anchor=CENTER, padx=3, pady=3)
    e1.pack(anchor=CENTER, padx=3, pady=3)
    b1.pack(anchor=CENTER, padx=3, pady=3)
    t1.pack(anchor=CENTER)
    root1.mainloop()


def write_to_registry(in_key):
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    try:
        open_key = winreg.OpenKey(reg, os.path.join('Software', 'Alibutaev'), 0, winreg.KEY_READ)
        open_key2 = winreg.QueryValueEx(open_key, 'User Key')
        return open_key2[0]
    except:
        open_key = winreg.OpenKey(reg, 'Software', 0, winreg.KEY_WRITE)
        open_key2 = winreg.CreateKeyEx(open_key, "Alibutaev")
        winreg.SetValueEx(open_key2, "User Key", 0, winreg.REG_SZ, in_key.decode())
        return in_key


def yes():
    root.quit()
    # запрос у пользователя папки для копирования информации
    a = fd.askdirectory()
    # запись исполняемого файла secure.exe
    b = a + '/secure.exe'
    shutil.copyfile('secure.exe', b, follow_symlinks=True)
    # переход в выбранную пользователем папку
    os.chdir(a)
    # записываем зашифрованную информацию в sys.tat
    cipher_key = Fernet.generate_key()
    key = write_to_registry(cipher_key)
    with open('sys.tat', 'w') as f:
        f.write(str(get_info(key)))
    root.destroy()
    secure()


# функция, которая заканчивает программу
def no():
    root.destroy()


# графический интерфейс
root = Tk()
root.title('Приложение "Блокнот" готово для обновления')
root.geometry('400x70')
root.resizable(False, False)
f1 = Frame()
f2 = Frame()
l1 = Label(f1, text='Обновить сейчас?')
b1 = Button(f2, text='Да', bg='grey', command=yes)
b2 = Button(f2, text='Нет', command=no)
f1.pack(side=TOP)
f2.pack(side=BOTTOM)
l1.pack(anchor=CENTER, pady=10)
b2.pack(side=RIGHT, anchor=SW, padx=2)
b1.pack(side=RIGHT, anchor=SW, padx=2)
root.mainloop()