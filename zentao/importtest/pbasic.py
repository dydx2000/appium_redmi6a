class Person:
    def __init__(self):
        print("正在执行构造方法")
    # 定义一个study()实例方法
    def study(self):
        print(self,"正在学Python")
zhangsan = Person()
zhangsan.study()
lisi = Person()
lisi.study()