def fibonacci(n):
    a,b =0,1
    count=0
    res =[]
    while True:
        if count>n:
            break
        res.append(a+b)
        a,b = b,a+b
        count +=1
    return res

def fibonacci2(n):
    a,b =0,1
    count=0
    # res =[]

    while True:
        if count>n:
            break
        yield a+b
        a,b = b,a+b
        count+=1

if __name__ == '__main__':
    # print(fibonacci(10))

    gen = fibonacci2(1000000000000)
    for i in gen:
        if i>1000:
            break
        print(i)