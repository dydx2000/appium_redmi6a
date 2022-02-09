from tkinter import *
from tkinter.ttk import *

__author__ = 'Administrator'

RELIEF = [None,"flat", "raised", "sunken", "solid", "ridge", "groove"]

root = Tk()
root.title("relief演示")
for i in range(len(RELIEF)):
    temp = Frame(root, relief=RELIEF[i], borderwidth=5, width=50, height=50)
    label = Label(temp, text=RELIEF[i])
    label.grid(row=0, column=0)
    temp.grid(row=1, column=i, padx=10, pady=10)

style = Style()
# 获取所有支持的主题
print(style.theme_names())

# 获取当前使用的主题
print(style.theme_use())

# 切换主题
style.theme_use("clam")

root.mainloop()
