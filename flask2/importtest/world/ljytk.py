from tkinter import *

app = Tk()
app['background']='black'
app.title("pack test window")

app.geometry("400x300+200+100")

lb1 = Label(app, text= "达达杀猪菜", bg='blue', fg='white',font=13,relief="groove")
lb1.pack( ipady=10,side=TOP,anchor=W,expand='no',fill=X)

lb1 = Label(app, text= "python tkinter", bg='green', fg='white',font=13)
lb1.pack(fill=Y, ipady=10,side=LEFT)

lb1 = Label(app, text= "大爷", bg='brown', fg='orange',font=13)
lb1.pack( ipady=10,side='bottom',padx=0,fill='x')

lb1 = Label(app, text= "狗轮", bg='yellow', fg='blue',font=13)
lb1.pack(ipady=10,side=LEFT,)

lb1 = Label(app, text= "土地伦", bg='pink', fg='white',font=13,anchor=W)
lb1.pack( ipady=10,side=RIGHT,padx=0,expand=Y,fill=X,)





app.mainloop()