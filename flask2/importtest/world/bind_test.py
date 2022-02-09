from tkinter import *
from tkinter.ttk import *
tk = Tk()  # 父窗口类实例
tk.title("bind用法实例")  # 窗口标题


def LoveChina(event):  # 定义回调函数
    # x1 = Label(tk, text='我爱你中国！', relief='groove')
    x1 = Label(tk, text='我爱你中国！', )
    x1.pack(pady=5,side=LEFT,padx=10)


x2 = Button(tk, text='单击左键试试')  # 定义一个按钮
x2.bind('<Button-1>', LoveChina)  # 单击鼠标左键，绑定LoveChina()函数
x2.pack()

tk.mainloop()
