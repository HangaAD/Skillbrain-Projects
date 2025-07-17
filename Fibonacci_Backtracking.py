def fibonacci(n,list=None):
    if list is None:
        list=[1]*(n+1)
    if n==0:
        return 0
    if n==1:
        return 1
    list[n]=fibonacci(n-1,list)+fibonacci((n-2),list)
    return list[n]
print(fibonacci(2))