from random import *
from tkinter import *
def vsbot_():
    global t
    t=0
    def bumaga_():
        p1=randint(1,3)
        if p1==1:
            t=+1
            rezult.configure(text='Ты выйграл, противник выбрал Камень')
        elif p1==2:
            t=-1
            rezult.configure(text='Ты проиграл, противник выбрал Ножницы')
        elif p1==3:
            rezult.configure(text='Ничья, вы оба выбрали Бумагу')
    def kamen_():
        p1=randint(1,3)
        if p1==1:
            rezult.configure(text='Ничья, вы оба выбрал Камень')
        elif p1==2:
            t=+1
            rezult.configure(text='Ты выйграл, противник выбрал Ножницы')
        elif p1==3:
            rezult.configure(text='Ты проиграл, противник выбрал Бумагу')
            t=-1
    def nosh_():
        p1=randint(1,3)
        if p1==1:
            t=+1
            rezult.configure(text='Ты проиграл, противник выбрал Камень')
        elif p1==2:
            rezult.configure(text='Ничья, вы оба выбрал Ножницы')
        elif p1==3:
            rezult.configure(text='Ты выйграл, вы оба выбрали Бумагу')
            t=+1
    okno=Toplevel()
    okno.grab_set()
    okno.geometry('500x200') 
    rezult=Label(okno,text='',font='Arial 16')
    kamen=Button(okno,text='Камень',font='Arial 8')
    nosh=Button(okno,text='Ножницы',font='Arial 8')
    bumaga=Button(okno,text='Бумага',command=bumaga_,font='Arial 8')
    kamen.pack(side=TOP)
    nosh.pack(side=TOP)
    bumaga.pack(side=TOP)
    rezult.pack(side=BOTTOM)

    okno.mainloop()
def botvsbot_():
    def igra():
        p1=randint(1,3)
        p2=randint(1,3)
        if p1==p2:
            print('Ничья')
        elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
            print('Выйграл 1 бот')
        else:
            print('Выйграл 2 бот')
    okno=Toplevel()
    okno.grab_set()
    okno.geometry('500x200') 
    rezult=Label(okno,text='',font='Arial 16')
    dalshe=Button(okno,text='Следующий раунд',font='Arial 10',command=igra)
    rezult.pack(side=BOTTOM)
    dalshe.pack(side=TOP)
    okno.mainloop()