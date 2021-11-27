with open('u2_6a.py') as f:
    while True:
        lin = next(f,None)
        if lin is None:
            break
        else:
            print(lin,end='')

with open("app1.py") as app:
    while True:
        try:
            print(next(app),end='')

        except StopIteration:
            print("读取结束。")
            break

