from random import *
from module import *
from tkinter import *
root = Tk()
root.geometry('500x200')  
root.title('Камень,Ножницы,Бумага')
vsbot=Button(root,text='Играть против бота',font='Arial 16',command=vsbot_)
botvsbot=Button(root,text='Бот против бота',font='Arial 16',command=botvsbot_)
nazvanie=Label(root,text='Камень,Ножницы,Бумага',font='Arial 24')
rezult=Button(root,text='Результаты игр',font='Arial 16')
nazvanie.pack(side=TOP)
vsbot.pack(side=TOP)
botvsbot.pack(side=TOP)
rezult.pack(side=TOP)


root.mainloop()
