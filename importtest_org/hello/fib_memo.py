memo = [-1] * 100
# print(memo)
def fib(n):
    global memo
    if n == 0:
        # memo[0]=0
        return 0
    elif n == 1:
        # memo[1]=1
        return 1
    else:
        if memo[n] == -1:
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
        else:
            return memo[n]


print(fib(40))
