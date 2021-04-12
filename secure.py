import os
from tkinter import *


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