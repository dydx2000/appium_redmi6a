from tkinter import *
# 增加如下导包语句即可
# from tkinter.ttk import *

root = Tk()
root.geometry("300x300")

# top = LabelFrame(root, text="Label")
top = Frame(root, )
top.pack(padx=8, pady=8)
Label(top, text="我是标签，哈哈").pack()

body = LabelFrame(root, text="Button")
body.pack(padx=8, pady=8)
Button(body, text="你点啊").pack()

bottom = LabelFrame(root, text="其他")
bottom.pack(padx=8, pady=8)
Checkbutton(bottom, text="唱歌").pack()
Checkbutton(bottom, text="跳舞").pack()
Checkbutton(bottom, text="健身").pack()

Scale(bottom, orient='horizonta', from_=0, to=100).pack()

root.mainloop()