import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

frm =ttk.Frame(root)
frm.pack()
ttk.Label(frm, text="编程语言").pack(side=tk.LEFT, padx=5, pady=5)

combo = ttk.Combobox(frm, values=["Go", "Python", "Java", "C++"])
# 设置当前选中的项
combo.current(1)
combo.pack(side=tk.LEFT, padx=5, pady=5)



frm1 =ttk.Frame(root)
frm1.pack(side=tk.TOP,fill=tk.X)

# 创建进度条控件
progress = ttk.Progressbar(frm1, mode='indeterminate', length=100)
# progress.pack(pady=10, padx=10)
progress.pack(pady=10, padx=10,expand='no',anchor='w')

# 启动进度条控件
progress.start()

frm3 =ttk.Frame(root)
frm3.pack(fill=tk.X)

progress2 = ttk.Progressbar(frm3, mode='determinate', length=100)
progress2.pack(pady=10, padx=10,anchor='w')
progress2.start()

root.mainloop()